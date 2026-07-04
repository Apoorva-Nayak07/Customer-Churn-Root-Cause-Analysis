# Insight Memo: Customer Churn Root-Cause Analysis

**To:** VP of Customer Retention
**Re:** Why we're losing 26.5% of customers, and what to do about it

## The headline number
We are losing **1 in 4 customers annually** (26.5% churn rate, n=7,043). That's not evenly spread — it's concentrated in three identifiable groups, which means it's fixable with targeted action rather than a blanket program.

## Three root causes, ranked by impact

**1. Contract structure is the dominant driver.**
Month-to-month customers churn at **42.7%**, one-year contract customers at **11.3%**, two-year at **2.8%**. This isn't a small effect — it's a ~15x difference between the best and worst segment. Customers with no commitment have no friction to leave.

**2. The first year is the danger zone.**
Customers in their first 12 months churn at **47.4%**, compared to **9.5%** for customers past 49 months. Whatever onboarding experience we provide isn't building enough habit or perceived value fast enough.

**3. Missing support add-ons correlate with churn.**
Customers without tech support churn at **41.6%** vs **15.2%** with it. This may be causal (support reduces frustration) or a proxy for lower overall engagement — worth a follow-up test.

## Recommendation
Target the **1,113 month-to-month customers** currently paying above-average monthly charges who haven't churned yet (identified via SQL query). This is the highest-value, highest-risk segment — offer them a discounted annual-contract upgrade in the next billing cycle. Even a modest 15% conversion rate on this group would meaningfully move the overall churn number, because moving one customer from month-to-month to annual cuts their individual churn probability by roughly 4x based on the data above.

## Confidence & next step
A logistic regression model built on this data reaches 79.6% accuracy (ROC-AUC 0.838), confirming these aren't spurious patterns. Recommended next step: pilot the annual-contract offer on the 1,113-customer segment for one billing cycle and measure conversion before scaling company-wide.
