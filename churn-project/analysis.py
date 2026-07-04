"""
Churn Root-Cause Analysis
Business question: WHY are customers churning, and who should we target to retain?
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report

# ---------- 1. LOAD & CLEAN ----------
df = pd.read_csv("data/Telco-Customer-Churn.csv")

# TotalCharges has some blank strings for brand-new customers (tenure=0) -> coerce + fill
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"] = df["TotalCharges"].fillna(0)
df["tenure"] = df["tenure"].astype(int)
df["SeniorCitizen"] = df["SeniorCitizen"].astype(int)

print(f"Rows: {len(df)}  |  Churn rate: {(df['Churn']=='Yes').mean():.1%}")

# ---------- 2. FEATURE ENGINEERING ----------
df["tenure_bucket"] = pd.cut(df["tenure"], bins=[-1, 12, 24, 48, 100],
                             labels=["0-12mo", "13-24mo", "25-48mo", "49+mo"])

target = (df["Churn"] == "Yes").astype(int)

feature_cols = ["tenure", "MonthlyCharges", "TotalCharges", "SeniorCitizen",
                 "Contract", "PaymentMethod", "TechSupport", "OnlineSecurity",
                 "InternetService", "PaperlessBilling"]

X = df[feature_cols].copy()
encoders = {}
for col in X.select_dtypes(include="object").columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

# ---------- 3. MODEL ----------
X_train, X_test, y_train, y_test = train_test_split(X, target, test_size=0.25,
                                                      random_state=42, stratify=target)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

preds = model.predict(X_test)
probs = model.predict_proba(X_test)[:, 1]
print(f"\nModel accuracy: {accuracy_score(y_test, preds):.3f}")
print(f"Model ROC-AUC:   {roc_auc_score(y_test, probs):.3f}")

# ---------- 4. FEATURE IMPORTANCE (coefficients, standardized) ----------
importance = pd.Series(model.coef_[0], index=feature_cols).sort_values()
print("\nFeature impact on churn (positive = increases churn risk):")
print(importance.round(3))

# ---------- 5. CHARTS ----------
plt.figure(figsize=(7, 4))
churn_by_contract = df.groupby("Contract")["Churn"].apply(lambda s: (s == "Yes").mean() * 100)
churn_by_contract.sort_values(ascending=False).plot(kind="bar", color="#1F3864")
plt.ylabel("Churn rate (%)")
plt.title("Churn Rate by Contract Type")
plt.tight_layout()
plt.savefig("charts/churn_by_contract.png", dpi=120)
plt.close()

plt.figure(figsize=(7, 4))
churn_by_tenure = df.groupby("tenure_bucket")["Churn"].apply(lambda s: (s == "Yes").mean() * 100)
churn_by_tenure.plot(kind="bar", color="#2E5F9E")
plt.ylabel("Churn rate (%)")
plt.title("Churn Rate by Tenure Bucket")
plt.tight_layout()
plt.savefig("charts/churn_by_tenure.png", dpi=120)
plt.close()

plt.figure(figsize=(7, 5))
importance.plot(kind="barh", color="#C0504D")
plt.title("Feature Impact on Churn Risk (Logistic Regression Coefficients)")
plt.tight_layout()
plt.savefig("charts/feature_importance.png", dpi=120)
plt.close()

print("\nCharts saved to charts/")
