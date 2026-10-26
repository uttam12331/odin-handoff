# Odin Task veiw1b03 – Q3 Returns Analysis
Apps: **DBeaver · Visual Studio Code · Google Sheets (in Brave)**
Target length: **25–30 min** (allowed 15:00–45:59)

> Keep this file on your PHONE or PAPER while recording – never on the Mac screen.
> Learn the flow, then narrate in your own words. Do NOT read it word-for-word.

---

## PART 1 – In Studio (main Mac user), before recording

1. Start the Insightful timer → minimize.
2. Open task **veiw1b03** (In Progress).
3. Copy the **Goal** text exactly as it is in Prompt/Description. This exact text goes into:
   - the opening Google Doc
   - TaskRecorder → Task Description
   - Metadata.rtf → Request
4. Download the **Metadata.rtf template** from the task (Task files section) and fill it in (Part 7 below). Save it in Documents of the main user. Never open it in rec.mac.
5. Fill the pre-recording fields:
   - **Professional Domain:** Data Science & Analytics
   - **Mac spec:** Apple menu → About This Mac (Chip, Memory) · System Information → Graphics/Displays (GPU) · System Settings → General → Storage (available)
   - **Resolution / Light-Dark / Dock position (Left or Right) / Wallpaper changed** – enter what you will actually use in rec.mac
   - **Apps:** DBeaver, Visual Studio Code, Google Sheets
   - **Inputs:** sales.db – "AI-generated before recording"
6. Read the "Before you record" criteria list in the task.

---

## PART 2 – Setup in rec.mac (once)

1. Install: **DBeaver Community** (dbeaver.io), **VS Code** (code.visualstudio.com), **Python 3** (python.org).
2. VS Code → Extensions → install **Python** and **Jupyter** (Microsoft). Uninstall **GitHub Copilot / Copilot Chat** if present. Settings → search `chat` → turn off chat/Copilot.
3. VS Code → Terminal → New Terminal:
   ```
   pip3 install pandas matplotlib ipykernel
   mkdir -p ~/Desktop/ReturnsAnalysis
   ```
4. Brave → sign in to Google with the **OTA** account (for Sheets + opening doc).

### Make sales.db with Gemini (before recording)
Brave → gemini.google.com (OTA) → paste:

```
Write a Python script that creates a SQLite database file named sales.db in the same folder as the script, using only the Python standard library (sqlite3, random, datetime, os). Use random.seed(42). If sales.db already exists, delete it first. Create 4 tables:

1. customers (customer_id INTEGER PRIMARY KEY, region TEXT) – 400 customers, regions: North, South, East, West.
2. products (product_id INTEGER PRIMARY KEY, product_name TEXT, category TEXT, unit_price REAL) – 30 fictional products, 6 in each category: Electronics, Apparel, Home, Sports, Beauty.
3. orders (order_id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, order_date TEXT in YYYY-MM-DD format, quantity INTEGER) – about 6000 orders spread evenly from 2025-01-01 to 2025-09-30.
4. returns (return_id INTEGER PRIMARY KEY, order_id INTEGER, return_date TEXT in YYYY-MM-DD format, reason TEXT) – reasons: Defective, Wrong size, Not as described, Changed mind. return_date is 3 to 20 days after order_date.

Base return rate about 6 percent with mixed reasons. Hidden pattern: for orders from July to September 2025, Electronics in the West region has a return rate of about 18 percent, mostly reason Defective, and Apparel in the South region has a return rate of about 11 percent, mostly reason Wrong size. Add data issues to clean: 15 orders with NULL quantity and 10 exact duplicate rows in returns (same order_id, return_date and reason, new return_id). Use fictional data only, no real names or personal information. At the end, print the row count of each table. Give only the complete script.
```

- Save Gemini's script as `~/Desktop/ReturnsAnalysis/make_db.py`, then in the terminal:
  ```
  cd ~/Desktop/ReturnsAnalysis && python3 make_db.py
  ```
