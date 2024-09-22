from .utils import create_dataset
import polars as pl

def generate_customers() -> pl.DataFrame:
    df = create_dataset(table_name="customer")

    df.rename(lambda col_name: col_name[2:]).rename({"custkey": "customer_key"})
    return df