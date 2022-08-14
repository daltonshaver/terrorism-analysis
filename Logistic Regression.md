# Logistic Regression
## Overview
Logistic Regression (also known as a Logit model) estimates the probability of an event occurring based on given independent variables. It is a classification model, not a regression model. The probability is bounded between 0 and 1.

## How it Works
Logistic Regression is alternate form of linear regression. The logit function is applied to the probability (between 0 and 1) of the dependent variable. It is defined as the logarithm of the odds ratio (or log-odds).

Logit(p) = log(odds) = log(p/(1-p))

The weights of independent variables in the model are represented as log-odds. The usual probability graph associated with Logistic Regression is transformed to an infinite cartesian plane when the Logit function is applied (thus it just becomes regression).

## Implementation
I will code in two Logistic Regression models using two seperate Python packages, statsmodel and sklearn. Then I will compare the results (optimization). I must determine whether to use forward propogation or backward propogation to optimize my model.