- Move `make_db.py` to Documents. The folder must contain **only sales.db**.
- Close Gemini.
- DBeaver: Database → New Database Connection → SQLite → Path: sales.db → Finish (Download driver if asked). Check tables have rows.

### Practise once (not recorded)
Do the whole Part 5 flow once so you know every step. Then **delete** everything except sales.db from the ReturnsAnalysis folder, delete the practice notebook/CSVs/PNG, delete the practice Google Sheet, and empty Downloads of practice files.
Note your real numbers during practice (top category-region, rates, z-scores) so your narration makes sense.

---

## PART 3 – Code to practise

### DBeaver – Query 1 (data-quality check)
```sql
SELECT
  (SELECT COUNT(*) FROM orders) AS total_orders,
  (SELECT COUNT(*) FROM orders WHERE quantity IS NULL) AS null_quantity,
  (SELECT COUNT(*) FROM returns) AS return_rows,
  (SELECT COUNT(DISTINCT order_id) FROM returns) AS returned_orders;
```
Meaning: return_rows > returned_orders → duplicate return rows exist, so we count DISTINCT order_id.

### DBeaver – Query 2 (monthly return rate, export → returns_by_month.csv)
```sql
SELECT strftime('%Y-%m', o.order_date) AS month,
       p.category,
       c.region,
       COUNT(DISTINCT o.order_id) AS orders,
       COUNT(DISTINCT r.order_id) AS returned_orders
FROM orders o
JOIN products p ON p.product_id = o.product_id
JOIN customers c ON c.customer_id = o.customer_id
LEFT JOIN returns r ON r.order_id = o.order_id
GROUP BY month, p.category, c.region
ORDER BY month, p.category, c.region;
```

### DBeaver – Query 3 (Q3 return reasons, export → reasons_q3.csv)
```sql
SELECT p.category, c.region, r.reason,
       COUNT(DISTINCT r.order_id) AS returns_q3
FROM returns r
JOIN orders o ON o.order_id = r.order_id
JOIN products p ON p.product_id = o.product_id
JOIN customers c ON c.customer_id = o.customer_id
WHERE o.order_date BETWEEN '2025-07-01' AND '2025-09-30'
GROUP BY p.category, c.region, r.reason
ORDER BY returns_q3 DESC;
```

### VS Code notebook – returns_analysis.ipynb (one block = one cell)

Cell 1 – load
```python
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("returns_by_month.csv")
df.head()
```

Cell 2 – inspect
```python
df.info()
df.isna().sum()
```

Cell 3 – clean + totals check
```python
df = df.drop_duplicates()
df["month"] = pd.to_datetime(df["month"])
df["return_rate"] = df["returned_orders"] / df["orders"]
print(df["orders"].sum(), df["returned_orders"].sum())
```
→ these two numbers must equal **total_orders** and **returned_orders** from DBeaver Query 1.

Cell 4 – Q2 vs Q3 by category-region
```python
df["quarter"] = df["month"].dt.quarter
q = df[df["quarter"].isin([2, 3])]
q = q.groupby(["category", "region", "quarter"])[["orders", "returned_orders"]].sum()
q["rate"] = q["returned_orders"] / q["orders"]
pivot = q["rate"].unstack("quarter")
pivot.columns = ["q2_rate", "q3_rate"]
pivot["change"] = pivot["q3_rate"] - pivot["q2_rate"]
pivot.head()
```

Cell 5 – z-score + top 5
```python
pivot["z"] = (pivot["change"] - pivot["change"].mean()) / pivot["change"].std()
pivot["flag"] = pivot["z"] > 1.5
top5 = pivot.sort_values("z", ascending=False).head(5).round(3)
top5
```

Cell 6 – trend chart
```python
m = df.groupby(["month", "category"])[["orders", "returned_orders"]].sum()
m["rate"] = m["returned_orders"] / m["orders"]
m["rate"].unstack().plot(marker="o", figsize=(9, 5), title="Monthly return rate by category")
plt.ylabel("Return rate")
plt.savefig("return_trend.png", dpi=150, bbox_inches="tight")
```

Cell 7 – export
```python
top5.to_csv("top5_outliers.csv")
```

