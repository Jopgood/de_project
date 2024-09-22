# simple query to get the output dataset
import duckdb

conn = duckdb.connect("tpch.db")

conn.sql("""
WITH order_items AS (
    SELECT
        l_orderkey,
        COUNT(*) AS item_count
    FROM
        lineitem
    GROUP BY
        l_orderkey
),
customer_orders AS (
    SELECT
        o.o_custkey,
        o.o_orderkey,
        o.o_totalprice,
        oi.item_count
    FROM
        orders o
    JOIN
        order_items oi ON o.o_orderkey = oi.l_orderkey
)
SELECT
    c.c_custkey AS customer_key,
    c.c_name AS customer_name,
    MIN(co.o_totalprice) AS min_order_value,
    MAX(co.o_totalprice) AS max_order_value,
    AVG(co.o_totalprice) AS avg_order_value,
    AVG(co.item_count) AS avg_num_items_per_order
FROM
    customer c
JOIN
    customer_orders co ON c.c_custkey = co.o_custkey
GROUP BY
    c.c_custkey, c.c_name;
""").show()

conn.commit()
conn.close() # close the connection