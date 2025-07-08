#!/usr/bin/env python3
"""
Tests for upload_to_db.py script.

This module contains tests for the Supabase upload functions in upload_to_db.py,
testing data loading, validation, record preparation, and database uploads.
"""

import json
import os
import uuid
from unittest.mock import Mock, patch, mock_open

import pytest

# Add the src directory to the path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from scripts.upload_to_db import (
    load_json_data,
    validate_record,
    prepare_record_for_db,
    upload_records_to_supabase,
    main
)
from models.model import MarketplacePlanJSON


class TestLoadJsonData:
    """Test the load_json_data function."""

    def test_load_json_data_success(self) -> None:
        """Test loading JSON data successfully."""
        test_data = [{"state_code": "CA", "county_name": "Alameda"}]

        with patch('builtins.open', mock_open(read_data=json.dumps(test_data))):
            result = load_json_data("dummy/path.json")

        assert len(result) == 1
        assert result[0]["state_code"] == "CA"
        assert result[0]["county_name"] == "Alameda"

    def test_load_json_data_with_limit(self) -> None:
        """Test loading JSON data with a limit."""
        test_data = [
            {"state_code": "CA", "county_name": "Alameda"},
            {"state_code": "NY", "county_name": "Kings"}
        ]

        with patch('builtins.open', mock_open(read_data=json.dumps(test_data))):
            result = load_json_data("dummy/path.json", limit=1)

        assert len(result) == 1
        assert result[0]["state_code"] == "CA"

    def test_load_json_data_file_not_found(self) -> None:
        """Test handling of file not found error."""
        with patch('builtins.open', side_effect=FileNotFoundError()):
            result = load_json_data("nonexistent/file.json")

        assert result == []

    def test_load_json_data_invalid_json(self) -> None:
        """Test handling of invalid JSON format."""
        with patch('builtins.open', mock_open(read_data="invalid json")):
            with patch('json.load', side_effect=json.JSONDecodeError("Invalid JSON", "", 0)):
                result = load_json_data("dummy/path.json")

        assert result == []

    def test_load_json_data_general_exception(self) -> None:
        """Test handling of general exceptions."""
        with patch('builtins.open', side_effect=Exception("Test error")):
            result = load_json_data("dummy/path.json")

        assert result == []


class TestValidateRecord:
    """Test the validate_record function."""

    def test_validate_valid_record(self) -> None:
        """Test validating a valid record."""
        # Create a minimal valid record based on your model
        valid_record = {
            "state_code": "CA",
            "county_name": "Alameda"
        }

        # Patch the MarketplacePlanJSON to accept our minimal record
        with patch('scripts.upload_to_db.MarketplacePlanJSON') as mock_model:
            mock_instance = Mock()
            mock_model.return_value = mock_instance

            result = validate_record(valid_record)

        assert result is not None
        mock_model.assert_called_once_with(**valid_record)

    def test_validate_invalid_record(self) -> None:
        """Test validating an invalid record."""
        # Create a record for testing
        record = {
            "state_code": "CA",
            "county_name": "Alameda"
        }

        # Define a test exception class
        class TestValidationError(Exception):
            pass

        # Test with a ValidationError-like exception
        with patch('scripts.upload_to_db.ValidationError', TestValidationError), \
             patch('scripts.upload_to_db.MarketplacePlanJSON',
                  side_effect=TestValidationError("Validation failed")):
            result = validate_record(record)

        assert result is None

    def test_validate_general_exception(self) -> None:
        """Test handling of general exceptions during validation."""
        record = {"state_code": "CA"}

        with patch('scripts.upload_to_db.MarketplacePlanJSON',
                  side_effect=Exception("Test error")):
            result = validate_record(record)

        assert result is None


