# DATA CRISIS — ROUND 2: THE MODEL IS LYING
**College Technical Symposium | ML & Data Forensics Incident Challenge**

---

## 1. Executive Mission Brief
Welcome to **Round 2 of DATA CRISIS**.

In this round, you are deployed as an emergency Data Science Taskforce for **Apex Telecom**, a major multi-regional telecommunications provider. Over recent quarters, Apex Telecom has noticed high subscriber turnover, and the executive board urgently requires an automated customer churn prediction system to trigger targeted interventions before subscribers abandon the service.

However, there is a catch: **THE MODEL IS LYING.**

The datasets gathered by the engineering division have been extracted from legacy operational databases, fragmented customer support logs, and real-time transaction pipelines. They contain severe data-quality problems, noisy signals, and hidden traps. A naive model trained blindly will fool you during evaluation, and catastrophic failures will occur when deployed to unseen production data.

Your mission is to perform rigorous data forensics, clean the corrupted inputs, detect when your model is deceiving you, adapt to dynamic crisis updates, and deliver a production-grade machine-learning pipeline that achieves real generalization.

---

## 2. Business Scenario
- **Client**: Apex Telecom Inc.
- **Objective**: Predict which current subscribers will cancel their telecommunication contracts (`churn = 1`) versus remain active (`churn = 0`).
- **Impact**: Retaining an existing customer costs $5\times$ less than acquiring a new one. False negatives (failing to detect a customer who churns) lead to direct revenue loss. False positives result in wasted retention incentives.

---

## 3. Dataset Package Overview
As a participating team, you are provided with four files in your workspace:

| Filename | Description |
| :--- | :--- |
| `train.csv` | Historical customer records with ground-truth target `churn`. Contains deliberate real-world data quality anomalies. |
| `test.csv` | Unseen test customers without the target column. Your pipeline must generate predictions for these records. |
| `submission_template.csv` | Template file showing the exact required schema for final scoring. |
| `README.md` | This competition manual and problem specification. |

---

## 4. Column Dictionary

Every record represents an individual customer account.

| Column Name | Type | Description / Domain Constraints |
| :--- | :--- | :--- |
| `customer_id` | String | Unique identifier (e.g., `C0001` in train, `T0001` in test). Primary Key. |
| `age` | Integer / Float | Customer age in years. Expected adult range: 18 to 75. |
| `gender` | Categorical | Demographic gender identifier (`Male`, `Female`). |
| `tenure_months` | Integer / Float | Number of consecutive months the customer has been subscribed (1 to 72). |
| `monthly_bill` | Numeric / Text | Monthly recurring charge for telecom services (in ₹ INR). Typical range: ₹299 – ₹1,999. |
| `total_bill` | Numeric / Text | Cumulative bill paid across the entire tenure. |
| `contract_type` | Categorical | Subscription commitment level (`Monthly`, `Annual`, `Two Year`). |
| `payment_method` | Categorical | Billing payment method (`UPI`, `Credit Card`, `NetBanking`, `Debit Card`). |
| `internet_plan` | Categorical | Primary broadband/connectivity tier (`Fiber`, `DSL`, `None`). |
| `support_calls` | Integer | Number of customer service telephone inquiries made over the last 12 months. |
| `complaints` | Integer | Formal escalated complaints logged against connectivity or billing. |
| `usage_hours` | Numeric | Average active service hours logged per month. |
| `last_login_days` | Integer | Days elapsed since the subscriber last opened the mobile self-care app. |
| `data_usage_gb` | Numeric | High-speed data consumption volume in Gigabytes (GB). |
| `num_devices` | Integer | Number of active connected hardware units registered to the account. |
| `discount_percent` | Integer / Text | Promotional discount applied to monthly billing (0% to 25%). |
| `late_payments` | Integer | Count of delayed invoice payments over the customer lifecycle. |
| `satisfaction_score`| Integer | Customer feedback rating recorded on a scale of 1 (Horrible) to 10 (Delighted). |
| `region` | Categorical | Geographic operating zone (`North`, `South`, `East`, `West`). |
| `plan_upgrade_count`| Integer | Frequency of tier upgrades requested by subscriber. |
| `paperless_billing`| Categorical | Account billing preference (`Yes`, `No`). |
| `favorite_theme` | Categorical | Selected mobile app display theme (`Dark`, `Light`, `System`). |
| `retention_offer_status` | Categorical | Recorded status of customer retention negotiations (`Offered`, `Accepted`, `Rejected`, `Not Offered`, `None`). |
| `churn` | Binary Flag | **TARGET COLUMN** (Training set only). `1` = Customer churned, `0` = Customer stayed. |

---

## 5. Target Definition
The target variable is `churn`:
- **`0`**: The customer remains an active subscriber.
- **`1`**: The customer has terminated their subscription.

---

## 6. Phase Breakdown & Time Structure

The round operates under strict time constraints totaling **60 to 70 minutes**:

