# 📊 Customer Churn Root-Cause Analysis
 
> **An end-to-end Data Analytics project that identifies why customers leave a telecom company and predicts which customers are most likely to churn using SQL, Python, Machine Learning, and Data Visualization.**

---

## 🚀 Project Overview

Customer churn directly impacts business revenue. This project analyzes customer behavior, uncovers the major reasons behind churn, and builds a Machine Learning model to identify high-risk customers before they leave.

The project combines **Business Analytics**, **SQL**, **Python**, and **Machine Learning** to provide actionable insights that help businesses improve customer retention and maximize profitability.

---

## 🎯 Business Objective

Answer the following critical business questions:

- Why are customers leaving?
- Which customer groups have the highest churn risk?
- Which factors contribute the most to churn?
- Which customers should the company prioritize for retention campaigns?
- How can predictive analytics reduce customer loss?

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Data Cleaning & Machine Learning |
| SQL (SQLite) | Business Analysis |
| Pandas | Data Manipulation |
| Matplotlib | Data Visualization |
| Scikit-Learn | Logistic Regression Model |
| SQLite | Database |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```
Customer-Churn-Root-Cause-Analysis
│
├── analysis.py              # ML pipeline
├── churn.db                 # SQLite database
├── sql/
│   └── queries.sql          # Business SQL queries
├── charts/                  # Generated visualizations
├── README.md
└── requirements.txt
```

---

# 📈 Project Workflow

```
Customer Data
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
SQL Business Analysis
      │
      ▼
Feature Engineering
      │
      ▼
Machine Learning Model
      │
      ▼
Prediction & Business Insights
```

---

# 🔍 Business Analysis

The project performs detailed SQL analysis to identify churn trends across multiple customer segments.

### ✔ Contract Type Analysis

- Month-to-Month
- One Year
- Two Year

### ✔ Customer Tenure Analysis

- New Customers
- Medium Tenure
- Long-Term Customers

### ✔ Payment Method Analysis

- Electronic Check
- Credit Card
- Bank Transfer
- Mailed Check

### ✔ Service Analysis

- Tech Support
- Online Security
- Internet Service
- Multiple Lines

---

# 🤖 Machine Learning Pipeline

The project uses **Logistic Regression** to classify customers into churn and non-churn categories.

### Data Preprocessing

- Missing value handling
- Label Encoding
- Feature Engineering
- Tenure Bucketing
- Train/Test Split

### Model

- Logistic Regression

### Evaluation Metrics

- Accuracy
- ROC-AUC Score
- Confusion Matrix

---

# 📊 Results

## Overall Customer Churn

**26.5%**

---

## Highest Risk Customer Segment

🔥 Month-to-Month Customers

**42.7% churn rate**

---

## Lowest Risk Customer Segment

🟢 Two-Year Contract Customers

**2.8% churn rate**

---

## Customer Tenure

| Tenure | Churn |
|---------|-------|
| 0–12 Months | 47.4% |
| 49+ Months | 9.5% |

---

## Tech Support Impact

| Service | Churn |
|----------|-------|
| Without Tech Support | 41.6% |
| With Tech Support | 15.2% |

---

## Machine Learning Performance

| Metric | Score |
|---------|--------|
| Accuracy | **79.6%** |
| ROC-AUC | **0.838** |

---

# 📌 Key Insights

✔ Contract type is the strongest predictor of churn.

✔ New customers are significantly more likely to leave.

✔ Customers without Tech Support exhibit substantially higher churn.

✔ Long-term customers demonstrate strong loyalty.

✔ Predictive analytics enables proactive retention strategies rather than reactive responses.

---

# 📊 Business Recommendations

### 🎯 Convert Month-to-Month Customers

Offer attractive discounts and incentives to encourage annual or two-year contracts.

---

### 🎯 Strengthen Early Customer Engagement

Launch onboarding campaigns during the first 12 months to improve customer satisfaction and retention.

---

### 🎯 Promote Value-Added Services

Bundle Tech Support and Online Security with internet plans to reduce churn.

---

### 🎯 Predict High-Risk Customers

Use the ML model to identify customers likely to churn and prioritize personalized retention offers.

---

# 📷 Sample Visualizations

- 📈 Churn by Contract Type
- 📉 Churn by Tenure Group
- 📊 Feature Importance
- 📌 Payment Method Analysis
- 📍 Customer Distribution

---

# ▶️ Getting Started

## Clone Repository

```bash
git clone https://github.com/Apoorva-Nayak07/Customer-Churn-Root-Cause-Analysis.git
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install pandas matplotlib scikit-learn
```

---

## Run the Project

```bash
python analysis.py
```

---

# 📚 Dataset

**IBM Telco Customer Churn Dataset**

- 7,043 Customers
- 21 Features
- Public Benchmark Dataset

---

# 🚀 Future Enhancements

- 📊 Interactive Power BI Dashboard
- 🌐 Streamlit Web Application
- ⚡ XGBoost & Random Forest Models
- 🎯 Customer Lifetime Value (CLV) Prediction
- 📧 Automated Retention Recommendation Engine
- ☁️ Cloud Deployment (AWS/Azure)
- 🔄 Real-Time Churn Prediction API

---

# 💡 Skills Demonstrated

- Business Analytics
- SQL Query Optimization
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Machine Learning
- Predictive Analytics
- Data Visualization
- Business Intelligence
- Problem Solving

---

# ⭐ Project Highlights

✅ End-to-End Analytics Project

✅ Real Business Use Case

✅ SQL + Python + Machine Learning

✅ Actionable Business Insights

✅ Production-Ready Repository Structure

✅ Placement & Portfolio Ready

---

## 👨‍💻 Author

**Apoorva Nayak**

Computer Science Engineering Student

Passionate about **Data Analytics**, **Machine Learning**, and **Software Development**.

If you found this project useful, consider giving it a ⭐ on GitHub!
