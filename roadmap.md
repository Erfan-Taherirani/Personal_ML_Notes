# Hamrah Aval — Data Scientist Internship

## Interview Preparation & Onboarding Roadmap

**Candidate:** Erfan Taherirani
**Target:** Data Scientist Internship
**Company:** Hamrah Aval
**Current stage:** AI Virtual Interview
**Immediate preparation time:** 48 hours
**Potential next stage:** Face-to-face technical interview, ~2 weeks preparation

---

# 0. Preparation Strategy

## Objective

The goal is **not** to master the entire job description before the interview.

The goal is to demonstrate:

1. Strong Data Science fundamentals
2. Strong analytical/problem-solving ability
3. Practical Python/Pandas/SQL/ML experience
4. Understanding of statistics and probability
5. Understanding of the end-to-end data lifecycle
6. Awareness of Data Engineering / Big Data / AI technologies
7. Ability to explain technical concepts clearly
8. Ability to learn technologies that are currently less familiar
9. Genuine interest in working with data and AI
10. Good communication and systematic thinking

---

# 1. Current Skill Assessment

| Area                     | Current | Priority                     |
| ------------------------ | ------: | ---------------------------- |
| Python                   |     4/5 | 🔴 High                      |
| Pandas / NumPy           |     5/5 | 🔴 High                      |
| SQL                      |     5/5 | 🔴 High                      |
| Statistics / Probability |   3–4/5 | 🔴 Very High                 |
| Machine Learning         |     4/5 | 🔴 Very High                 |
| Deep Learning            |     3/5 | 🟠 Medium                    |
| PyTorch                  |     0/5 | 🟡 Low for virtual interview |
| NoSQL                    |     0/5 | 🟡 Low for virtual interview |
| ETL                      |     4/5 | 🔴 High                      |
| Big Data / Spark         |     0/5 | 🟡 Low for virtual interview |
| Airflow                  |     0/5 | 🟡 Low for virtual interview |
| LLM / RAG / Agents       |     2/5 | 🟠 Medium                    |

## Strategic conclusion

For the next 48 hours:

> **Depth > breadth.**

Do not attempt to learn Spark, Airflow, PyTorch, and NoSQL deeply.

Instead:

* Strengthen Statistics
* Strengthen ML fundamentals
* Review SQL
* Review Python/Pandas
* Review ETL concepts
* Prepare your projects
* Prepare behavioral/technical explanations
* Learn enough about Spark, NoSQL, Airflow and LLM/Agents to discuss them intelligently

---

# 2. Expected Virtual Interview

Because the first interview is conducted by an **AI interviewer**, expect a structured screening rather than a deep engineering interview.

Most likely categories:

```text
AI Virtual Interview
│
├── 1. Self Introduction
│
├── 2. Motivation
│
├── 3. Resume / Projects
│
├── 4. Python / SQL
│
├── 5. Statistics / Probability
│
├── 6. Machine Learning
│
├── 7. Deep Learning
│
├── 8. Data Engineering / ETL
│
├── 9. Problem Solving
│
└── 10. Learning Ability / Behavioral
```

## Expected weighting

| Category                        | Estimated importance |
| ------------------------------- | -------------------: |
| Resume + project discussion     |                ⭐⭐⭐⭐⭐ |
| ML fundamentals                 |                ⭐⭐⭐⭐⭐ |
| Statistics / probability        |                ⭐⭐⭐⭐½ |
| SQL                             |                ⭐⭐⭐⭐½ |
| Python / data processing        |                 ⭐⭐⭐⭐ |
| Problem solving                 |                 ⭐⭐⭐⭐ |
| ETL / data engineering concepts |                 ⭐⭐⭐½ |
| Deep Learning                   |                  ⭐⭐⭐ |
| Big Data / Spark                |                  ⭐⭐½ |
| NoSQL                           |                   ⭐⭐ |
| Airflow                         |                   ⭐⭐ |
| LLM / Agents                    |                  ⭐⭐½ |

These are estimates, not information provided by Hamrah Aval.

---

# 3. The 48-Hour Virtual Interview Plan

## Day 1 — Core Technical Preparation

### Block 1 — Statistics & Probability

