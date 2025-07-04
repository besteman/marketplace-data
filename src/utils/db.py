import os
from typing import Optional
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class SupabaseConnection:
    """Supabase database connection manager."""

    _instance: Optional['SupabaseConnection'] = None
    _client: Optional[Client] = None

    def __new__(cls) -> 'SupabaseConnection':
        """Singleton pattern to ensure only one connection instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize the Supabase connection."""
        if self._client is None:
            self._client = self._create_client()

    def _create_client(self) -> Client:
        """Create and return a Supabase client."""
        url = os.getenv('SUPABASE_URL')
        key = os.getenv('SUPABASE_KEY')

        if not url or not key:
            raise ValueError(
                "Missing Supabase credentials. Please set SUPABASE_URL and SUPABASE_ANON_KEY "
                "environment variables in your .env file or system environment."
            )

        return create_client(url, key)

    @property
    def client(self) -> Client:
        """Get the Supabase client instance."""
        if self._client is None:
            self._client = self._create_client()
        return self._client

# Singleton instance
_supabase_connection = SupabaseConnection()

def get_supabase_client() -> Client:
    """
    Get a Supabase client instance.

    Returns:
        Client: Configured Supabase client instance

    Raises:
        ValueError: If Supabase credentials are not properly configured

    Example:
        >>> from src.utils.db import get_supabase_client
        >>> supabase = get_supabase_client()
        >>> result = supabase.table('your_table').select('*').execute()
    """
    return _supabase_connection.client

def test_connection() -> bool:
    """
    Test the Supabase connection.

    Returns:
        bool: True if connection is successful, False otherwise
    """
    try:
        client = get_supabase_client()
        # Try a simple query to test the connection
        client.rpc('ping').execute()
        return True
    except Exception as e:
        print(f"Connection test failed: {e}")
        return False

# Convenience function for direct table access
def get_table(table_name: str):
    """
    Get a table reference for direct querying.

    Args:
        table_name (str): Name of the table

    Returns:
        Table reference for chaining queries

    Example:
        >>> from src.utils.db import get_table
        >>> users = get_table('users').select('*').execute()
    """
    client = get_supabase_client()
    return client.table(table_name)
