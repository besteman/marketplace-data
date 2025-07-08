#!/usr/bin/env python3
"""
Script to generate seed.sql file from marketplace_plans.json
Creates INSERT statements for the marketplace_plans table using the MarketplacePlanJSON model
"""

import json
import sys
from pathlib import Path
from typing import Any

# Add src to path to import models
sys.path.append(str(Path(__file__).parent.parent))

from models.model import MarketplacePlanJSON


def escape_sql_string(value: Any) -> str:
    """Escape a value for SQL insertion"""
    if value is None:
        return "NULL"
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    if isinstance(value, (int, float)):
        if str(value).lower() in ('nan', 'inf', '-inf'):
            return "NULL"
        return str(value)
    if isinstance(value, str):
        # Escape single quotes and backslashes
        escaped = value.replace("'", "''").replace("\\", "\\\\")
        return f"'{escaped}'"
    return f"'{str(value)}'"


def get_table_columns() -> list[str]:
    """Get the column names from the MarketplacePlanJSON model in the correct order"""
    # Get field names from the Pydantic model
    model_fields = MarketplacePlanJSON.model_fields.keys()

    # Add id column at the beginning (UUID primary key)
    columns = ["id"] + list(model_fields)

    return columns


def generate_insert_statement(plan: dict[str, Any], columns: list[str]) -> str:
    """Generate a single INSERT statement for a marketplace plan"""

    # Generate UUID for the id field
    values = ["gen_random_uuid()"]  # PostgreSQL function to generate UUID

    # Add values for each column (excluding id which we just added)
    for column in columns[1:]:  # Skip the id column
        value = plan.get(column)
        values.append(escape_sql_string(value))

    # Create the INSERT statement
    columns_str = ", ".join(columns)
    values_str = ", ".join(values)

    return f"INSERT INTO marketplace_plans ({columns_str}) VALUES ({values_str});"


def main():
    """Main function to generate seed.sql file"""

    # Define paths relative to script location
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    json_file = project_root / "src" / "data" / "marketplace_plans.json"
    output_file = project_root / "supabase" / "seed.sql"

    print(f"Reading data from: {json_file}")
    print(f"Output file: {output_file}")

    # Check if input file exists
    if not json_file.exists():
        print(f"Error: Input file {json_file} does not exist")
        return 1

    try:
        # Load and validate JSON data
        print("Loading JSON data...")
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        print(f"Loaded {len(data)} records")

        # Validate first record with Pydantic model
        if data:
            try:
                MarketplacePlanJSON(**data[0])
                print("✓ Data validation successful")
            except Exception as e:
                print(f"Warning: Data validation failed for first record: {e}")
                print("Continuing anyway...")

        # Get table columns
        columns = get_table_columns()
        print(f"Table columns ({len(columns)}): {', '.join(columns[:5])}...")

        # Generate SQL file
        print("Generating SQL INSERT statements...")

        with open(output_file, 'w', encoding='utf-8') as f:
            # Write header
            f.write("-- Seed data for marketplace_plans table\n")
            f.write(f"-- Generated from marketplace_plans.json with {len(data)} records\n")
            f.write(f"-- Generated on: {Path(__file__).name}\n\n")

            # Write TRUNCATE statement (optional, commented out by default)
            f.write("-- Uncomment the next line to clear existing data before inserting\n")
            f.write("-- TRUNCATE TABLE marketplace_plans RESTART IDENTITY CASCADE;\n\n")

            # Write INSERT statements
            f.write("-- Insert marketplace plans data\n")
            f.write("BEGIN;\n\n")

            for i, plan in enumerate(data):
                try:
                    insert_statement = generate_insert_statement(plan, columns)
                    f.write(insert_statement + "\n")

                    # Progress indicator
                    if (i + 1) % 1000 == 0:
                        print(f"  Processed {i + 1}/{len(data)} records...")

                except Exception as e:
                    print(f"Error processing record {i + 1}: {e}")
                    continue

            f.write("\nCOMMIT;\n")
            f.write(f"\n-- Total records inserted: {len(data)}\n")

        print(f"✓ Successfully generated {output_file}")
        print(f"  Total records: {len(data)}")

        # Show file size
        file_size = output_file.stat().st_size
        file_size_mb = file_size / (1024 * 1024)
        print(f"  File size: {file_size_mb:.2f} MB")

        return 0

    except FileNotFoundError:
        print(f"Error: File {json_file} not found")
        return 1
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {json_file}: {e}")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