**2–3 hours**

Review:

* Mean / median / variance / standard deviation
* Probability
* Conditional probability
* Bayes theorem
* Expected value
* Covariance / correlation
* Normal distribution
* Central Limit Theorem
* Sampling
* Confidence interval
* Hypothesis testing
* p-value
* Type I / Type II errors
* A/B testing

### Block 2 — Machine Learning

**3 hours**

Review:

* Supervised vs unsupervised learning
* Regression vs classification
* Linear regression
* Logistic regression
* Decision trees
* Random Forest
* Gradient Boosting
* KNN
* SVM
* K-Means
* PCA
* Regularization
* Bias / variance
* Overfitting / underfitting
* Cross-validation
* Data leakage
* Feature engineering
* Feature selection

### Block 3 — SQL

**1.5–2 hours**

Review:

* JOINs
* GROUP BY
* HAVING
* CTE
* Subqueries
* CASE
* Window functions
* ROW_NUMBER
* RANK
* DENSE_RANK
* Aggregation
* NULL handling
* Date operations

### Block 4 — Python / Pandas

**1–1.5 hours**

Review:

* Lists / dictionaries / sets
* Functions
* List comprehensions
* Exceptions
* NumPy arrays
* Pandas filtering
* groupby
* merge
* pivot
* aggregation
* missing values
* duplicates
* vectorization

---

# 4. Day 2 — Resume + Broader JD

## Block 5 — Your Projects

**2 hours**

Be prepared to explain every project using:

```text
Problem
↓
Business / practical objective
↓
Data
↓
Data quality
↓
EDA
↓
Feature engineering
↓
Model / analysis
↓
Evaluation
↓
Results
↓
Limitations
↓
Next steps
```

Never describe a project as:

> "I used Pandas, Scikit-learn and Random Forest."

Instead explain:

> "The problem was X. I used Y data to answer Z. After validating and preparing the data, I performed EDA and feature engineering. I compared several models using an appropriate validation strategy and selected the final model based on the relevant evaluation metric."

The second explanation demonstrates **thinking**, not tool usage.

---

# 5. Your Most Important Project

Your strongest project for this interview is the:

## AI Impact on Students / GPA Prediction

Know these numbers and decisions:

* Dataset size: ~50,000 observations
* Target: post-semester GPA / GPA difference
* Regression problem
* MSE ≈ 0.021
* RMSE ≈ 0.148
* MAE ≈ 0.116
* R² ≈ 0.908

Be able to explain:

### Why regression?

Because the target is continuous.

### Why RMSE?

It measures prediction error in the same unit as the target and penalizes larger errors more strongly.

### What does R² = 0.908 mean?

Approximately 90.8% of the variance in the target is explained by the model **on the evaluated data**, assuming the evaluation procedure was correctly designed.

Do not say:

> "The model is 90.8% accurate."

That is incorrect for regression.

---

# 6. Your E-Commerce Project

This project is useful because it demonstrates:

* SQL
* Data analysis
* Data modeling
* Business KPIs
* Power BI
* Data validation
* Business thinking

Be able to explain:

```text
Raw order data
↓
Data understanding
↓
Data quality audit
↓
Cleaning / validation
↓
SQL transformation
↓
Analytical queries
↓
KPIs
↓
Business interpretation
↓
Power BI
```

Important business concepts:

* Revenue
* Orders
* Items sold
* AOV
* Revenue per item
* Profit
* Profit margin
* Customer segmentation
* Time analysis
* Geographic analysis

---

# 7. High-Probability Statistics Questions

## Q1. Mean vs Median?

**Answer:**

Mean is sensitive to extreme values, while median is more robust to outliers. For highly skewed distributions, median can better represent the typical observation.

---

## Q2. What is variance?

**Answer:**

Variance measures the average squared deviation of observations from their mean. It represents the dispersion of a distribution.

---

## Q3. What is standard deviation?

**Answer:**

Standard deviation is the square root of variance and expresses dispersion in the same units as the original variable.

---

## Q4. What is conditional probability?

**Answer:**

The probability of an event occurring given that another event has already occurred.

$$
P(A|B)=\frac{P(A\cap B)}{P(B)}
$$
---

