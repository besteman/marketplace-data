#!/usr/bin/env python3
"""
Convert CSV marketplace plans data to JSON format with transformations.

This script:
1. Reads the marketplace_plans.csv file using the MarketplacePlanCSV Pydantic model
2. Converts column names to lowercase snake_case
3. Preserves numeric values as numbers
4. Converts monetary values (with $) to decimals
5. Outputs clean JSON data
"""

import sys
import os
import json
import csv
import re
from typing import List, Dict, Any, Union
from datetime import datetime

# Add the src directory to the path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models.model import MarketplacePlanCSV


def convert_to_snake_case(name: str) -> str:
    """Convert a string to lowercase snake_case."""
    # Handle special cases and clean up the name first
    name = name.strip()

    # Replace common patterns
    name = re.sub(r'[+]', '_plus_', name)  # Handle "Couple+1 child" -> "Couple_plus_1 child"
    name = re.sub(r'[,]+', '_', name)      # Replace commas with underscores
    name = re.sub(r'[\s]+', '_', name)     # Replace spaces with underscores
    name = re.sub(r'[-]+', '_', name)      # Replace hyphens with underscores
    name = re.sub(r'[()]+', '', name)      # Remove parentheses
    name = re.sub(r'[%]+', '_percent', name)  # Replace % with _percent

    # Convert to snake_case
    # Insert underscore before uppercase letters that follow lowercase letters
    name = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name)

    # Convert to lowercase
    name = name.lower()

    # Clean up multiple underscores
    name = re.sub(r'_+', '_', name)

    # Remove leading/trailing underscores
    name = name.strip('_')

    # If the name starts with a number, prefix with 'col_'
    if name and name[0].isdigit():
        name = f"col_{name}"

    return name


def parse_value(value: str) -> Union[str, int, float, None]:
    """Parse a value and convert it to appropriate type."""
    if not value or value.strip() == '':
        return None

    value = value.strip()

    # Handle monetary values (contains $)
    if '$' in value:
        # Remove $ and commas, then convert to decimal
        cleaned_value = value.replace('$', '').replace(',', '')
        try:
            return float(cleaned_value)
        except ValueError:
            return value  # Return original if conversion fails

    # Handle percentage values
    if value.endswith('%'):
        # Keep as string for now, but could convert to decimal if needed
        return value

    # Try to convert to number
    try:
        # Try integer first
        if '.' not in value and ',' not in value:
            return int(value)
        else:
            # Remove commas and try float
            cleaned_value = value.replace(',', '')
            return float(cleaned_value)
    except ValueError:
        # Return as string if not a number
        return value


def transform_csv_record(csv_record: MarketplacePlanCSV) -> Dict[str, Any]:
    """Transform a CSV record to JSON format with snake_case keys and proper types."""
    # Get the original data as a dictionary using the aliases
    original_data = csv_record.model_dump(by_alias=True)

    transformed_data: Dict[str, Any] = {}

    for original_key, value in original_data.items():
        # Convert key to snake_case
        snake_case_key = convert_to_snake_case(original_key)

        # Parse and convert the value
        parsed_value = parse_value(value) if value is not None else None

        transformed_data[snake_case_key] = parsed_value

    return transformed_data


def load_csv_data(file_path: str) -> List[MarketplacePlanCSV]:
    """Load CSV data and validate using Pydantic model."""
    print(f"📖 Loading CSV data from {file_path}...")

    records: List[MarketplacePlanCSV] = []
    validation_errors = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)

            for row_num, row in enumerate(csv_reader, start=2):  # Start at 2 since row 1 is headers
                try:
                    # Create MarketplacePlanCSV instance
                    record = MarketplacePlanCSV(**row)
                    records.append(record)
                except Exception as e:
                    validation_errors += 1
                    if validation_errors <= 5:  # Show first 5 errors
                        print(f"  ⚠️ Validation error in row {row_num}: {e}")

        print(f"✅ Successfully loaded {len(records)} records ({validation_errors} validation errors)")
        return records

    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return []
    except Exception as e:
        print(f"❌ Error loading CSV data: {e}")
        return []


