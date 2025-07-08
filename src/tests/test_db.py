#!/usr/bin/env python3
"""
Tests for the database utility module.

This module tests the Supabase connection manager and related functions in db.py,
including singleton behavior, client creation, error handling, and utility functions.
"""

import os
from unittest.mock import patch, Mock
import pytest

# Add the src directory to the path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import test functions but not the class - we'll import that within tests
from utils.db import (
    get_supabase_client,
    test_connection as db_test_connection,  # Renamed to avoid pytest confusion
    get_table
)


class TestSupabaseConnection:
    """Tests for the SupabaseConnection class."""

    @patch('utils.db.create_client')
    def test_singleton_pattern(self, mock_create_client: Mock) -> None:
        """Test that SupabaseConnection follows the singleton pattern."""
        # Import the class here to avoid global import
        from utils.db import SupabaseConnection

        # We'll use patch.object to avoid directly accessing protected attributes
        with patch.object(SupabaseConnection, '_instance', None), \
             patch.object(SupabaseConnection, '_client', None), \
             patch.dict(os.environ, {"SUPABASE_URL": "https://example.com", "SUPABASE_KEY": "test-key"}):

            # Mock client creation
            mock_client = Mock()
            mock_create_client.return_value = mock_client

            # Create two instances
            instance1 = SupabaseConnection()
            instance2 = SupabaseConnection()

            # Both should be the same object
            assert instance1 is instance2

    @patch('utils.db.create_client')
    def test_create_client_success(self, mock_create_client: Mock) -> None:
        """Test successful client creation with valid credentials."""
        # Import the class here to avoid global import
        from utils.db import SupabaseConnection

        # Setup mock
        mock_client = Mock()
        mock_create_client.return_value = mock_client

        # Test with valid environment variables
        with patch.object(SupabaseConnection, '_instance', None), \
             patch.object(SupabaseConnection, '_client', None), \
             patch.dict(os.environ, {"SUPABASE_URL": "https://example.com", "SUPABASE_KEY": "test-key"}):

            # Create a new connection
            connection = SupabaseConnection()
            client = connection.client

            # Verify the client was created with the correct parameters
            mock_create_client.assert_called_with("https://example.com", "test-key")
            assert client == mock_client

    def test_create_client_missing_env_vars(self) -> None:
        """Test error handling when environment variables are missing."""
        # Import the class here to avoid global import
        from utils.db import SupabaseConnection

        # Test with empty environment
        with patch.object(SupabaseConnection, '_instance', None), \
             patch.object(SupabaseConnection, '_client', None), \
             patch.object(SupabaseConnection, '__init__', return_value=None), \
             patch.dict(os.environ, {}, clear=True), \
             patch('utils.db.create_client', side_effect=Exception("This should not be called")):

            # Create instance without calling __init__
            connection = SupabaseConnection.__new__(SupabaseConnection)

            # Verify that accessing client raises an error
            with pytest.raises(ValueError) as excinfo:
                connection.client

            # Check the error message
            assert "Missing Supabase credentials" in str(excinfo.value)

    def test_create_client_missing_key(self) -> None:
        """Test error handling when SUPABASE_KEY is missing."""
        # Import the class here to avoid global import
        from utils.db import SupabaseConnection

        # Test with only URL in environment
        with patch.object(SupabaseConnection, '_instance', None), \
             patch.object(SupabaseConnection, '_client', None), \
             patch.object(SupabaseConnection, '__init__', return_value=None), \
             patch.dict(os.environ, {"SUPABASE_URL": "https://example.com"}, clear=True), \
             patch('utils.db.create_client', side_effect=Exception("This should not be called")):

            # Create instance without calling __init__
            connection = SupabaseConnection.__new__(SupabaseConnection)

            # Verify that accessing client raises an error
            with pytest.raises(ValueError) as excinfo:
                connection.client

            # Check the error message
            assert "Missing Supabase credentials" in str(excinfo.value)

    def test_create_client_missing_url(self) -> None:
        """Test error handling when SUPABASE_URL is missing."""
        # Import the class here to avoid global import
        from utils.db import SupabaseConnection

        # Test with only KEY in environment
        with patch.object(SupabaseConnection, '_instance', None), \
             patch.object(SupabaseConnection, '_client', None), \
             patch.object(SupabaseConnection, '__init__', return_value=None), \
             patch.dict(os.environ, {"SUPABASE_KEY": "test-key"}, clear=True), \
             patch('utils.db.create_client', side_effect=Exception("This should not be called")):

            # Create instance without calling __init__
            connection = SupabaseConnection.__new__(SupabaseConnection)

            # Verify that accessing client raises an error
            with pytest.raises(ValueError) as excinfo:
                connection.client

            # Check the error message
            assert "Missing Supabase credentials" in str(excinfo.value)


class TestClientFunctions:
    """Tests for the client access functions."""

    @patch('utils.db._supabase_connection')
    def test_get_supabase_client(self, mock_connection: Mock) -> None:
        """Test that get_supabase_client returns the client from the connection."""
        # Create a mock client
        mock_client = Mock()
        mock_connection.client = mock_client

        # Get the client using the function
        client = get_supabase_client()

        # Verify it returns the client from the connection
        assert client == mock_client

    @patch('utils.db.get_supabase_client')
    def test_test_connection_success(self, mock_get_client: Mock) -> None:
        """Test the test_connection function when connection is successful."""
        # Setup mock for successful connection
        mock_client = Mock()
        mock_rpc = Mock()

        mock_get_client.return_value = mock_client
        mock_client.rpc.return_value = mock_rpc
        mock_rpc.execute.return_value = True

        # Test the connection
        success = db_test_connection()

        # Verify the result and function calls
        assert success is True
        mock_client.rpc.assert_called_once_with('ping')
        mock_rpc.execute.assert_called_once()

    @patch('utils.db.get_supabase_client')
    def test_test_connection_failure(self, mock_get_client: Mock) -> None:
        """Test the test_connection function when connection fails."""
        # Setup mock for failed connection
        mock_client = Mock()
        mock_client.rpc.side_effect = Exception("Connection error")
        mock_get_client.return_value = mock_client

        # Test the connection
        result = db_test_connection()

        # Verify the result
        assert result is False

    @patch('utils.db.get_supabase_client')
    def test_get_table(self, mock_get_client: Mock) -> None:
        """Test the get_table utility function."""
        # Setup mock
        mock_client = Mock()
        mock_table = Mock()

        mock_get_client.return_value = mock_client
        mock_client.table.return_value = mock_table

        # Get a table
        result = get_table('test_table')

        # Verify the result and function calls
        assert result == mock_table
        mock_client.table.assert_called_once_with('test_table')


if __name__ == "__main__":
    pytest.main([__file__])