## Q5. What is Bayes' theorem?

$$
P(A|B)=\frac{P(B|A)P(A)}{P(B)}
$$

It allows us to update the probability of a hypothesis using observed evidence.

---

## Q6. Correlation vs causation?

**Answer:**

Correlation measures statistical association between variables. It does not by itself establish that changes in one variable cause changes in another.

---

## Q7. What is a p-value?

**Answer:**

The p-value is the probability, assuming the null hypothesis is true, of observing a result at least as extreme as the one obtained.

A small p-value provides evidence against the null hypothesis.

It is **not** the probability that the null hypothesis is true.

---

## Q8. Type I vs Type II error?

**Answer:**

* Type I: rejecting a true null hypothesis
* Type II: failing to reject a false null hypothesis

---

## Q9. What is the Central Limit Theorem?

**Answer:**

Under appropriate conditions, the sampling distribution of the sample mean approaches a normal distribution as sample size increases, even when the underlying population is not normally distributed.

---

# 8. High-Probability Machine Learning Questions

## Q1. Supervised vs unsupervised learning?

**Supervised:** learn from labeled data.

Examples:

* Regression
* Classification

**Unsupervised:** discover structure without labeled targets.

Examples:

* Clustering
* Dimensionality reduction

---

## Q2. Overfitting?

A model overfits when it learns patterns specific to the training data and fails to generalize well to unseen data.

Typical solutions:

* More data
* Regularization
* Simpler model
* Cross-validation
* Feature selection
* Early stopping
* Data augmentation for relevant DL problems

---

## Q3. Bias vs variance?

**Bias:** error from overly simplistic assumptions.

**Variance:** sensitivity to changes in the training data.

High bias → underfitting.

High variance → overfitting.

---

## Q4. What is regularization?

Regularization adds a penalty to model complexity to reduce overfitting.

### L1

Encourages sparse coefficients and can perform feature selection.

### L2

Penalizes large coefficients and generally encourages smoother models.

---

## Q5. Random Forest vs Gradient Boosting?

### Random Forest

Builds many trees independently and combines their predictions.

### Gradient Boosting

Builds trees sequentially, with later trees focusing on errors made by previous ones.

A useful interview answer:

> "For tabular data, both are strong choices. I would compare them empirically while considering dataset size, noise, interpretability, training cost and validation performance."

---

## Q6. What is cross-validation?

Cross-validation repeatedly splits the training data into training and validation portions to obtain a more robust estimate of model performance and support model selection.

Important:

> The final test set should remain untouched until final evaluation.

---

## Q7. What is data leakage?

Data leakage occurs when information unavailable at prediction time enters the training process.

Example:

Using a customer's future churn status or post-event information to predict an earlier event.

Leakage can produce unrealistically strong validation results.

---

## Q8. Why split before preprocessing?

To prevent information from the validation/test set influencing preprocessing decisions.

For example, scaling should generally be:

```text
Training data
→ fit scaler

Validation/Test data
→ transform using fitted scaler
```

not:

```text
Entire dataset
→ fit scaler
→ split
```

---

# 9. Classification Metrics

Know when each metric matters.

| Metric    | Important when                                    |
| --------- | ------------------------------------------------- |
| Accuracy  | Classes reasonably balanced and costs are similar |
| Precision | False positives are expensive                     |
| Recall    | False negatives are expensive                     |
| F1        | Need balance between precision and recall         |
| ROC-AUC   | Ranking/class discrimination                      |
| PR-AUC    | Particularly useful with strong class imbalance   |

Example:

For fraud detection, missing fraudulent transactions may be expensive → **recall matters**.

---

# 10. Regression Metrics

### MAE

Average absolute prediction error.

### MSE

Average squared error.

### RMSE

Square root of MSE; same units as target.

### R²

Measures the proportion of variance explained relative to a baseline mean predictor.

---

# 11. SQL Questions You Must Be Able to Solve

You should be able to write queries for:

### Top-N per group

Example:

> Find the top 3 customers by revenue in every region.

Use:

```sql
ROW_NUMBER() OVER (
    PARTITION BY region
    ORDER BY revenue DESC
)
```

