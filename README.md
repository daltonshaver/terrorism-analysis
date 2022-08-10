# Main Research Focus
The main focus of the research is to determine the specific type of attacks that result in the highest success and/or casualty rates. Because of the high number of categorical variables, an analysis dealing with discrete probabilities would be really effective. On a conceptual level, I would like to pinpoint the exact combinations that grant the maximum success/casualty rates using some form of optimization. 

## Methods
I will be implementing a Multiple Logistic Regression model as well as a Zero Inflated Poisson model. The Logistic Regression model will determine the probability of an attack being successful using a linear combination of multiple independent variables. The Zero Inflated Poisson model will determine the probability distribution of casualty counts. It takes into account the significant number of zeros present in the 'nkill' variable.

As an initial step, I have found the joint probabilities of variable combinations (sum to 1). I can then aggregate those specific combinations with success or casualties. It would require an optimization model to find the combinations (potentially hundreds of millions) with maximum success/casualty rates. With these results, I would be able to confidently argue which areas of counterterrorism measures are needed most, and which measures are not worth budgeting for. 

Final goal could be to build a [[Bayesian Network]] based on the foundational framework laid by a logistic regression and Poisson model.

## Potential Methods
Additional analysis methods can include adding in graphical maps. The can serve as a better representation of the attacks, tentially showing the most dangerous attacks in a different color. (Most dangerous: type of attack with the highest casualty rates). Potentially may create a subset of the database to only include attacks linked to Islamic State in the countries Iraq, Nigeria, and the Philippines. These are three countries in very different regions of the world, with differing IS groups operating within them. 

*Can use statsmodel package in Python.*
