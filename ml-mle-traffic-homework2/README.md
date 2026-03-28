# Machine Learning Homework

## Maximum Likelihood Estimation for Traffic Modeling

This project models the number of cars passing through a busy city street using the Poisson distribution.

The goal is to estimate the traffic intensity parameter λ using Maximum Likelihood Estimation (MLE).

## Dataset

Observed traffic counts (vehicles per minute):

12, 15, 10, 8, 14, 11, 13, 16, 9, 12, 11, 14, 10, 15

## Method

The Poisson distribution is used to model the traffic flow.
The parameter λ represents the expected number of cars per minute.

Using Maximum Likelihood Estimation:

λ̂ = (1/n) Σ kᵢ

Therefore, the MLE estimate for a Poisson distribution equals the **sample mean**.

## Result

λ ≈ 12.14 cars per minute.

Both analytical derivation and numerical optimization in Python produce the same result.

## Repository Structure

code/ → Python implementation

data/ → dataset used in analysis

report/ → theoretical derivation and discussion

results/ → interpretation of results

## Key Insight

The Poisson MLE estimator equals the sample mean because the derivative of the log-likelihood function leads to:

λ̂ = (1/n) Σ kᵢ

This demonstrates that Maximum Likelihood Estimation for the Poisson parameter is simply the average of the observed data.

Author: QUNOO A K TAWEEL

Course: Machine Learning

Year: 2025–2026