or `RANK()` / `DENSE_RANK()` depending on tie requirements.

---

### Running total

Know:

```sql
SUM(revenue) OVER (
    ORDER BY order_date
)
```

---

### Month-over-month growth

Understand:

```text
Current month
vs
Previous month
```

using `LAG()`.

---

### Duplicate detection

Use:

```sql
GROUP BY key
HAVING COUNT(*) > 1
```

---

### Conditional aggregation

Know:

```sql
SUM(CASE WHEN condition THEN value ELSE 0 END)
```

---

# 12. ETL

## What is ETL?

```text
Extract
↓
Transform
↓
Load
```

Data is extracted from source systems, transformed into a usable form, and loaded into a target system.

## ETL vs ELT

### ETL

```text
Extract
→ Transform
→ Load
```

### ELT

```text
Extract
→ Load
→ Transform
```

ELT is common in modern cloud/data-platform architectures because transformation can be performed inside scalable analytical systems.

---

# 13. Data Pipeline Concepts

Know these terms:

### Batch processing

Data is processed periodically.

Example:

> Daily customer aggregation.

### Streaming

Data is processed continuously or with very low latency.

Example:

> Real-time telecom network events.

### Idempotency

Running the same pipeline operation multiple times should not unintentionally duplicate or corrupt the result.

### Data quality

Check:

* Missing values
* Duplicates
* Invalid values
* Referential integrity
* Schema changes
* Unexpected distributions

---

# 14. Big Data — Minimum Interview Knowledge

You do **not** need to become a Spark expert before the virtual interview.

Understand:

## Why Big Data?

Traditional single-machine processing becomes insufficient when data volume, velocity, or complexity becomes too large.

## Distributed processing

Instead of processing everything on one machine:

```text
Large dataset
      ↓
Partition
 ┌────┼────┐
 ↓    ↓    ↓
Node Node Node
 └────┼────┘
      ↓
Combine results
```

## Spark

Apache Spark is a distributed data-processing framework.

Know these concepts:

* Driver
* Executors
* DataFrame
* Transformation
* Action
* Lazy evaluation
* Partition
* Shuffle

A good answer:

> "I haven't used Spark in a production environment yet, but I understand its distributed processing model, DataFrames, transformations, actions, partitioning and shuffle. It's one of the technologies I would prioritize learning if I join the team."

This is much better than pretending to have experience.

---

# 15. NoSQL — Minimum Interview Knowledge

Know why relational databases are not always ideal for every workload.

### SQL databases

Good for:

* Structured data
* Strong relationships
* Transactions
* Complex relational queries

### NoSQL

Can be useful for:

* Flexible schemas
* Very large distributed workloads
* Specific high-throughput access patterns

Know these categories:

```text
Document      → MongoDB
Key-value     → Redis
Column-family → Cassandra
Graph         → Neo4j
```

Do not claim practical experience if you don't have it.

---

# 16. Airflow — Minimum Interview Knowledge

Airflow is an orchestration platform.

Think:

```text
Extract
   ↓
Validate
   ↓
Transform
   ↓
Load
   ↓
Train
```

Airflow manages:

* Scheduling
* Dependencies
* Retries
* Monitoring
* Logging
* Workflow execution

### Important term

**DAG = Directed Acyclic Graph**

It represents tasks and their dependencies.

---

# 17. Deep Learning — Minimum Interview Knowledge

Know:

```text
Input
↓
Weights + Bias
↓
Activation
↓
Hidden Layers
↓
Output
↓
Loss
↓
Backpropagation
↓
Gradient Descent
```

Understand:

* Neuron
* Weight
* Bias
* Activation function
* Loss
* Forward pass
* Backpropagation
* Gradient descent
* Epoch
* Batch
* Learning rate
* Optimizer

### Activation functions

Know:

* ReLU
* Sigmoid
* Softmax
* Tanh

### Architectures

| Architecture | Typical use                                  |
| ------------ | -------------------------------------------- |
| MLP          | Tabular / general                            |
| CNN          | Images / spatial patterns                    |
| RNN          | Sequential data                              |
| LSTM         | Long-term sequential dependencies            |
| Transformer  | Language / sequence modeling / multimodal AI |

---

