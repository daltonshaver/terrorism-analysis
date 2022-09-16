# Main Research Focus
The main focus of the research is to determine the specific type of attacks that result in the highest success and/or casualty rates. Because of the high number of categorical variables, an analysis dealing with discrete probabilities would be really effective. On a conceptual level, I would like to pinpoint the exact combinations that grant the maximum success/casualty rates using some form of optimization. 

## Methods
I will be implementing a [[Logistic Regression]] model as well as a [[Poisson Regression]] model and a Zero Inflated Poisson Regression model. The Logistic Regression model will determine the probability of an attack being successful using a linear combination of multiple independent variables. The Zero Inflated Poisson model will determine the probability distribution of casualty counts. It takes into account the significant number of zeros present in the 'nkill' variable.

This analysis will focus on comparing and contrasting three components of Operation Enduring Freedom (OEF). Each component represents an Area of Operations that is focused on combatting terrorism within select countries. This allows me to compare how terrorist attacks differ according to geography, group structure, and political situations. 

As an initial step, I have found the joint probabilities of variable combinations (sum to 1). I can then aggregate those specific combinations with success or casualties. It would require an optimization model to find the combinations (potentially hundreds of millions) with maximum success/casualty rates. With these results, I would be able to confidently argue which areas of counterterrorism measures are needed most, and which measures are not worth budgeting for. 

Final goal could be to build a Bayesian Network based on the foundational framework laid by a logistic regression and Poisson model.

## Task List
- Plot attack coordinates using Geopandas. 
- Accumulate sources to explain why attack success is more volatile in the Philippines than the Horn of Africa.
- I can analyze the linear combinations with predicted probabilities of 90%> and <10% to find trends, differences, etc.
- Build a more accurate model using ROC Curve, Accuracy Matrix, Residuals (analyze unique combinations), DF Beta (Influence).

## Research Progress
- I have created three subsets of data which represent three seperate components of Operation Enduring Freedom (specific mission as a part of the War on Terror). The subsets total 22,507 events. The subsets are:
	- OEF-P Philippines (Operation Freedom Eagle)
	- OEF-TS Trans Sahara (Operation Juniper Shield)
	- OEF-HOA Horn of Africa
- I have begun to examine univariate statistics on all of the variables in each subset.
- I have created a table of all possible variable combinations and the associated success rate, attack frequency, mean casualties, and total casualties. Using this table, I can determine which specific types of attacks have the highest success/casualty rates. 
- I have created a High Performance Logistic Regression model that predicts whether the attack will be successful or not. 
	- Predicted probabilities for each subset have been exported into three CSV files.
	- I have created a table that includes all of the variable levels that are significant (a=0.05) in the model, as well as their associated p-values.
- I have organized the terrorist groups ("gname" variable) into more generalized groups in order to create a more accurate Logistic Regression model.

## Difficulties
- I am unsure of the key differences between the SAS Logistic Procedure and the SAS HPLogistic Procedure.

## Background
For background information, refer to [Mapping Militants](https://cisac.fsi.stanford.edu/mappingmilitants). This website includes background information on most Islamic State terrorist cells in the world. 

##### OEF-P Notes:
On September 1, 2017 Secretary of Defense James Mattis designated Operation Pacific Eagle - Philippines as a contingency operation, serving as a continuation of Operation Freedom Eagle. *Page 98 of DOD Operation Pacific Eagle Report (PDF).*
The operation mainly consisted of training the Armed Forces of the Philippines in counter-terrorism operations as well as supporting humanitarian aid.

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