```
+-------------------------------------------------------------------------------+
|  PHASE 1 (10 mins) : Data Normalization & Forensic Audit                      |
+-------------------------------------------------------------------------------+
                                      |
                           [ 🚨 CRISIS UPDATE 1 ]
                                      v
+-------------------------------------------------------------------------------+
|  PHASE 2 (10 mins) : Twist 1 Investigation & Adaptation                       |
+-------------------------------------------------------------------------------+
                                      |
                           [ 🚨 CRISIS UPDATE 2 ]
                                      v
+-------------------------------------------------------------------------------+
|  PHASE 3 (10 mins) : Twist 2 Investigation & Pipeline Tuning                  |
+-------------------------------------------------------------------------------+
                                      |
                           [ 🚨 CRISIS UPDATE 3 ]
                                      v
+-------------------------------------------------------------------------------+
|  PHASE 4 (25-30 mins): Twist 3 Adaptation, Final Training & Submission        |
+-------------------------------------------------------------------------------+
```

### Phase 1: Data Normalization (First 10 Minutes)
Your initial training dataset has deliberately not been sanitized. It mirrors raw enterprise telemetry. You must write robust data preparation scripts to detect and resolve:
1. **Missing Values**: Identify columns with empty entries and choose appropriate imputation strategies.
2. **Duplicate Records**: Audit both exact identical rows and duplicate primary keys with conflicting attributes.
3. **Inconsistent Categories**: Clean variations in casing, abbreviations, and trailing whitespace.
4. **Numerical Outliers & Anomalies**: Spot and handle impossible values violating realistic domain rules.
5. **Data Type Corruption**: Fix numbers stored as formatted strings (e.g., currency symbols, percentage signs, comma separators).
6. **Feature Relevance**: Scrutinize whether all provided features provide meaningful predictive signal or merely noise.

*Notice*: The organizers will **NOT** disclose where the faults are located. You must inspect the data using programmatic summaries.

### Phases 2, 3, & 4: Crisis Updates (Twists 1, 2, and 3)
At 10-minute intervals, the event controllers will broadcast a cryptic riddle. Each riddle points directly to an underlying flaw in naive modeling logic. You are expected to decipher the riddle, investigate your models and data, and modify your pipeline accordingly.

---

## 7. AI Assistance Policy

> [!NOTE]
> **AI Assistance is Explicitly Allowed.**

Participants may freely utilize AI tools, including:
- Large Language Models (ChatGPT, Gemini, Claude, Copilot, etc.)
- Official Documentation & Stack Overflow
- Online Machine Learning Tutorials

### Core Ground Rules
- **Understanding Required**: If your team qualifies, organizers may conduct a 2-minute oral audit. You must be able to articulate why your preprocessing steps, feature selections, and model architectures were chosen.
- **Strictly Prohibited**:
  1. No accessing organizer directories, network shares, or ground-truth files.
  2. No hardcoding or manually hand-crafting predictions for `test.csv`.
  3. No external labeled customer churn datasets.
  4. No collaboration between competing teams.
  5. Any attempt to breach organizer validation scripts results in immediate disqualification.

---

## 8. Final Submission Requirements

Your final deliverable must be a single CSV file named `submission.csv` placed in your submission folder.

### File Schema
The file must contain **exactly two columns** and matching headers:
```csv
customer_id,churn
T0001,0
T0002,1
T0003,0
...
```

### Integrity Checklist
- [x] Exact filename: `submission.csv`
- [x] Header present: `customer_id,churn`
- [x] Row count matches test set exactly (600 test customers)
- [x] Customer IDs match `test.csv` perfectly (no missing, extra, or duplicated IDs)
- [x] Predictions must be binary (`0` or `1`), or calibrated probabilities between `0.0` and `1.0`.

---

## 9. Evaluation & Qualification Criteria

### Primary Hurdle: The 90% Gate
To qualify for the final round, a team's submission **MUST** achieve:
$$\mathbf{\text{Accuracy} > 90.00\%}$$

Any submission scoring $\le 90.00\%$ accuracy is automatically marked **NOT QUALIFIED**.

### Secondary Ranking Score
Among the qualifying teams, ranking is determined using the official **Competition Composite Index**:

$$\text{Final Score} = 0.60 \times \text{Accuracy} + 0.20 \times F_1 + 0.10 \times \text{Recall} + 0.10 \times \text{Robustness}$$

Where:
- **Accuracy**: Overall correct classification percentage.
- **$F_1$-Score**: Harmonic mean of Precision and Recall on the churn class.
- **Recall**: Proportion of actual churners correctly caught by the model.
- **Robustness**: Consistency of model accuracy across shifted demographic sub-cohorts in the unseen test distribution.

**Top 3 qualifying teams** will advance to the Grand Finale!

---

*“A model that looks brilliant on yesterday's data may be completely blind to tomorrow's reality. Trust nothing until you verify.”*
