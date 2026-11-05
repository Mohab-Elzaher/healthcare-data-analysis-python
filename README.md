# Healthcare Data Analysis (Python + Power BI)

Exploratory analysis of 55,500 hospital admission records using Python and Pandas, plus an interactive Power BI dashboard covering billing, medical conditions, admission types, age groups, insurance providers, and test results.

> The dataset is a public **synthetic** healthcare dataset (from Kaggle). It contains no real patient information.

## Power BI Dashboard

![Power BI Dashboard](power%20bi.png)

**Features:**
- KPI cards: total billing ($1.42B), average billing ($25.54K), total patients (55.5K)
- Breakdowns by test result, gender, admission type, insurance provider, and age group (10-year bins)
- Admissions over time (yearly trend)
- Slicers for Hospital, Medical Condition, and Gender, plus cross-filtering between charts

## Questions
- What is the average billing amount, and does it vary by medical condition?
- How common is each medical condition and test result?
- How do Emergency admissions compare with the overall average?
- How are patients distributed across age groups?
- How does billing differ by condition **and** admission type together?
- How have admissions changed over time?

## Tools
- **Python**
- **Pandas**: filtering, `groupby`, `value_counts`, `pd.cut` binning, pivot tables
- **Power BI Desktop**: KPI cards, charts, binning, slicers, date hierarchies

## Dataset
15 columns, including Age, Gender, Medical Condition, Admission Type, Billing Amount, Insurance Provider, Medication, and Test Results.

## Key Findings
| Metric | Result |
| --- | --- |
| Records analyzed | 55,500 |
| Average billing amount | $25,539 |
| Emergency admissions | 18,269 (avg. billing $25,497) |
| Most common condition | Arthritis (9,308 patients) |
| Highest avg. billing by condition | Obesity ($25,806) |
| Lowest avg. billing by condition | Cancer ($25,162) |
| Age groups (0–30 / 31–60 / 61–100) | 10,499 / 24,631 / 20,370 |
| Yearly admissions (2020–2023) | About 11,000 per year |

- The six conditions are almost evenly represented, about 9,200–9,300 patients each.
- Average billing is very similar across conditions (within about $650).
- Test results, admission types, and gender all split almost evenly.
- The pivot table shows Diabetes has the highest average billing for Elective admissions ($25,983), and Cancer the lowest for Emergency admissions ($24,862).
- 2019 and 2024 show fewer admissions because the data covers only part of those years.
- These even splits are typical of a synthetic dataset, so checking whether data looks realistic was part of the analysis.

## Files
| File | Description |
| --- | --- |
| `healthcare.py` | Data exploration: preview, averages, condition counts, billing by condition, test results |
| `analysis.py` | Deeper analysis: Emergency filter, age-group binning, condition × admission type pivot table |
| `power BI project.pbix` | Interactive Power BI dashboard (open with Power BI Desktop) |
| `power bi.png` | Dashboard screenshot |
| `healthcare_dataset.csv` | Dataset (55,500 rows) |

## How to Run
**Python:**

    pip install pandas
    python healthcare.py
    python analysis.py

**Power BI:** Download `power BI project.pbix` and open it in [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (free).

## Author
**Mohab Elzaher**: Information Science (Health Informatics) student at the University of South Florida 
https://www.linkedin.com/in/mohabelzaher/