# 18. LLM / RAG / Agent — Minimum Interview Knowledge

You currently have limited experience here, so focus on conceptual fluency.

## RAG

```text
Documents
↓
Chunking
↓
Embeddings
↓
Vector database
↓
Similarity search
↓
Retrieved context
↓
LLM
↓
Answer
```

Purpose:

> Provide external/domain-specific information to an LLM at inference time.

## Agent

An AI agent typically combines:

```text
LLM
+
Tools
+
Context / Memory
+
Decision / Planning
```

Example:

> An agent receives a business question, queries a database, analyzes the result, and generates an explanation.

---

# 19. System Thinking

This is explicitly mentioned in the JD and should become one of your strongest interview characteristics.

When given a vague problem, don't immediately choose an algorithm.

Use:

```text
1. Define the problem
        ↓
2. Define the objective
        ↓
3. Identify stakeholders
        ↓
4. Identify available data
        ↓
5. Define target / KPI
        ↓
6. Check data quality
        ↓
7. Establish baseline
        ↓
8. Select method
        ↓
9. Evaluate
        ↓
10. Deploy / communicate
        ↓
11. Monitor
```

This demonstrates **systematic problem solving**.

---

# 20. Example System-Design Question

### Question

> Hamrah Aval wants to predict customers who are likely to churn. How would you approach it?

### Strong answer structure

```text
First, I would define what churn means and determine
the prediction horizon.

Then I would identify relevant historical customer data,
such as usage, recharge behavior, complaints, plan history,
and customer activity.

I would construct features using only information available
before the prediction point and carefully avoid temporal
data leakage.

I would establish a baseline model, then compare suitable
classification algorithms using an appropriate validation
strategy.

Because churn datasets can be imbalanced, I would not rely
only on accuracy. I would evaluate metrics such as precision,
recall, F1 and PR-AUC depending on the business objective.

Finally, I would consider how predictions would be delivered
to the business, monitored over time, and retrained as
customer behavior changes.
```

This type of answer demonstrates much more than simply saying:

> "I would use Random Forest."

---

# 21. Behavioral Questions

Prepare concise answers for:

### Tell me about yourself.

Structure:

```text
Current identity
→ Data Science experience
→ strongest technical skills
→ relevant projects
→ why this internship
```

### Why Data Science?

Connect:

```text
Problem solving
+
Mathematical thinking
+
Programming
+
Real-world impact
```

### Why Hamrah Aval?

Focus on:

* Large-scale data
* Telecom domain
* Real-world data problems
* Data/AI applications
* Opportunity to learn production-level systems

### Why should we select you?

Use:

```text
Strong fundamentals
+
Practical project experience
+
Problem-solving approach
+
Fast learning
+
Honest awareness of gaps
```

---

# 22. Handling Missing Experience

This is critical.

Never say:

> "I know Spark."

if you have never used it.

Instead:

> "I haven't had hands-on production experience with Spark yet, but I understand the core concepts and I have strong experience with Python and data processing. I'm confident I can transfer that foundation to PySpark quickly."

Use this pattern:

```text
Acknowledge gap
↓
State what you DO understand
↓
Connect to existing skill
↓
Show learning ability
```

Example:

> "I haven't used Airflow practically yet. I understand its role in orchestrating data pipelines, DAGs, dependencies, scheduling and retries. My existing ETL experience gives me the conceptual foundation, and Airflow is one of the tools I would prioritize learning in the internship."

---

# 23. AI Interview Communication Rules

Because the interviewer is an AI system:

## Rule 1 — Answer the question directly

Bad:

> "There are many different perspectives..."

Good:

> "Overfitting occurs when a model performs well on training data but generalizes poorly to unseen data."

---

## Rule 2 — Give the definition first

Use:

```text
Definition
→ Explanation
→ Example
```

---

## Rule 3 — Avoid unnecessarily long answers

Target:

* Simple technical question → 20–40 seconds
* Medium question → 45–75 seconds
* Project question → 60–120 seconds

---

## Rule 4 — Use technical terminology correctly

Don't replace technical concepts with vague language.

Say:

* data leakage
* cross-validation
* class imbalance
* regularization
* feature engineering
* ETL
* data pipeline
* distributed processing