---

## PART 4 – Just before recording (rec.mac)

- [ ] Mac on power, enough storage
- [ ] Clock with seconds, Dock left/right (not hidden), **new wallpaper** (different from practice), notifications off
- [ ] Accessibility Inspector running (dot in Dock, window closed)
- [ ] Insightful timer running, minimized
- [ ] ReturnsAnalysis folder contains **only sales.db**
- [ ] **DBeaver** open, sales.db connection expanded, no old scripts open → minimize
- [ ] **VS Code** open with folder ReturnsAnalysis (File → Open Folder) → minimize
- [ ] **Brave** open at sheets.google.com (OTA), only that tab → minimize
- [ ] Opening note: **Google Doc in Brave** (separate window) with ONLY the Goal, visible
- [ ] TaskRecorder: Task Description = Goal (exact) · Used Apps = DBeaver, Visual Studio Code, Google Sheets · OTA account · built-in display · mic green
- [ ] Close Studio, Slack, Odin pages, Metadata.rtf, this script, Chrome, Gemini
- [ ] Copilot/AI off in VS Code

---

## PART 5 – Recording script

Rules the whole time: mouse + menus · pause ~1 s after each click · point at what you name · say every shortcut before using it · type in short bursts (<45 s), then point/explain · never silent >45 s · windows in Fill (not Full Screen), no overlap >25 %.

### 0. Intro (≈0:00–0:20)
| Do | Say |
|---|---|
| Click **Start Recording** → minimize TaskRecorder (yellow button) | – |
| Leave Goal doc visible 3–4 s | "I will be beginning my task soon. Here is the workflow I have in mind." |
| Minimize the Goal doc (yellow button) | – |

### 1. DBeaver – check data quality (≈0:20–4:00) → LOOKUP
| Do | Say (own words) |
|---|---|
| Click **DBeaver** in Dock | "I'm opening DBeaver, where the sales database is already connected, to investigate why returns went up in Q3." |
| In Database Navigator (left) expand **sales.db → Tables**, point at each table | "There are four tables: customers with region, products with category, orders with the date and quantity, and returns with the reason." |
| Click **orders → Data** tab, scroll a little | "Each order has a date and a product, so I can join it to category and to the customer's region." |
| Top menu **SQL Editor → New SQL script** | "I'll open a new SQL script to check data quality first, before I calculate any rates." |
| Type **Query 1** (in 2 bursts), then click the orange **Execute** ▶ on the left of the editor | "First I count total orders, orders with missing quantity, total return rows, and distinct returned orders." |
| Point at results | "Return rows is higher than distinct returned orders – that means there are duplicate return records. If I counted rows I'd overstate the return rate, so I'll count distinct order IDs. Missing quantity doesn't affect a count of orders, so I'll keep those orders." |
| Remember/point at total_orders and returned_orders | "I'll use these two totals later to reconcile against the notebook." |

### 2. DBeaver – monthly rates + export (≈4:00–9:00) → CREATE
| Do | Say |
|---|---|
| Below Query 1, type **Query 2** in bursts | "Now the main query: for each month, category and region, I count distinct orders and distinct returned orders. I use a LEFT JOIN to returns so months with zero returns still appear." |
| Click inside Query 2 → **Execute** ▶ | "Running just this statement." |
| Scroll results, point at a West/Electronics row in July–Sept | "You can already see Electronics in the West has more returns in the summer months." |
| Right-click inside results → **Export data…** → **CSV** → **Next** (through pages) | "I'll export this result as CSV so I can analyse it in Python." |
| On Output page: **Directory** → choose **Desktop/ReturnsAnalysis**; **File name pattern** → `returns_by_month` → **Proceed** | "Saving it in the project folder as returns_by_month." |
| Type **Query 3** → **Execute** ▶ → point at top rows | "This query breaks Q3 returns down by reason – I'll need it to explain *why* returns increased." |
| Export same way → file name `reasons_q3` → **Proceed** | "Exporting the reasons as reasons_q3.csv for the summary workbook." |
| Minimize DBeaver | – |

