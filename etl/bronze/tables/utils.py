# Defining dataset creation helper functions
import duckdb
import polars as pl

def create_dataset(
        table_name: str, 
        source_database: str ="tpch.db") -> pl.DataFrame:
    conn = duckdb.connect(source_database)
    pulled_df = conn.sql(f"SELECT * FROM {table_name}").pl()
    conn.close()
    return pulled_df
