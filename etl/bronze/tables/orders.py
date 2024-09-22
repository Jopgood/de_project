from .utils import create_dataset
import polars as pl

def generate_orders() -> pl.DataFrame:
    df = create_dataset(table_name="orders")

    df.rename(lambda col_name: col_name[2:]).rename({"orderkey": "order_key", "custkey": "customer_key"})
    return df