### 3. VS Code – notebook (≈9:00–18:00) → CREATE
| Do | Say |
|---|---|
| Click **VS Code** in Dock; point at Explorer showing the CSVs | "Both exported CSV files are now in the project folder." |
| **File → New File… → Jupyter Notebook** | "I'm creating a Jupyter notebook for the analysis." |
| **File → Save As** → `returns_analysis` → Save | "Saving it as returns_analysis." |
| Top-right **Select Kernel → Python Environments → Python 3** | "Selecting the Python 3 kernel." |
| Type **Cell 1** → click ▷ left of the cell | "Loading pandas, matplotlib and the monthly CSV." Point at head: "Month, category, region, orders, returned orders." |
| Click **+ Code** → type **Cell 2** → ▷ | "Checking types and missing values." Point: "No missing values, and orders are integers." |
| **+ Code** → **Cell 3** → ▷ | "Removing any duplicate rows, converting month to a real date, and calculating the return rate as returned orders divided by orders. Then I print the totals." |
| Point at the two printed numbers | "These must match DBeaver." |

### 4. DBeaver – reconcile (≈18:00–19:00) → LOOKUP
| Do | Say |
|---|---|
| Click **DBeaver** in Dock → point at Query 1 result | "DBeaver showed X total orders and Y returned orders – the notebook shows the same, so nothing was lost in the export." |
| Minimize DBeaver | – |

### 5. VS Code – analysis (≈19:00–24:00) → MODIFY
| Do | Say |
|---|---|
| **+ Code** → **Cell 4** (2 bursts) → ▷ | "I keep only Q2 and Q3, sum orders and returns per category-region, recalculate the rate per quarter, and compute the change from Q2 to Q3. I sum counts first instead of averaging monthly rates, so small months don't distort it." |
| **+ Code** → **Cell 5** → ▷ | "To find unusual increases I use a z-score of the change. Anything above 1.5 standard deviations is flagged." Point at top rows: "Electronics–West jumped from about A% to B% – far above the others – followed by Apparel–South." (use your real numbers) |
| **+ Code** → **Cell 6** → ▷ | "Now a monthly trend chart by category, saved as a PNG for the report." Point at chart: "Electronics rises sharply from July." |
| **+ Code** → **Cell 7** → ▷ ; point at Explorer | "Exporting the top-five table to CSV for the workbook." |
| **File → Save** → minimize VS Code | "Saving the notebook." |

