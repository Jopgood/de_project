# read customer, order, and lineitem dataset from duckdb into Polars dataframe
from tables import generate_customers, generate_line_items, generate_nations, generate_orders, generate_regions
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# remove c_ and then rename custkey to customer_key
cleaned_customer_df = generate_customers()
logging.info("CUSTOMER TABLE")
print(cleaned_customer_df)

# Remove the o_ and l_ from the order and lineitem table's column names
# We also rename customer key and order key
cleaned_orders_df = generate_orders()
logging.info("ORDERS TABLE")
print(cleaned_orders_df)

cleaned_lineitem_df = generate_line_items()
logging.info("LINEITEM TABLE")
print(cleaned_lineitem_df)

# remove the n_ and r_ from the nation and region table's column names
cleaned_nation_df = generate_nations()
logging.info("NATION TABLE")
print(cleaned_nation_df)

cleaned_region_df = generate_regions()
logging.info("REGION TABLE")
print(cleaned_region_df)