def save_json_data(data: List[Dict[str, Any]], output_path: str) -> bool:
    """Save transformed data to JSON file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)

        print(f"💾 JSON data saved to: {output_path}")
        return True
    except Exception as e:
        print(f"❌ Error saving JSON file: {e}")
        return False


def generate_transformation_report(sample_data: List[Dict[str, Any]], output_path: str) -> bool:
    """Generate a report showing the transformations applied."""
    try:
        if not sample_data:
            return False

        # Get a sample record to show transformations
        sample_record = sample_data[0]

        report: Dict[str, Any] = {
            "transformation_info": {
                "description": "CSV to JSON transformation with snake_case keys and type conversion",
                "generated_at": datetime.now().isoformat(),
                "total_records": len(sample_data),
                "transformations_applied": [
                    "Column names converted to lowercase snake_case",
                    "Column names starting with numbers prefixed with 'col_'",
                    "Monetary values (with $) converted to decimal numbers",
                    "Numeric values preserved as numbers",
                    "Empty/null values set to null",
                    "Percentage values kept as strings"
                ]
            },
            "sample_transformations": {},
            "field_types": {}
        }

        # Show some example transformations
        original_fields = [
            "State Code", "FIPS County Code", "County Name", "Premium Child Age 0-14",
            "Couple+1 child, Age 21", "Medical Deductible - Individual - Standard",
            "EHB Percent of Total Premium"
        ]

        for original_field in original_fields:
            snake_case_field = convert_to_snake_case(original_field)
            if snake_case_field in sample_record:
                report["sample_transformations"][original_field] = {
                    "snake_case_name": snake_case_field,
                    "sample_value": sample_record[snake_case_field],
                    "value_type": type(sample_record[snake_case_field]).__name__
                }

        # Analyze field types
        for field_name, value in sample_record.items():
            value_type = type(value).__name__
            report["field_types"][field_name] = value_type

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)

        print(f"💾 Transformation report saved to: {output_path}")
        return True

    except Exception as e:
        print(f"❌ Error generating transformation report: {e}")
        return False


def main():
    """Main function to orchestrate the CSV to JSON conversion."""
    print("🚀 Starting CSV to JSON conversion with transformations...")

    # Configuration
    csv_file_path = "/Users/besteman/code/marketplace-data/src/data/marketplace_plans.csv"
    output_dir = "/Users/besteman/code/marketplace-data/src/data"

    # Output file paths
    json_output_path = os.path.join(output_dir, "marketplace_plans.json")
    report_output_path = os.path.join(output_dir, "transformation_report.json")

    # Step 1: Load and validate CSV data
    csv_records = load_csv_data(csv_file_path)
    if not csv_records:
        print("❌ No CSV data loaded. Exiting.")
        return

    # Step 2: Transform records
    print("🔄 Transforming records...")
    transformed_records: List[Dict[str, Any]] = []

    for i, record in enumerate(csv_records):
        try:
            transformed_record = transform_csv_record(record)
            transformed_records.append(transformed_record)

            # Show progress for large datasets
            if (i + 1) % 10000 == 0:
                print(f"  Processed {i + 1:,} records...")
        except Exception as e:
            print(f"  ⚠️ Error transforming record {i + 1}: {e}")
            continue

    print(f"✅ Successfully transformed {len(transformed_records)} records")

    # Step 3: Show sample of transformations
    if transformed_records:
        print("\n📋 Sample transformations:")
        sample_record = transformed_records[0]
        for key, value in list(sample_record.items())[:10]:  # Show first 10 fields
            value_type = type(value).__name__
            print(f"  {key}: {value} ({value_type})")
        print("  ...")

    # Step 4: Save JSON data
    if not save_json_data(transformed_records, json_output_path):
        print("❌ Failed to save JSON file. Exiting.")
        return

    # Step 5: Generate transformation report
    generate_transformation_report(transformed_records, report_output_path)

    print(f"\n🎉 Conversion completed successfully!")
    print(f"📁 Generated files:")
    print(f"   • JSON Data: {json_output_path}")
    print(f"   • Transformation Report: {report_output_path}")
    print(f"\n📊 Summary:")
    print(f"   • Total records processed: {len(csv_records)}")
    print(f"   • Successfully transformed: {len(transformed_records)}")
    print(f"   • Output format: JSON with snake_case keys and proper types")


if __name__ == "__main__":
    main()