class TestPrepareRecordForDb:
    """Test the prepare_record_for_db function."""

    def test_prepare_record_for_db(self) -> None:
        """Test preparing a record for database insertion."""
        # Create a mock MarketplacePlanJSON instance
        mock_record = Mock(spec=MarketplacePlanJSON)
        mock_record.model_dump.return_value = {
            "state_code": "CA",
            "county_name": "Alameda",
            "premium_amount": None
        }

        # Patch uuid.uuid4 to return a consistent value for testing
        test_uuid = "12345678-1234-5678-1234-567812345678"
        with patch('uuid.uuid4', return_value=uuid.UUID(test_uuid)):
            result = prepare_record_for_db(mock_record)

        # Check the result has expected values
        assert result["id"] == test_uuid
        assert result["state_code"] == "CA"
        assert result["county_name"] == "Alameda"
        assert result["premium_amount"] is None


class TestUploadRecordsToSupabase:
    """Test the upload_records_to_supabase function."""

    @patch('scripts.upload_to_db.get_supabase_client')
    def test_upload_records_success(self, mock_get_client: Mock) -> None:
        """Test successful upload of records to Supabase."""
        # Setup test data
        test_records = [
            {"id": "uuid-1", "state_code": "CA", "county_name": "Alameda"},
            {"id": "uuid-2", "state_code": "NY", "county_name": "Kings"}
        ]

        # Mock Supabase client
        mock_client = Mock()
        mock_get_client.return_value = mock_client

        # Mock table.insert operation
        mock_table = Mock()
        mock_client.table.return_value = mock_table
        mock_table.insert.return_value = mock_table

        # Mock successful execution
        mock_execute_result = Mock()
        mock_execute_result.data = test_records
        mock_table.execute.return_value = mock_execute_result

        # Test the function
        result = upload_records_to_supabase(test_records, batch_size=2)

        # Verify the result
        assert result is True
        mock_client.table.assert_called_once_with('marketplace_plans')
        mock_table.insert.assert_called_once_with(test_records)
        mock_table.execute.assert_called_once()

    @patch('scripts.upload_to_db.get_supabase_client')
    def test_upload_records_no_data_response(self, mock_get_client: Mock) -> None:
        """Test upload with no data response from Supabase."""
        # Setup test data
        test_records = [
            {"id": "uuid-1", "state_code": "CA", "county_name": "Alameda"},
        ]

        # Mock Supabase client
        mock_client = Mock()
        mock_get_client.return_value = mock_client

        # Mock table.insert operation
        mock_table = Mock()
        mock_client.table.return_value = mock_table
        mock_table.insert.return_value = mock_table

        # Mock execution with no data
        mock_execute_result = Mock()
        mock_execute_result.data = None
        mock_table.execute.return_value = mock_execute_result

        # Test the function
        result = upload_records_to_supabase(test_records, batch_size=1)

        # Verify the result
        assert result is True  # Function should still return True

    @patch('scripts.upload_to_db.get_supabase_client')
    def test_upload_records_with_batching(self, mock_get_client: Mock) -> None:
        """Test uploading records in multiple batches."""
        # Setup test data with 5 records and batch size 2
        test_records = [
            {"id": f"uuid-{i}", "state_code": "CA"} for i in range(5)
        ]

        # Mock Supabase client
        mock_client = Mock()
        mock_get_client.return_value = mock_client

        # Mock table.insert operation
        mock_table = Mock()
        mock_client.table.return_value = mock_table
        mock_table.insert.return_value = mock_table

        # Mock successful execution
        mock_execute_result = Mock()
        mock_execute_result.data = [{"success": True}]
        mock_table.execute.return_value = mock_execute_result

        # Test the function with batch size 2
        result = upload_records_to_supabase(test_records, batch_size=2)

        # Verify the result
        assert result is True
        assert mock_client.table.call_count == 3  # Called for each batch
        assert mock_table.insert.call_count == 3  # 3 batches (2+2+1)
        assert mock_table.execute.call_count == 3

    @patch('scripts.upload_to_db.get_supabase_client')
    def test_upload_records_batch_error(self, mock_get_client: Mock) -> None:
        """Test handling of errors during batch upload."""
        # Setup test data
        test_records = [
            {"id": "uuid-1", "state_code": "CA"},
            {"id": "uuid-2", "state_code": "NY"}
        ]

        # Mock Supabase client
        mock_client = Mock()
        mock_get_client.return_value = mock_client

        # Mock table.insert operation
        mock_table = Mock()
        mock_client.table.return_value = mock_table
        mock_table.insert.return_value = mock_table

        # Mock execution with error
        mock_table.execute.side_effect = Exception("Upload error")

        # Test the function
        result = upload_records_to_supabase(test_records)

        # Verify the result
        assert result is False

    @patch('scripts.upload_to_db.get_supabase_client')
    def test_upload_records_with_long_string_fields(self, mock_get_client: Mock) -> None:
        """Test upload with records containing very long string fields."""
        # Setup test data with a long string field that will be flagged during error analysis
        test_records = [
            {
                "id": "uuid-1",
                "state_code": "CA",
                "very_long_field": "x" * 300  # Field with 300 characters
            }
        ]

        # Mock Supabase client
        mock_client = Mock()
        mock_get_client.return_value = mock_client

        # Mock table.insert operation
        mock_table = Mock()
        mock_client.table.return_value = mock_table
        mock_table.insert.return_value = mock_table

        # Mock execution with error to trigger the long string analysis
        mock_table.execute.side_effect = Exception("Upload error")

        # Test the function
        result = upload_records_to_supabase(test_records)

        # Verify the result
        assert result is False

    @patch('scripts.upload_to_db.get_supabase_client')
    def test_upload_records_client_error(self, mock_get_client: Mock) -> None:
        """Test handling of client initialization error."""
        mock_get_client.side_effect = Exception("Client error")

        result = upload_records_to_supabase([{"id": "test"}])

        assert result is False


