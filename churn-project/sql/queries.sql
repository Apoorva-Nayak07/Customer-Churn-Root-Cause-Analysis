-- CHURN ROOT-CAUSE ANALYSIS: SQL QUERIES
-- Run with: sqlite3 churn.db < sql/queries.sql
-- Each query answers ONE business question. This is the pattern to memorize:
-- business question -> SQL question -> single clear answer.

-- Q1: Overall churn rate (the headline KPI)
SELECT
  Churn,
  COUNT(*) AS customers,
  ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM customers), 1) AS pct
FROM customers
GROUP BY Churn;

-- Q2: Churn rate by contract type (classic root-cause query - GROUP BY + ratio)
SELECT
  Contract,
  COUNT(*) AS total_customers,
  SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
  ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS churn_rate_pct
FROM customers
GROUP BY Contract
ORDER BY churn_rate_pct DESC;

-- Q3: Churn rate by tenure bucket (is it new customers or long-term ones leaving?)
SELECT
  CASE
    WHEN CAST(tenure AS INTEGER) <= 12 THEN '0-12 months'
    WHEN CAST(tenure AS INTEGER) <= 24 THEN '13-24 months'
    WHEN CAST(tenure AS INTEGER) <= 48 THEN '25-48 months'
    ELSE '49+ months'
  END AS tenure_bucket,
  COUNT(*) AS total_customers,
  SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
  ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS churn_rate_pct
FROM customers
GROUP BY tenure_bucket
ORDER BY churn_rate_pct DESC;

-- Q4: Churn rate by payment method (operational friction check)
SELECT
  PaymentMethod,
  COUNT(*) AS total_customers,
  ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS churn_rate_pct
FROM customers
GROUP BY PaymentMethod
ORDER BY churn_rate_pct DESC;

-- Q5: Does having tech support reduce churn? (does an add-on retain customers?)
SELECT
  TechSupport,
  COUNT(*) AS total_customers,
  ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS churn_rate_pct
FROM customers
GROUP BY TechSupport
ORDER BY churn_rate_pct DESC;

-- Q6: Window function example - rank contract types by churn rate
-- (window functions are a common Mu Sigma SQL-round ask)
SELECT
  Contract,
  churn_rate_pct,
  RANK() OVER (ORDER BY churn_rate_pct DESC) AS churn_rank
FROM (
  SELECT
    Contract,
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS churn_rate_pct
  FROM customers
  GROUP BY Contract
);

-- Q7: High-value customers at risk (business-prioritization query)
-- Customers paying above-average monthly charges who are on month-to-month contracts
SELECT COUNT(*) AS high_value_at_risk
FROM customers
WHERE Contract = 'Month-to-month'
  AND CAST(MonthlyCharges AS REAL) > (SELECT AVG(CAST(MonthlyCharges AS REAL)) FROM customers)
  AND Churn = 'No';  -- these are the ones worth targeting NOW, before they churn