---

## Rule 5 — If you don't know

Do not hallucinate.

Use:

> "I haven't worked with that directly, so I don't want to claim practical experience. My understanding is..."

Then explain what you know.

---

# 24. 30 Questions You Should Practice Before the AI Interview

## Statistics

1. Mean vs median?
2. Variance vs standard deviation?
3. Covariance vs correlation?
4. Conditional probability?
5. Bayes theorem?
6. Central Limit Theorem?
7. Confidence interval?
8. p-value?
9. Type I vs Type II error?
10. Hypothesis testing?

## Machine Learning

11. Supervised vs unsupervised learning?
12. Overfitting?
13. Underfitting?
14. Bias vs variance?
15. Regularization?
16. L1 vs L2?
17. Cross-validation?
18. Data leakage?
19. Precision vs recall?
20. Random Forest vs Gradient Boosting?

## Deep Learning

21. What is a neural network?
22. What is backpropagation?
23. What is gradient descent?
24. Why use activation functions?
25. CNN vs RNN vs Transformer?

## Data Engineering

26. ETL vs ELT?
27. SQL vs NoSQL?
28. What is Big Data?
29. What is Spark?
30. What is Airflow?

You should be able to answer these **without notes**.

---

# 25. 10 Questions About Your Projects

Prepare answers for:

1. What was the problem?
2. Why did you choose this problem?
3. What was the dataset?
4. What data-quality issues did you find?
5. What preprocessing did you perform?
6. How did you perform EDA?
7. How did you engineer/select features?
8. Why did you choose your model?
9. How did you evaluate it?
10. What would you improve if you had more time?

---

# 26. Interview Answer Framework

For technical questions:

```text
Definition
↓
Mechanism
↓
Practical implication
↓
Example
```

For project questions:

```text
Problem
↓
Approach
↓
Technical decisions
↓
Result
↓
Limitation
```

For system questions:

```text
Objective
↓
Data
↓
Architecture
↓
Model / Method
↓
Evaluation
↓
Deployment
↓
Monitoring
```

For unknown technologies:

```text
Honest limitation
↓
Current understanding
↓
Transferable knowledge
↓
Learning plan
```

---

# 27. Two-Week Technical Preparation After Passing

If you pass the AI interview, switch from **screening preparation** to **technical depth**.

## Week 1

### Day 1

Statistics + Probability

### Day 2

Machine Learning fundamentals

### Day 3

ML implementation + evaluation

### Day 4

Deep Learning + neural networks

### Day 5

SQL + databases + NoSQL

### Day 6

ETL + data pipelines

### Day 7

Spark + distributed processing

---

## Week 2

### Day 8

Airflow + orchestration

### Day 9

LLM + RAG + Agents

### Day 10

End-to-end data architecture

### Day 11

Project deep dive

### Day 12

SQL + Python coding

### Day 13

Technical interview simulation

### Day 14

Weak-area revision + final mock interview

---

# 28. Long-Term Onboarding Curriculum

## Phase 1 — Programming & Data

* Python
* NumPy
* Pandas
* Git
* SQL

**Target:** Strong

---

## Phase 2 — Mathematical Foundation

* Probability
* Statistics
* Linear algebra
* Calculus
* Optimization

**Target:** Strong practical understanding

---

## Phase 3 — Data Analysis

* EDA
* Data cleaning
* Data validation
* Visualization
* Business KPIs

**Target:** Strong

---

## Phase 4 — Machine Learning

* Regression
* Classification
* Clustering
* Dimensionality reduction
* Feature engineering
* Feature selection
* Model evaluation
* Hyperparameter optimization

**Target:** Strong

---

## Phase 5 — Deep Learning

* Neural networks
* Backpropagation
* Optimization
* CNN
* RNN/LSTM
* Transformers
* PyTorch

**Target:** Intermediate

---

## Phase 6 — Data Engineering

* ETL / ELT
* Data pipelines
* Data warehouses
* Data lakes
* Data quality
* Batch / streaming

**Target:** Intermediate

---

## Phase 7 — Big Data

* Distributed computing
* Spark
* PySpark
* Partitioning
* Shuffle
* Spark SQL