class TestMainFunction:
    """Test the main function."""

    @patch('scripts.upload_to_db.prepare_record_for_db')
    @patch('scripts.upload_to_db.get_supabase_client')
    @patch('scripts.upload_to_db.load_json_data')
    @patch('scripts.upload_to_db.validate_record')
    def test_main_prepare_record_error(self,
                                    mock_validate: Mock,
                                    mock_load: Mock,
                                    mock_get_client: Mock,
                                    mock_prepare: Mock) -> None:
        """Test main function when there's an error preparing a record."""
        # Setup mock for successful DB connection
        mock_client = Mock()
        mock_get_client.return_value = mock_client

        mock_result = Mock()
        mock_result.data = [{"count": 0}]
        mock_client.table().select().execute.return_value = mock_result

        # Mock load_json_data to return test data
        test_data = [{"state_code": "CA"}]
        mock_load.return_value = test_data

        # Mock validate_record to return a validated record
        mock_validated_record = Mock()
        mock_validate.return_value = mock_validated_record

        # Mock prepare_record_for_db to raise an exception
        mock_prepare.side_effect = Exception("Error preparing record")

        # Run the main function
        main()

        # Verify prepare_record_for_db was called
        mock_prepare.assert_called_once_with(mock_validated_record)

    @patch('scripts.upload_to_db.get_supabase_client')
    @patch('scripts.upload_to_db.load_json_data')
    @patch('scripts.upload_to_db.validate_record')
    @patch('scripts.upload_to_db.prepare_record_for_db')
    @patch('scripts.upload_to_db.upload_records_to_supabase')
    def test_main_success_path(self,
                            mock_upload: Mock,
                            mock_prepare: Mock,
                            mock_validate: Mock,
                            mock_load: Mock,
                            mock_get_client: Mock) -> None:
        """Test the main function's happy path."""
        # Setup mocks for successful execution
        mock_client = Mock()
        mock_get_client.return_value = mock_client

        mock_result = Mock()
        mock_result.data = [{"count": 0}]
        mock_client.table().select().execute.return_value = mock_result

        # Mock load_json_data to return test data
        test_data = [{"state_code": "CA"}, {"state_code": "NY"}]
        mock_load.return_value = test_data

        # Mock validate_record to return a validated record
        mock_validated_record = Mock()
        mock_validate.return_value = mock_validated_record

        # Mock prepare_record_for_db to return a prepared record
        mock_prepared_record = {"id": "test-uuid", "state_code": "CA"}
        mock_prepare.return_value = mock_prepared_record

        # Mock upload_records_to_supabase to return success
        mock_upload.return_value = True

        # Run the main function
        main()

        # Verify the expected flow
        mock_get_client.assert_called_once()
        mock_load.assert_called_once()
        assert mock_validate.call_count == 2  # Called for each record
        assert mock_prepare.call_count == 2  # Called for each validated record
        mock_upload.assert_called_once()

    @patch('scripts.upload_to_db.get_supabase_client')
    def test_main_db_connection_failure(self, mock_get_client: Mock) -> None:
        """Test main function when database connection fails."""
        # Mock database connection failure
        mock_get_client.side_effect = Exception("Connection error")

        # Run the main function
        main()

        # No need for assertions as we're just testing it doesn't raise exceptions

    @patch('scripts.upload_to_db.get_supabase_client')
    @patch('scripts.upload_to_db.load_json_data')
    def test_main_no_json_data(self, mock_load: Mock, mock_get_client: Mock) -> None:
        """Test main function when no JSON data is loaded."""
        # Setup mock for successful DB connection
        mock_client = Mock()
        mock_get_client.return_value = mock_client

        mock_result = Mock()
        mock_result.data = [{"count": 0}]
        mock_client.table().select().execute.return_value = mock_result

        # Mock load_json_data to return empty list
        mock_load.return_value = []

        # Run the main function
        main()

        # Verify load_json_data was called but not other functions
        mock_load.assert_called_once()

    @patch('scripts.upload_to_db.get_supabase_client')
    @patch('scripts.upload_to_db.load_json_data')
    @patch('scripts.upload_to_db.validate_record')
    def test_main_validation_failure(self, mock_validate: Mock, mock_load: Mock, mock_get_client: Mock) -> None:
        """Test main function when all records fail validation."""
        # Setup mock for successful DB connection
        mock_client = Mock()
        mock_get_client.return_value = mock_client

        mock_result = Mock()
        mock_result.data = [{"count": 0}]
        mock_client.table().select().execute.return_value = mock_result

        # Mock load_json_data to return test data
        test_data = [{"state_code": "CA"}, {"state_code": "NY"}]
        mock_load.return_value = test_data

        # Mock validate_record to return None (validation failure)
        mock_validate.return_value = None

        # Run the main function
        main()

        # Verify validate_record was called but later functions weren't
        assert mock_validate.call_count == 2

    @patch('scripts.upload_to_db.get_supabase_client')
    @patch('scripts.upload_to_db.load_json_data')
    @patch('scripts.upload_to_db.validate_record')
    @patch('scripts.upload_to_db.prepare_record_for_db')
    @patch('scripts.upload_to_db.upload_records_to_supabase')
    def test_main_upload_failure(self,
                              mock_upload: Mock,
                              mock_prepare: Mock,
                              mock_validate: Mock,
                              mock_load: Mock,
                              mock_get_client: Mock) -> None:
        """Test main function when upload fails."""
        # Setup mock for successful DB connection
        mock_client = Mock()
        mock_get_client.return_value = mock_client

        mock_result = Mock()
        mock_result.data = [{"count": 0}]
        mock_client.table().select().execute.return_value = mock_result

        # Mock load_json_data to return test data
        test_data = [{"state_code": "CA"}]
        mock_load.return_value = test_data

        # Mock validate_record to return a validated record
        mock_validated_record = Mock()
        mock_validate.return_value = mock_validated_record

        # Mock prepare_record_for_db to return a prepared record
        mock_prepared_record = {"id": "test-uuid", "state_code": "CA"}
        mock_prepare.return_value = mock_prepared_record

        # Mock upload_records_to_supabase to return failure
        mock_upload.return_value = False

        # Run the main function
        main()

        # Verify the expected flow
        mock_upload.assert_called_once()


if __name__ == "__main__":
    pytest.main([__file__])
