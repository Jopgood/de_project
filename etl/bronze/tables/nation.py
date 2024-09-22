from .utils import create_dataset
import polars as pl

def generate_nations() -> pl.DataFrame:
    df = create_dataset(table_name="nation")

    df.rename(lambda col_name: col_name[2:])
    return df