# Logistic Regression
## Overview
Logistic Regression (also known as a Logit model) estimates the probability of an event occurring based on given independent variables. It is a classification model, not a regression model. The probability is bounded between 0 and 1.

## How it Works
Logistic Regression is alternate form of linear regression. The logit function is applied to the probability (between 0 and 1) of the dependent variable. It is defined as the logarithm of the odds ratio (or log-odds).

Logit(p) = log(odds) = log(p/(1-p)) = Ln(p/(1-p))

The weights of independent variables in the model are represented as log-odds. The usual probability graph associated with Logistic Regression is transformed to an infinite cartesian plane when the Logit function is applied (thus it just becomes regression).

Ln(p/1-p) = B0 + B1x + B2x where the B coefficients are either 0 or 1 for categorical variables.

The odds ratio is the is odds of the variable level divided by the odds of the reference level. The linear combination of B coefficients are then exponentiated, and divided by the two levels. This results in e raised to the power of whichever coefficients are 1.
Example: If the terrorist group is targeting a business, the odds of success to failure are double the odds of success to failure of targeting a political party. (If the resulting value is 2).

## SAS HPLOGISTIC Degrees of Freedom
DDFM=RESIDUAL | NONE specifies how degrees of freedom for statistical inference be determined in the “Parameter Estimates Table.” The HPLOGISTIC procedure always displays the statistical tests and confidence intervals in the “Parameter Estimates” tables in terms of a t test and a two-sided probability from a t distribution. With the DDFM= option, you can control the degrees of freedom of this t distribution and thereby switch between small-sample inference and large-sample inference based on the normal or chi-square distribution. The default is DDFM=NONE, which leads to z-based statistical tests and confidence intervals. The HPLOGISTIC procedure then displays the degrees of freedom in the DF column as Infty, the p-values are identical to those from a Wald chi-square test, and the square of the t value equals the Wald chi-square statistic. If you specify DDFM=RESIDUAL, the degrees of freedom are finite and determined by the number of usable frequencies (observations) minus the number of nonredundant model parameters. This leads to t-based statistical tests and confidence intervals. If the number of frequencies is large relative to the number of parameters, the inferences from the two degrees-of-freedom methods are almost identical.

#### Tooltip
If you specify DDFM=RESIDUAL, the degrees of freedom are finite and determined by the number of usable frequencies (observations) minus the number of nonredundant model parameters. This leads to t-based statistical tests and confidence intervals. **If the number of frequencies is large relative to the number of parameters, the inferences from the two degrees-of-freedom methods are almost identical.**


Page 4257

## Current ideas & thinking
- Why take out variable levels with very few unsuccessful attacks? My research goal is to understand which linear combinations have the highest probability of success (as well as the lowest).


## Reference Level Strategies
Ultimately, which reference levels I choose do not matter, the analysis is always the same. Although, the specific output, such as estimates and p-values will change dependent on the reference.
- Use the "normative" category: Choose the level that is the most logical and easiest to intepret.
- Use the largest category: Choose the level with the highest frequency count.
Source: https://www.theanalysisfactor.com/strategies-dummy-coding/

#### Reference Levels
All OEF
- gname = "Islamic Extremists"
- attacktype1 = "Bombing/Explosion"
- targtype1 = "Private Citizens & Property"
- weaptype1 = "Explosives"

OEF-HOA
- country = "Somalia"

OEF-TS
- country = "Nigeria"


## Interpretation
The test is significant (p-value < 0.001), thus one or more of the model effects significantly affects the probability of observing an unsuccessful terrorist attack.

**Examples:**
- The odds of an attack being successful when a suicide bomber is involved is 1.43 times greater than the odds of a terrorist attack being successful without a suicide attack.
- The odds of an attack being successful when it occurs in the outskirts of a city is 1.05 times greater than the odds of a terrorist attack being successful inside the city.
- The odds of success for the Abu Sayyaf Group (ASG) is 60.21% of the odds of success for Islamic Extremists.

## Implementation
See [[001 Terrorism Research#Research Progress |Research Progress]]. 

## Notes
Justify of the ones actually successful, what were the traits?
Narrowing down the best ones (95%)


Make a legend (with two datasets and surrounding countries)

Stratified ROC Curves
6 Multiple

6 Predictor Variables
