# Classification

Classfication is a supervised learning to classify and predict a discrete target variable.

## Characteristics to Categorize Different Classification Algorithms:

- **Parametric**
- **Non-Parametric**

> **Parametric:** Parametric models make strong assumptions on the data and have constant specified parameters.

> **Non-Parametric:** Non-parametric models does not make strong assumptions on the data and grow with the dataset size.

- **Linear**
- **Non-Linear**

> **Linear:** Linear models assume a linear relationship between the features and the target variable.

> **Non-Linear:** Non-linear models does not assume linear relationship and can capture more complex patterns.

- **Probabilistic**
- **Non-Probabilistic**

> **Probabilistic:** Probabilistic models do soft classification and output the proability-like classification so we can see how much they are sure about their prediction.

> **Non-Probabilistic:** Non-probabilistic models do hard classification and output the label not the probability.

- **Discriminative**
- **Generative**

> **Discriminative:** Discriminative models learn the decision boudary to classify variables.

> **Generative:** Generative models learn the distribution of the data not the decision boundary. We can generate the data for each class using them cause they know the distribution of the data.

- **Eager Learner**
- **Lazy Learner**

> **Eager Learner:** Eager learner models make an mathematical model of the data and do a lot of processes in the training step then the prediction step is mush faster and very computationally efficient.

> **Lazy Learner:** Lazy learner models do less in the training step, do not make any mathematical model of the data, and just save the data, In the prediction phase they do lots of processes to predict the class of the test data and their prediction step in more computationally complex than eager learner models.

## Different Types of Classification Models:

- **GLMs**

Parametric, Linear, Probabilistic, Discriminative, Eager Learner

- **Tree-Based Models**

Non-Parametric, Non-Linear, Non-Probabilistic|Probilistic, Discriminative, Eager Learner

- **SVMs**

Non-Parametric, Non-Linear|Linear, Non-Probabilistic, Discriminative, Eager Learner

- **Naive Bayes**

Parametric, Probabilistic, Generative, Eager Learner

- **K-Nearest Neighbors**

Non-Parametric, Non-Linear, Non-Probabilistic, Discriminative, Lazy Learner

## Models Covered:

- GLMs:
    - Logistic Regression
    - Probit Regression
    - Ordinal Regression
    - ...

- Tree-Based Algorithms:
    - ...

- Naive Bayes:
    - ...

- K-Nearest Neighbors:
    - ...

- SVMs:
    - ...
