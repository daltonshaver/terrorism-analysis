# Logistic Regression
## Overview
Logistic Regression (also known as a Logit model) estimates the probability of an event occurring based on given independent variables. It is a classification model, not a regression model. The probability is bounded between 0 and 1.

## How it Works
Logistic Regression is alternate form of linear regression. The logit function is applied to the probability (between 0 and 1) of the dependent variable. It is defined as the logarithm of the odds ratio (or log-odds).

Logit(p) = log(odds) = log(p/(1-p)) = Ln(p/(1-p))

The weights of independent variables in the model are represented as log-odds. The usual probability graph associated with Logistic Regression is transformed to an infinite cartesian plane when the Logit function is applied (thus it just becomes regression).

Classification value 0 (unsuccessful attack) is class one. Classification value 1 (successful attack) is class two.

## Interpretation
**Analysis ran on 09/01:**
The test is significant (p-value < 0.001), thus one or more of the model effects significant affects the probability of observing an unsuccessful terrorist attack.

## Implementation
See [[001 Terrorism Research#Research Progress |Research Progress]]. 
