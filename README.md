# Main Research Focus
The main focus of the research is to determine the specific type of attacks that result in the highest success and/or casualty rates. Because of the high number of categorical variables, an analysis dealing with discrete probabilities would be really effective. On a conceptual level, I would like to pinpoint the exact combinations that grant the maximum success/casualty rates using some form of optimization. 

## Methods
I will be implementing a [[Logistic Regression]] model as well as a [[Poisson Regression]] model and a Zero Inflated Poisson Regression model. The Logistic Regression model will determine the probability of an attack being successful using a linear combination of multiple independent variables. The Zero Inflated Poisson model will determine the probability distribution of casualty counts. It takes into account the significant number of zeros present in the 'nkill' variable.

This analysis will focus on comparing and contrasting three components of Operation Enduring Freedom (OEF). Each component represents an Area of Operations that is focused on combatting terrorism within select countries. This allows me to compare how terrorist attacks differ according to geography, group structure, and political situations. 

As an initial step, I have found the joint probabilities of variable combinations (sum to 1). I can then aggregate those specific combinations with success or casualties. It would require an optimization model to find the combinations (potentially hundreds of millions) with maximum success/casualty rates. With these results, I would be able to confidently argue which areas of counterterrorism measures are needed most, and which measures are not worth budgeting for. 

Final goal could be to build a Bayesian Network based on the foundational framework laid by a logistic regression and Poisson model.

## Task List
- **Compute the accuracy of my models (confusion matrix + model validation metrics).**
- Accumulate sources to explain why attack success is more volatile in the Philippines than the Horn of Africa.
- I can analyze the linear combinations with predicted probabilities of 90%> and <10% to find trends, differences, etc.
	- I can then plot attacks by associated predicted probability. (e.g. attacks with +95% probability of success color-coded by some variable.)
- Build a more accurate model using ROC Curve, Accuracy Matrix, Residuals (analyze unique combinations), DF Beta (Influence).

## Research Progress
- I have created three subsets of data which represent three seperate components of Operation Enduring Freedom (specific mission as a part of the War on Terror). The subsets total 22,506 events. The subsets are:
	- OEF-P Philippines (Operation Freedom Eagle), 6,101 attacks
	- OEF-TS Trans Sahara (Operation Juniper Shield), 9,328 attacks
	- OEF-HOA Horn of Africa, 7,077 attacks
- I have examined univariate statistics on all of the variables in each subset.
-  I have organized the terrorist groups ("gname" variable) into more generalized groups in order to create a more accurate Logistic Regression model.
- I have created a High Performance Logistic Regression model that predicts whether the attack will be successful or not. 
	- Predicted probabilities for each subset have been exported into three CSV files.
	- I have created a tables that includes all of the coefficient estimates, standard errors, Degrees of Freedom, t values, p-values, and calculated odds.
- I have created bar charts examining the distributions of attacks with a predicted probability of 95% or greater. These can be used to determine similarities/differences in the success of varying components of a terrorist attack in three separate regions of the world.
- I have imported all necessary shapefiles, and plotted all attack coordinates for each component of Operation Enduring Freedom.

## Difficulties
- I am unsure of the key differences between the SAS Logistic Procedure and the SAS HPLogistic Procedure.
- The predicted probabilities potentially have quite a bit of uncertainty, and would be accurate when describing them as confidence intervals.

## Problems Solved
- Why is the Degrees of Freedom for all variable levels in the Logistic Regression model infinite?
		- This is the default option for the HPLOGISTIC procedure in SAS, using the z distribution. Setting the DDFM model option to DDFM=RESIDUAL sets the DF to a finite value allowing the use of a t distibution. The two methods are almost identical when using a large sample.

## Background
For background information, refer to [Mapping Militants](https://cisac.fsi.stanford.edu/mappingmilitants). This website includes background information on most Islamic State terrorist cells in the world. 

##### OEF-P Notes:
On September 1, 2017 Secretary of Defense James Mattis designated Operation Pacific Eagle - Philippines as a contingency operation, serving as a continuation of Operation Freedom Eagle. *Page 98 of DOD Operation Pacific Eagle Report (PDF).*
The operation mainly consisted of training the Armed Forces of the Philippines in counter-terrorism operations as well as supporting humanitarian aid.
- Only 15 out of 6101 terrorist attacks in the Philippines were suicide attacks.

Generalized groups consist of the following: 
- New People's Army (NPA): Armed wing of the Communist Party of the Philippines.
- Islamic Extremists: Groups following a form of Islamic jihadism.
- Moro Insurgents: Muslim-majority armed groups focused on establishing independent state in the Philippines.
- Unknown: Groups with ambiguous names, or groups that lacked any reference online.

##### OEF-HOA Notes:
Generalized groups consist of the following: 
- Islamic Extremists: Groups following a form of Islamic jihadism.
- Regional Militias/Tribes: Ethnic, rebel, or insurgency groups focused on regional interests, such as competing for territory, money, or political power.
- Political Organization: Groups that are formally recognized political parties.
- Unknown: Groups with ambiguous names, or groups that lacked any reference online.

##### OEF-TS Notes:
The Trans-Sahara Counterterrorism Partnership (TSCTP) is the central U.S. interagency plan to combat terrorism in Trans-Saharan Africa. OEF-TS is the military combat component of TSCTP. Its predecessor is the Pan Sahel Initiative, focusing on Mali, Niger, Chad, and Mauritania as an initial component of the War on Terrorism beginning in 2002. 
*Countries that OEF-TS explicitly focuses on are stated on page 48 of DOD 2019 Budget (PDF).*

- Maghreb: Algeria, Morocco, Tunisia
- Sub-Sahara: Burkina Faso, Cameroon, Chad, Mali, Mauritania, Niger, Nigeria, Senegal

Generalized groups consist of the following: 
- Islamic Extremists: Groups following a form of Islamic jihadism.
- Al-Qaida in the Islamic Maghreb (AQIM): Merged with its formally recognized name used prior to 2007. A significant number of attacks were carried out by this group alone.
- Regional Militias/Tribes: Ethnic, rebel, or insurgency groups focused on regional interests, such as competing for territory, money, or political power.
- Unknown: Groups with ambiguous names, or groups that lacked any reference online.


## Results
- Intepretations: 
	- Nearly 50% of attacks with an extremely high predicted chance of success (95%) are kidnappings in the Philippines.
	- Approximately 90% of attacks with a predicted probability of success greater than 95% are located inside a city rather on the outskirts of a city for all three regions analyzed.
	- Over 95% of attacks with an extremely high predicted probability of success (95%) are non-suicide attacks for the Horn of Africa, Trans-Sahara, and Philippines mission components.


## Further Notes
**_This means if the probability of an event happening is >0.5 we usually consider the event to happen or in other words if the chances of an event happening are more than 50% then we can claim that the event will take place, i.e., in this case, it will rain._**

Add 2 digit labels to bar charts.
Make bars wider.
Raise font size.
Put x axis label in all caps.
Change labels



Will remove the Unknown level from final results of the summary analysis of attacks with <= 95% predicted success chance due to there being no relevant insights gained from it. (Also removed "Other" in Weapon Types for the same reason).
