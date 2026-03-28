# Maximum Likelihood Estimation for Traffic Modeling

## Introduction

Modeling traffic flow is important for urban planning and infrastructure management. In this assignment, we model the number of vehicles passing through a busy road per minute using the Poisson distribution.

The objective is to estimate the traffic intensity parameter λ using Maximum Likelihood Estimation.

## Poisson Distribution

The Poisson distribution models the probability of observing k events within a fixed time interval.

P(k|λ) = (λ^k e^-λ) / k!

Where:

k = number of vehicles observed
λ = average number of vehicles per minute

## Likelihood Function

Given a dataset:

{k₁, k₂, …, kₙ}

The likelihood function is the product of individual probabilities:

L(λ) = ∏ P(kᵢ | λ)

Substituting the Poisson distribution:

L(λ) = ∏ (λ^kᵢ e^-λ / kᵢ!)

## Log-Likelihood

To simplify calculations, we take the natural logarithm:

ℓ(λ) = log L(λ)

After simplification:

ℓ(λ) = Σ (kᵢ log λ − λ − log(kᵢ!))

Since log(kᵢ!) does not depend on λ, it is treated as a constant.

## Derivation of the Maximum Likelihood Estimator

Taking the derivative with respect to λ:

dℓ/dλ = Σ (kᵢ / λ − 1)

Setting the derivative equal to zero:

Σ (kᵢ / λ − 1) = 0

Solving for λ gives:

λ̂ = (1/n) Σ kᵢ

Therefore, the MLE estimator for the Poisson parameter is the sample mean.

## Data Analysis

The observed traffic data contains 14 measurements of the number of vehicles passing per minute.

Dataset:

12, 15, 10, 8, 14, 11, 13, 16, 9, 12, 11, 14, 10, 15

The sample mean is:

λ ≈ 12.14 vehicles per minute.

Both the analytical formula and numerical optimization using Python produce the same value.

## Visualization

The histogram of the observed traffic data was compared with the Poisson probability mass function.

The Poisson curve follows the general pattern of the observed data, indicating that the Poisson model reasonably approximates the traffic flow.

## Outlier Analysis

If a mistaken observation of 200 vehicles is included in the dataset, the sample mean increases to approximately 24.67 vehicles per minute.

This shows that Maximum Likelihood Estimation is highly sensitive to outliers because it relies on the arithmetic mean.

Such an error could mislead city planners into believing that traffic volume is much higher than it actually is.

## Conclusion

This assignment demonstrated how Maximum Likelihood Estimation can be used to estimate the parameter of a Poisson distribution.

The estimated traffic intensity was approximately 12.14 vehicles per minute.

The analysis also highlighted the sensitivity of MLE to outliers, emphasizing the importance of data validation before using statistical models for real-world decision making.

