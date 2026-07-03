import pandas as pd
import sqlite3

# Connect to the database we created
conn = sqlite3.connect("superstore.db")

# ── Query 1: Prove yesterday's finding ──────────
query1 = """
SELECT 
    Category,
    ROUND(SUM(Sales), 2) as Total_Sales,
    ROUND(SUM(Profit), 2) as Total_Profit,
    ROUND(AVG(Discount) * 100, 1) as Avg_Discount_Percent
FROM superstore
GROUP BY Category
ORDER BY Total_Profit DESC;
"""

result1 = pd.read_sql(query1, conn)
print("📊 Category Analysis:")
print(result1)
print()

# ── Query 2: Worst sub-categories by profit ─────
query2 = """
SELECT 
    Category,
    [Sub-Category],
    ROUND(SUM(Profit), 2) as Total_Profit,
    ROUND(AVG(Discount) * 100, 1) as Avg_Discount_Percent
FROM superstore
GROUP BY Category, [Sub-Category]
ORDER BY Total_Profit ASC
LIMIT 10;
"""

result2 = pd.read_sql(query2, conn)
print("❌ Most Loss-Making Sub-Categories:")
print(result2)
print()

# ── Query 3: Best sub-categories by profit ──────
query3 = """
SELECT 
    Category,
    [Sub-Category],
    ROUND(SUM(Profit), 2) as Total_Profit,
    ROUND(AVG(Discount) * 100, 1) as Avg_Discount_Percent
FROM superstore
GROUP BY Category, [Sub-Category]
ORDER BY Total_Profit DESC
LIMIT 10;
"""

result3 = pd.read_sql(query3, conn)
print("✅ Most Profitable Sub-Categories:")
print(result3)


# ── Query 4: Binders vs Tables deep dive ────────
query4 = """
SELECT 
    [Sub-Category],
    COUNT(*) as Total_Orders,
    ROUND(AVG(Sales), 2) as Avg_Sale_Amount,
    ROUND(AVG(Discount) * 100, 1) as Avg_Discount,
    ROUND(AVG(Profit), 2) as Avg_Profit_Per_Order,
    ROUND(SUM(Profit), 2) as Total_Profit
FROM superstore
WHERE [Sub-Category] IN ('Binders', 'Tables')
GROUP BY [Sub-Category];
"""

result4 = pd.read_sql(query4, conn)
print("🔍 Binders vs Tables:")
print(result4)
conn.close()