**Target:** Practical intermediate

---

## Phase 8 — Databases

### SQL

Advanced

### NoSQL

Conceptual → practical

Learn at least one document database such as MongoDB.

---

## Phase 9 — Orchestration

Learn:

* Airflow
* DAGs
* Scheduling
* Dependencies
* Retries
* Monitoring

**Target:** Practical beginner/intermediate

---

## Phase 10 — Modern AI

Learn:

* LLM fundamentals
* Embeddings
* Vector databases
* RAG
* Function calling
* Agents
* Agent evaluation
* AI APIs

**Target:** Practical beginner/intermediate

---

# 29. Recommended Learning Philosophy

For every technology:

```text
WHY
↓
WHAT
↓
HOW
↓
WHEN
↓
IMPLEMENT
↓
EXPLAIN
```

Do not learn:

> "Spark syntax"

before understanding:

> "Why distributed processing is necessary."

Do not learn:

> "Random Forest parameters"

before understanding:

> "Why an ensemble of trees can generalize better."

Do not learn:

> "Airflow operators"

before understanding:

> "Why workflow orchestration exists."

---

# 30. Priority System

Use this classification.

## 🔴 MUST KNOW

Before the technical interview:

* Python
* Pandas / NumPy
* SQL
* Probability
* Statistics
* ML fundamentals
* Model evaluation
* Feature engineering
* Data leakage
* Overfitting
* Bias/variance
* ETL
* Data quality
* Your projects
* Problem-solving methodology

## 🟠 SHOULD KNOW

* Deep Learning fundamentals
* Neural networks
* PyTorch concepts
* NoSQL concepts
* Spark concepts
* Data warehouse / data lake
* Airflow concepts
* LLM / RAG fundamentals

## 🟡 NICE TO KNOW

* Advanced Spark optimization
* Advanced Airflow
* Advanced MLOps
* Kubernetes
* Advanced RL
* Advanced distributed systems
* Advanced agent architectures

---

# 31. Your Biggest Interview Risk

Your biggest risk is **not** that you don't know Spark or PyTorch.

Your biggest risk would be:

> Knowing many concepts but being unable to explain your reasoning clearly.

Therefore prioritize:

```text
Understanding
>
Memorization
```

and:

```text
Reasoning
>
Tool familiarity
```

and:

```text
Practical experience
>
Certificates
```

---

# 32. Your Biggest Competitive Advantage

Your combination is useful:

```text
Mechanical Engineering
        +
Mathematical background
        +
Python
        +
SQL
        +
Data Analysis
        +
Machine Learning
        +
Practical projects
```

Position yourself as someone who can:

> **understand a problem mathematically, work with the data, build an analytical/modeling solution, and reason about how that solution fits into a larger data system.**

That is much stronger than presenting yourself as someone who simply knows ML algorithms.

---

# 33. Final 48-Hour Checklist

## Technical

* [ ] Probability
* [ ] Bayes theorem
* [ ] Statistics
* [ ] p-value
* [ ] Hypothesis testing
* [ ] CLT
* [ ] Regression
* [ ] Classification
* [ ] Overfitting
* [ ] Bias/variance
* [ ] Regularization
* [ ] Cross-validation
* [ ] Data leakage
* [ ] Classification metrics
* [ ] SQL joins
* [ ] CTE
* [ ] Window functions
* [ ] Pandas
* [ ] ETL
* [ ] Big Data concepts
* [ ] Spark concepts
* [ ] NoSQL concepts
* [ ] Airflow concepts
* [ ] Neural network fundamentals
* [ ] RAG / Agent concepts

## Personal

* [ ] 60-second self-introduction
* [ ] Why Data Science?
* [ ] Why Hamrah Aval?
* [ ] Why this internship?
* [ ] Strongest project explanation
* [ ] E-commerce project explanation
* [ ] Biggest technical challenge
* [ ] Project failure/limitation
* [ ] Example of self-learning
* [ ] Example of problem solving
* [ ] Honest explanation of technology gaps

## Final rule

Before the interview, don't try to learn everything.

Be able to **explain what you know exceptionally well**, and demonstrate that you can **learn what you don't know**.
