#!/usr/bin/env python3
"""
Upload marketplace plans JSON data to Supabase database.

This script:
1. Reads the marketplace_plans.json file
2. Validates each record using the MarketplacePlanJSON Pydantic model
3. Uploads records to the Supabase marketplace_plans table
4. Provides progress tracking and error handling
"""

import sys
import os
import json
from typing import List, Dict, Any, Optional
import uuid

# Add the src directory to the path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models.model import MarketplacePlanJSON
from utils.db import get_supabase_client
from pydantic import ValidationError


def load_json_data(file_path: str, limit: Optional[int] = None) -> List[Dict[str, Any]]:
    """Load JSON data from file with optional limit."""
    print(f"📖 Loading JSON data from {file_path}...")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if limit:
            data = data[:limit]
            print(f"✅ Loaded {len(data)} records (limited to {limit} for testing)")
        else:
            print(f"✅ Loaded {len(data)} records")

        return data

    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON format: {e}")
        return []
    except Exception as e:
        print(f"❌ Error loading JSON data: {e}")
        return []


def validate_record(record_data: Dict[str, Any]) -> Optional[MarketplacePlanJSON]:
    """Validate a single record using the Pydantic model."""
    try:
        return MarketplacePlanJSON(**record_data)
    except ValidationError as e:
        print(f"  ⚠️ Validation error: {e}")
        return None
    except Exception as e:
        print(f"  ⚠️ Unexpected error during validation: {e}")
        return None


def prepare_record_for_db(validated_record: MarketplacePlanJSON) -> Dict[str, Any]:
    """Prepare a validated record for database insertion."""
    # Convert the Pydantic model to a dictionary
    record_dict = validated_record.model_dump()

    # Add UUID for the id field
    record_dict['id'] = str(uuid.uuid4())

    # Handle None values - Supabase expects null, not None
    for key, value in record_dict.items():
        if value is None:
            record_dict[key] = None

    return record_dict


def upload_records_to_supabase(records: List[Dict[str, Any]], batch_size: int = 50, start_from_batch: int = 1) -> bool:
    """Upload records to Supabase in batches."""
    try:
        supabase = get_supabase_client()
        total_records = len(records)

        # Calculate starting position
        start_index = (start_from_batch - 1) * batch_size
        if start_index >= total_records:
            print(f"⚠️ Start batch {start_from_batch} is beyond available records. No upload needed.")
            return True

        remaining_records = total_records - start_index
        print(f"🚀 Resuming upload from batch {start_from_batch} ({remaining_records} remaining records in batches of {batch_size})...")

        # Upload in batches starting from the specified position
        for i in range(start_index, total_records, batch_size):
            batch = records[i:i + batch_size]
            batch_num = (i // batch_size) + 1
            total_batches = (total_records + batch_size - 1) // batch_size

            print(f"  📦 Uploading batch {batch_num}/{total_batches} ({len(batch)} records)...")

            try:
                result = supabase.table('marketplace_plans').insert(batch).execute()  # type: ignore

                if result.data:
                    print(f"    ✅ Batch {batch_num} uploaded successfully ({len(result.data)} records)")
                else:
                    print(f"    ⚠️ Batch {batch_num} upload returned no data")

            except Exception as e:
                print(f"    ❌ Error uploading batch {batch_num}: {e}")

                # Show details of the problematic batch for debugging
                print(f"    🔍 Analyzing batch {batch_num} for issues...")
                for j, record in enumerate(batch):
                    for field, value in record.items():
                        if isinstance(value, str) and len(value) > 200:
                            print(f"      Record {j+1}, field '{field}': {len(value)} chars (truncated: {value[:100]}...)")

                return False

        print(f"🎉 Successfully uploaded all remaining records!")
        return True

    except Exception as e:
        print(f"❌ Error during upload: {e}")
        return False


def main():
    """Main function to orchestrate the upload process."""
    print("🚀 Starting marketplace plans data upload to Supabase...")

    # Configuration
    json_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'marketplace_plans.json')
    test_limit = None  # Full upload - all records
    batch_size = 100   # Increased batch size for better performance
    start_from_batch = 74  # Resume from batch 74 (around where we failed)

    # Step 1: Test database connection
    print("🔗 Testing database connection...")
    try:
        supabase = get_supabase_client()
        result = supabase.table('marketplace_plans').select('count').execute()
        current_count = len(result.data) if result.data else 0
        print(f"✅ Database connection successful! Current records in table: {current_count}")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("Please check your Supabase credentials and ensure the service is running.")
        return

    # Step 2: Load JSON data
    json_data = load_json_data(json_file_path, limit=test_limit)
    if not json_data:
        print("❌ No JSON data loaded. Exiting.")
        return

    # Step 3: Validate records
    print("🔍 Validating records...")
    validated_records: List[MarketplacePlanJSON] = []
    validation_errors = 0

    for i, record_data in enumerate(json_data):
        validated_record = validate_record(record_data)
        if validated_record:
            validated_records.append(validated_record)
        else:
            validation_errors += 1
            if validation_errors <= 5:  # Show first 5 errors
                print(f"  ❌ Record {i + 1} failed validation")

    print(f"✅ Validated {len(validated_records)} records ({validation_errors} validation errors)")

    if not validated_records:
        print("❌ No valid records to upload. Exiting.")
        return

    # Step 4: Prepare records for database
    print("🔧 Preparing records for database...")
    db_records: List[Dict[str, Any]] = []

    for validated_record in validated_records:
        try:
            db_record = prepare_record_for_db(validated_record)
            db_records.append(db_record)
        except Exception as e:
            print(f"  ⚠️ Error preparing record: {e}")
            continue

    print(f"✅ Prepared {len(db_records)} records for upload")

    # Step 5: Show sample record
    if db_records:
        print("\n📋 Sample record to be uploaded:")
        sample_record = db_records[0]
        for key, value in list(sample_record.items())[:10]:  # Show first 10 fields
            print(f"  {key}: {value}")
        print("  ...")

    # Step 6: Upload to Supabase
    success = upload_records_to_supabase(db_records, batch_size, start_from_batch)

    if success:
        print(f"\n🎉 Upload completed successfully!")
        print(f"📊 Summary:")
        print(f"   • Total records loaded: {len(json_data)}")
        print(f"   • Successfully validated: {len(validated_records)}")
        print(f"   • Successfully uploaded: {len(db_records)}")
        print(f"   • Validation errors: {validation_errors}")
        print(f"   • Started from batch: {start_from_batch}")
    else:
        print(f"\n❌ Upload failed. Please check the error messages above.")


if __name__ == "__main__":
    main()
