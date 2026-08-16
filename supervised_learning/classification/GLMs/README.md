# GLMs

GLMs are framework that is built on the *Linear Regression* model to make us do prediction on data that the target variable hasn't a normal distribution. When in our problem the assumptions of the linear regression violated we should move to other GLMs and use them.

**GLMs have three main components:**
- Random Component
- Systematic Component
- Link Function

> **Random component:** It's like the cars engine and we should analyse its properties. The random component is the distribution of the target variable and by looking at it we can pick the right link function for the model.

> **Systematic Component:** Systematic component is always a linear combination of features in every GLM and it's the base of the framework.
>
> $$
> \eta = \omega_1x_1 + \omega_2x_2 + \omega_3x_3 + ... + \epsilon
> $$

> **Link Function:** Link function is a function that connects the output of the linear predictor to the target variable. We choose the right link function in two ways: 1. experiment 2. commom link functions. There are many link functions that are commonly used for a specific random components and are suitable for them.
>
> $$
> \eta = g \text(y)
> $$
> $$
> g{-1}(\eta) = y
> $$
> that **g** is the link function, and **y** is our prediction.

**Assumptions of the linear regresion:**
- Linearity
- Independence
- Homoscedasticity
- Normality of Residuals

## Common Distributions:
- Binomial Distribution
- Normal Distribution
- Poisson Distribution
- ...

## Common Link Functions:
- **Identity** --> Linear Regression
- **Logit** --> Logistic Regression
- **Log** --> Poisson Regression
- **Inverse** --> Gamma Regression
- **Sigmoid**
- **Softmax**
- ...

# Different GLMs:
- **`Linear Regression`**
- **`Logistic Regression`**
- **`Poisson Regression`**
- **`Gamma Regression`**
- ...
