import os
import duckdb
import sqlite3
import logging

def clean_up(file: str) -> None:
    # Remove the file if it exists
    if os.path.exists(file):
        os.remove(file)
    else:
        logging.warning(f"The file {file} does not exist.")


def create_tpch_data(db: str) -> None:
    conn = duckdb.connect(
        db
    ) # Define a .db file to persist the generated tpch data
    conn.sql(
        "INSTALL tpch;LOAD tpch; CALL dbgen(sf = 0.01);"
    ) # Generate a 100MB TPCH dataset
    conn.commit()
    conn.close() # Close connection, since duckdb only allows oe connection to tpch.db


def create_metadata_table(db: str) -> None:
    # Connect to SQLite database (or create it)
    conn = sqlite3.connect(db)
    # Create a cursor object
    cursor = conn.cursor()

    # Create the run_metadata table
    cursor.execute(
        """
        CREATE TABLE run_metadata (
            run_id TEXT PRIMARY KEY,
            metadata TEXT
        )
        """
    )

    # Commit the changes and close
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # Vars
    database = "tpch.db"
    metadata_db = "metadata.db"


    logging.info("Cleaning up tpch and metadata db files...")
    clean_up(database)
    clean_up(metadata_db)
    logging.info("Creating TPCH input data...")
    create_tpch_data(database)
    logging.info("Creating metadata table...")
    create_metadata_table(metadata_db)