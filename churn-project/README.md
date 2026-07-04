# Churn Root-Cause Analysis

**Business question:** Why are customers churning, and which customers should we prioritize retaining right now?

## Approach
1. **SQL** (`sql/queries.sql`, run against `churn.db`) — quantified churn rate by contract type, tenure, payment method, and support add-ons.
2. **Python** (`analysis.py`) — cleaned the data, engineered a tenure-bucket feature, trained a logistic regression model, and extracted which factors most increase churn risk.
3. **Charts** (`charts/`) — visualized the top drivers for a non-technical audience.

## Key findings
- Overall churn rate: **26.5%**
- Month-to-month contracts churn at **42.7%** vs **2.8%** for two-year contracts — contract length is the single strongest lever
- New customers (0-12 months tenure) churn at **47.4%** vs **9.5%** for customers with 49+ months tenure
- Customers without tech support churn at **41.6%** vs **15.2%** for those with it
- Model: Logistic Regression, **79.6% accuracy, 0.838 ROC-AUC** — usable for prioritizing retention outreach, not just describing the past

## How to run
```
python3 analysis.py
```
Requires: pandas, scikit-learn, matplotlib (`pip install pandas scikit-learn matplotlib`)

## Dataset
IBM Telco Customer Churn dataset (7,043 customers, 21 features) — public, widely used for churn analysis.

## Future scope
- Add a live dashboard (Power BI/Streamlit) reading from `churn.db`
- Test a gradient-boosted model (XGBoost) for a lift in accuracy
- Turn the "high-value, at-risk" segment (Query 7 — month-to-month customers paying above-average charges) into an actual targeted retention campaign with a projected ROI
