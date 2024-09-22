from .utils import create_dataset
import polars as pl

def generate_line_items() -> pl.DataFrame:
    df = create_dataset(table_name="lineitem")

    df.rename(lambda col_name: col_name[2:]).rename({"orderkey": "order_key"})
    return df