### 6. Google Sheets – summary + findings (≈24:00–30:00) → CREATE
| Do | Say |
|---|---|
| Click **Brave** in Dock (Sheets tab) → **Blank spreadsheet** | "In Google Sheets I'll build the summary for the operations manager." |
| Click title → name `Q3 Returns Analysis` | – |
| **File → Import → Upload → Browse** → Desktop/ReturnsAnalysis/**top5_outliers.csv** → *Replace current sheet* → **Import data** | "Importing the top five problem areas." |
| Double-click sheet tab → rename **Top 5** | – |
| Select q2_rate, q3_rate, change columns → **Format → Number → Percent** | "Showing the rates as percentages so they're easy to read." |
| Select change column → **Format → Conditional formatting → Color scale** → Done | "A colour scale highlights the biggest increases in red." |
| Select category to q3_rate data → **Insert → Chart** → Chart editor: **Column chart** | "A column chart compares Q2 and Q3 for each problem area." |
| Hand check: in an empty cell type `=` returned/orders for one row you saw in DBeaver (e.g. `=23/128`) → Enter, point at it vs the table | "Checking one rate by hand – it matches the table." |
| Bottom **+** (Add sheet) → rename **Reasons** → **File → Import → Upload** reasons_q3.csv → *Replace current sheet* | "Adding the Q3 return reasons." Point: "Most Electronics–West returns are Defective; Apparel–South are mostly Wrong size." |
| **+** → rename **Findings** | – |
| Type short lines (each <45 s, point after each): title, 3 findings, 3 recommendations | e.g. "Q3 return rate rose mainly in Electronics–West (A%→B%), reason Defective." / "Apparel–South (C%→D%), reason Wrong size." / "Recommend: quality check on West electronics batch; review size guide for apparel; monitor weekly." |
| **Insert → Image → Image over cells → Upload** → return_trend.png | "Adding the monthly trend chart to the findings page." |
| Check every number on Findings against Top 5 sheet (point at each) | "All numbers on the findings match the summary table." |

### 7. Download + finish (≈30:00–32:00)
| Do | Say |
|---|---|
| **File → Download → Microsoft Excel (.xlsx)** | "Downloading the workbook." |
| **File → Download → PDF** → Export: **Current sheet** (Findings) → **Export** | "And the Findings page as a PDF for the manager." |
| Finder → **Downloads** → rename to `return_summary.xlsx` and `findings_report.pdf` | "Renaming the files clearly." |
| Open findings_report.pdf briefly (in Brave, NOT Preview) and point | "The PDF is readable with the chart and recommendations – the task is complete." |
| Click **TaskRecorder** in Dock → **Stop Recording** → wait **Idle** | "The deliverables are saved, so I'm stopping the recording." |

---

## PART 6 – After recording

1. Check video.mp4 (start/middle/end, audio) and screenshots > 0.5 per second.
2. Make a folder, copy and rename (keep extensions):
   - `input 1.db` ← sales.db
   - `artifact 1.csv` ← returns_by_month.csv
   - `artifact 2.csv` ← reasons_q3.csv
   - `artifact 3.ipynb` ← returns_analysis.ipynb
   - `artifact 4.png` ← return_trend.png
   - `artifact 5.csv` ← top5_outliers.csv
   - `final output 1.xlsx` ← return_summary.xlsx
   - `final output 2.pdf` ← findings_report.pdf
   Right-click folder → Compress → rename `deliverables.zip`.
3. Copy to /Users/Shared: deliverables.zip, recording_XXXX.zip, video.mp4.
4. Main user → Studio veiw1b03 → upload Metadata.rtf, video.mp4, recording zip, deliverables.zip (each in its own field).
5. Run **AutoQC 1** (Files & Recording) and **AutoQC 2** (Narration) → fix or dispute flags.
6. Tick the 22 manual checks honestly.
7. Final note: `sales.db (input 1) was AI-generated before recording.`
8. **Submit** → status Ready for Review.

---

## PART 7 – Metadata.rtf text

**Topology**
```
DBeaver (CREATE) -> Visual Studio Code (CREATE) -> DBeaver (LOOKUP) -> Visual Studio Code (MODIFY) -> Google Sheets (CREATE)
```

**Request**
Paste the approved Goal from Studio, exactly as it is (same text as TaskRecorder).

**Task Description**
```
1. In DBeaver, inspect the four tables of the synthetic SQLite database sales.db and run a data-quality query that counts total orders, orders with missing quantity, return rows and distinct returned orders, identifying duplicate return records.
2. In DBeaver, write a SQL query that joins orders, products, customers and returns to count distinct orders and distinct returned orders by month, category and region, and export it as returns_by_month.csv; run a second query for Q3 return reasons and export it as reasons_q3.csv.
3. In Visual Studio Code, create the Jupyter notebook returns_analysis.ipynb, load the CSV with pandas, check types and missing values, remove duplicates, convert months to dates and calculate return rates.
4. Return to DBeaver to reconcile the notebook totals with the SQL totals.
5. In Visual Studio Code, compare Q2 and Q3 return rates by category and region, flag outliers using a z-score threshold of 1.5, create a monthly trend chart saved as return_trend.png, and export the top five problem areas to top5_outliers.csv.
6. In Google Sheets, import the top-five table and the Q3 reasons, format rates as percentages, apply conditional formatting, create a Q2 vs Q3 column chart, verify one rate by hand, and build a Findings sheet with the trend chart, key findings and recommendations.
7. Download the workbook as return_summary.xlsx and the Findings sheet as findings_report.pdf for the operations manager, and confirm that all numbers match the summary table.
```
