# Main Research Focus
The main focus of the research is to determine the specific type of attacks that result in the highest success and/or casualty rates. Because of the high number of categorical variables, an analysis dealing with discrete probabilities would be really effective. On a conceptual level, I would like to pinpoint the exact combinations that grant the maximum success/casualty rates using some form of optimization. 

## Methods
I will be implementing a [[Logistic Regression]] model as well as a [[Poisson Regression]] model and a Zero Inflated Poisson Regression model. The Logistic Regression model will determine the probability of an attack being successful using a linear combination of multiple independent variables. The Zero Inflated Poisson model will determine the probability distribution of casualty counts. It takes into account the significant number of zeros present in the 'nkill' variable.

This analysis will focus on comparing and contrasting three components of Operation Enduring Freedom (OEF). Each component represents an Area of Operations that is focused on combatting terrorism within select countries. This allows me to compare how terrorist attacks differ according to geography, group structure, and political situations. 

As an initial step, I have found the joint probabilities of variable combinations (sum to 1). I can then aggregate those specific combinations with success or casualties. It would require an optimization model to find the combinations (potentially hundreds of millions) with maximum success/casualty rates. With these results, I would be able to confidently argue which areas of counterterrorism measures are needed most, and which measures are not worth budgeting for. 

Final goal could be to build a Bayesian Network based on the foundational framework laid by a logistic regression and Poisson model.

## Potential Methods
Additional analysis methods can include adding in graphical maps. The can serve as a better representation of the attacks, potentially showing the most dangerous attacks in a different color. (Most dangerous: type of attack with the highest casualty rates). 

I can plot the attack coordinates on individual countries (similar to previous research). I can create a density plot by setting the alpha parameter below 1 in the scatterplot.

I can create a QQ Plot for certain numerical variables.

## Progress
- I have created three subsets of data which represent three seperate components of Operation Enduring Freedom (specific mission as a part of the War on Terror). The subsets total 22,507 events. The subsets are:
	- OEF-P Philippines (Operation Freedom Eagle)
	- OEF-TS Trans Sahara (Operation Juniper Shield)
	- OEF-HOA Horn of Africa
- I have begun to examine univariate statistics on all of the variables in each subset.
- I have created a table of all possible variable combinations and the associated success rate, attack frequency, mean casualties, and total casualties. Using this table, I can determine which specific types of attacks have the highest success/casualty rates. 
- I have created a Logistic Regression model that predicts whether the attack will be successful or not. The highest accuracy score I have achieved is 87%. The model struggles to pick out unsuccessful attacks. 

## Difficulties
- While I can I build a Logistic Regression model that can predict successful attacks accurately, what method should I use to analyze the specific feature combinations that pose the highest probability of success?

## Background
For background information, refer to [Mapping Militants](https://cisac.fsi.stanford.edu/mappingmilitants). This website includes background information on most Islamic State terrorist cells in the world. 

##### OEF-P Notes:
On September 1, 2017 Secretary of Defense James Mattis designated Operation Pacific Eagle - Philippines as a contingency operation, serving as a continuation of Operation Freedom Eagle. *Page 98 of DOD Operation Pacific Eagle Report (PDF).*

##### OEF-TS Notes:
The Trans-Sahara Counterterrorism Partnership (TSCTP) is the central U.S. interagency plan to combat terrorism in Trans-Saharan Africa. OEF-TS is the military combat component of TSCTP. Its predecessor is the Pan Sahel Initiative, focusing on Mali, Niger, Chad, and Mauritania as an initial component of the War on Terrorism beginning in 2002. 
*Countries that OEF-TS explicitly focuses on are stated on page 48 of DOD 2019 Budget (PDF).*

- Maghreb: Algeria, Morocco, Tunisia
- Sub-Sahara: Burkina Faso, Cameroon, Chad, Mali, Mauritania, Niger, Nigeria, Senegal
