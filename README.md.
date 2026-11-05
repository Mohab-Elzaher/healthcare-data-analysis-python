# Healthcare Data Analysis (Python)

Exploratory analysis of 55,500 hospital admission records using Python and Pandas, looking at billing, medical conditions, admission types, age groups, and test results.

> The dataset is a public **synthetic** healthcare dataset (from Kaggle). It contains no real patient information.

## Questions
- What is the average billing amount, and does it vary by medical condition?
- How common is each medical condition and test result?
- How do Emergency admissions compare with the overall average?
- How are patients distributed across age groups?
- How does billing differ by condition **and** admission type together?

## Tools
- **Python**
- **Pandas**: filtering, `groupby`, `value_counts`, `pd.cut` binning, pivot tables

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

- The six conditions (Arthritis, Diabetes, Hypertension, Obesity, Cancer, Asthma) are almost evenly represented, about 9,200–9,300 patients each.
- Average billing is very similar across conditions (within about $650), which is typical of a synthetic dataset.
- Test results split almost evenly between Abnormal, Normal, and Inconclusive.
- The pivot table shows Diabetes has the highest average billing for Elective admissions ($25,983), and Cancer the lowest for Emergency admissions ($24,862).

## Files
| File | Description |
| --- | --- |
| `healthcare.py` | Data exploration: preview, averages, condition counts, billing by condition, test results |
| `analysis.py` | Deeper analysis: Emergency filter, age-group binning, condition × admission type pivot table |
| `healthcare_dataset.csv` | Dataset (55,500 rows) |

## How to Run
```bash
pip install pandas
python healthcare.py
python analysis.py
```

## Author
**Mohab Elzaher**: Information Science (Health Informatics) student at the University of South Florida
[LinkedIn](https://www.linkedin.com/in/mohabelzaher)
