This is a codebase to read in CSV files, infer PostgreSQL types, and create a table in a PostgreSQL database. It includes functions to parse CSV rows into models, load CSV files as models, and infer PostgreSQL types based on sample values. The code also handles specific cases for column names and types, ensuring compatibility with PostgreSQL's requirements.

Codebase is using Pydantic for data validation and type annotations, and it includes a script to create the necessary database table. The code is designed to be run in a Python environment with access to a PostgreSQL database.

Codebase is using Supabase for database operations, and it includes a `.env` file for configuration. The code is structured to allow easy extension and modification, with clear separation of concerns between data models, database operations, and CSV parsing logic.

Codebase is using uv package manager for dependency management. Use this for installing dependencies and running the code. Use it to run pytest.

Codebase is using pytest for testing. Use pytest to run the tests and ensure the code is functioning as expected. All tests are located in the `srctests` directory, and they cover various aspects of the codebase, including CSV parsing, model validation, and database operations.
