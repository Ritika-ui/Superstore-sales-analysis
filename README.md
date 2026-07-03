# Superstore-sales-analysis
End-to-end data analysis project using SQL, Python, and Power BI.

# 🛒 Superstore Sales Analysis

End-to-end data analysis project uncovering profit drivers 
and loss-making products in a retail superstore dataset.
Built with SQL, Python, and Power BI.

---

## 📌 Business Problem

A retail superstore has $2.30M in sales but only 12.47% 
profit margin. This analysis identifies WHY profit is low 
and provides specific recommendations to improve it.

---

## 🔍 Key Insights Discovered

### 1. Technology is the most profitable category
- Technology generates $145K profit despite not having 
  the highest sales
- Furniture has the lowest profit ($18K) despite high 
  sales volume due to aggressive discounting (17% avg)

### 2. Tables are losing $55.57 per sale
- Tables sub-category has -$17,725 total loss
- Root cause: 26.1% average discount on high-value items 
  ($648 avg sale price)
- Every single Table sale loses money

### 3. Central region underperforms due to high discounts
- Central region: 24% avg discount vs West region: 10.9%
- West generates $108K profit vs Central's $39K
- Same discount reduction strategy could unlock ~$70K 
  additional profit

### 4. Home Office is the most valuable customer segment
- Home Office: $407 profit per customer
- Consumer: $327 profit per customer  
- Despite fewest customers, Home Office generates 
  most value per acquisition

### 5. 5 products responsible for $22,120 in losses
- Cubify CubeX 3D Printer: -$8,879
- Lexmark MX611dhe Printer: -$4,589
- Chromcraft Conference Table: -$2,876
- Repricing or discontinuing these products could 
  recover significant losses

---

## 💡 Business Recommendations

1. **Reduce Table discounts** below 15% immediately
   → Could recover $17,725 in lost profit
2. **Investigate Central region** discount policy
   → 24% avg discount is unsustainable
3. **Prioritize Home Office** customer acquisition
   → 24% more profitable per customer than Consumer
4. **Review bottom 5 products**
   → $22,120 combined loss from just 5 SKUs
5. **Push Technology products** more aggressively
   → Highest profit margin, lowest discount rate

---

## 📊 Dashboard

### Page 1 — Executive Summary
<img width="1091" height="623" alt="image" src="https://github.com/user-attachments/assets/810df71b-4537-41bb-8e4f-a0e2fe6b8558" />


### Page 2 — Detailed Analysis
<img width="1090" height="612" alt="image" src="https://github.com/user-attachments/assets/7a746241-b329-4085-849c-d5e4dd1468bd" />


### Page 3 — Sales Trend
<img width="1268" height="752" alt="image" src="https://github.com/user-attachments/assets/4e5a2a46-8b7b-47e0-9afc-a11f038a52b8" />


### Page 4 — Discount Analysis
<img width="1286" height="767" alt="image" src="https://github.com/user-attachments/assets/3a7c16d5-992b-488d-a0d6-7d869e82ef6a" />


### Page 5 — Product Analysis
<img width="857" height="202" alt="image" src="https://github.com/user-attachments/assets/c94a559b-95e6-461e-9fdc-84031c0a5312" />


---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| **SQL (SQLite)** | Data querying and aggregation |
| **Python (Pandas)** | Data loading and manipulation |
| **Matplotlib** | Python visualizations |
| **Power BI** | Interactive dashboard |
| **Excel** | Initial data exploration |

---

## 📁 Project Structure
superstore-sales-analysis/

├── screenshots/ # Dashboard screenshots
├── data/        # Raw dataset
├── scripts/     # SQL + Python analysis files
├── dashboard/   # Power BI .pbix file
└── README.md

## 🔧 How to Run

```bash
# Install dependencies
pip install pandas matplotlib openpyxl

# Run analysis
python scripts/day2.py
python scripts/day3.py

# Open dashboard
# Open dashboard/superstore-sales-analysis.pbix in Power BI Desktop
```

---

## 📈 Dataset

- **Source:** Kaggle — Superstore Sales Dataset
- **Rows:** 9,994 transactions
- **Period:** 2014 — 2017
- **Fields:** Orders, customers, products, sales, profit, discount

---

## 👩‍💻 Author

**Ritika Khadka**
