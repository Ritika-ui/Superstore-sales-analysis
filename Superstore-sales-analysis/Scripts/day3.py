import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("superstore.db")

# ── Chart 1: Profit by Category ──────────────────
query_cat = """
SELECT Category, ROUND(SUM(Profit), 2) as Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Profit DESC;
"""
cat = pd.read_sql(query_cat, conn)

plt.figure(figsize=(8, 5))
colors = ['green' if x > 0 else 'red' for x in cat['Total_Profit']]
plt.bar(cat['Category'], cat['Total_Profit'], color=colors)
plt.title('Total Profit by Category', fontsize=14)
plt.xlabel('Category')
plt.ylabel('Profit ($)')
plt.tight_layout()
plt.savefig('chart1_category_profit.png')
plt.show()
print("✅ Chart 1 saved!")

# ── Chart 2: Profit by Region ────────────────────
query_reg = """
SELECT Region, ROUND(SUM(Profit), 2) as Total_Profit
FROM superstore
GROUP BY Region
ORDER BY Total_Profit DESC;
"""
reg = pd.read_sql(query_reg, conn)

plt.figure(figsize=(8, 5))
plt.bar(reg['Region'], reg['Total_Profit'], color='steelblue')
plt.title('Total Profit by Region', fontsize=14)
plt.xlabel('Region')
plt.ylabel('Profit ($)')
plt.tight_layout()
plt.savefig('chart2_region_profit.png')
plt.show()
print("✅ Chart 2 saved!")

# ── Chart 3: Profit per Customer by Segment ──────
segment_data = {
    'Segment': ['Consumer', 'Corporate', 'Home Office'],
    'Profit_Per_Customer': [327, 389, 407]
}
seg = pd.DataFrame(segment_data)

plt.figure(figsize=(8, 5))
plt.bar(seg['Segment'], seg['Profit_Per_Customer'],
        color=['#ff9999', '#66b3ff', '#99ff99'])
plt.title('Profit Per Customer by Segment', fontsize=14)
plt.xlabel('Segment')
plt.ylabel('Profit per Customer ($)')
plt.tight_layout()
plt.savefig('chart3_segment_profit.png')
plt.show()
print("✅ Chart 3 saved!")

conn.close()