# OPERATION ENDURING FREEDOM: Improving Mission Effectiveness by Identifying Trends in Successful Terrorism

## Abstract
This research examines how the characteristics of terrorist attacks predict the chance of an attack succeeding, where an attack is defined as successful if the intended attack type is carried out. Data from The Global Terrorism Database was analyzed across three geographical missions within Operation Enduring Freedom: Trans-Sahara, Horn of Africa, and the Philippines. The three models were able to distinguish between successful and unsuccessful attacks at 78.74%, 82.11%, 74.25%, respectively. Using predicted probabilities of success obtained from each logistic regression model, the medians were plotted to compare the characteristics of terrorist attacks across missions. The coefficients for each model were analyzed to compare the odds of success for each variable level to the odds of success of the reference level for that variable. The coordinates for successful and unsuccessful attacks as classified by the dataset were plotted to explore spatial patterns in regional maps. Many insights were gathered through analyzing Operation Enduring Freedom missions. For all three Operation Enduring Freedom missions, attacks involving Barricade Incidents, Unarmed Assaults, Infrastructure Attacks, and Incendiary weapons are predicted to have the highest probability of success. Additionally, the two most prevalent regional ethnic groups in the Trans-Sahara and Horn of Africa have higher predicted probabilities compared to jihadist organizations, in contrast to the Philippines, where attacks by Islamic Extremists have the highest probability of succeeding. Furthermore, attacks targeting private citizens, tourists, non-governmental organizations, and food or water supply, have the largest probability of success for the Trans-Sahara and Horn of Africa regions, whereas suicide attacks in the Philippines raise the chance of success. By determining the specific characteristics of attacks that produce the highest probabilities of success, the effectiveness of Operation Enduring Freedom can be improved by focusing counter-terrorism training and operations on the features that predict successful attacks.

## Why do we care?
By determining the type of attacks that result in the highest success rate, partner nations can focus training and operations on responding and preventing terrorist attacks that are most likely to occur. Some of these terrorist groups maintain "de facto control significant portions of the country, particularly in south-central Somalia, continuing to move freely, collect “taxes,” and exert governing authority in the areas under its control" (US Department of State Country Report 2019 Somalia). In Somolia, UN and other agencies cannot deliver aid and food to region because of terrorist groups blockading routes.

There is a key difference in how people picture terrorism; Many of these countries are currently battling terrorists and militants on the ground in conventional combat over the country's territory and resources. An important theme I have seen while reading sources is that there is a severe lack of military competence among partner nations in West and East Africa. Many forces do not have the capability to effectively fight these terrorist groups as they are often riddled with corruption (Warner, CNA Capacity Building Publication). Counterterrorism efforts such as "... basic infantry and special forces skills (i.e., marksmanship, communications, first aid, vehicle maintenance, air mobility, ground mobility, raids, closequarters battle, long-range reconnaissance, and hostage rescue)" can be directly improved by providing actionable intelligence to these units. 

Insights -> Training -> Increased Mission Effectiveness

"Effective counter-terrorism strategies must be risk-based, intelligence-driven and comprehensive, employing all elements and aspects of national and international security functions, measures and operations" (NATO Counter-Terrorism Reference Curriculum 2020, p. 95).

## Methods
This analysis will focus on comparing and contrasting three components of Operation Enduring Freedom (OEF). Each component represents an Area of Operations that is focused on combatting terrorism within select countries. This allows me to compare which features of terrorist attacks are most successful according to geography.

I will be implementing a [[Logistic Regression]] model. The Logistic Regression model will predict whether an attack was either successful or unsuccessful based on the predictor variables *suicide*, *vicinity*, *gname*, *attacktype1*, *targtype1*, *weaptype1*, and *country*. I will also use the associated predicted probabilities for each observation determined from the Logistic Regression model. Using stratified point plots, I will examine the predicted probabilities of each individual attack feature and compare and contrast these by mission area. 

Further research may involve a Zero Inflated [[Poisson Regression]] model. This model could determine the probability distribution of casualty counts. It takes into account the significant number of zeros present in the 'nkill' variable.

## Research Progress
- I have created three subsets of data which represent three seperate components of Operation Enduring Freedom (specific mission as a part of the War on Terror). The subsets total 22,506 events. The subsets are:
	- OEF-P Philippines (Operation Freedom Eagle), 6,101 attacks
	- OEF-TS Trans Sahara (Operation Juniper Shield), 9,328 attacks
	- OEF-HOA Horn of Africa, 7,077 attacks
- I have examined univariate statistics on all of the variables in each subset.
-  I have organized the terrorist groups ("gname" variable) into more generalized groups in order to create a more accurate Logistic Regression model.
- I have created a High Performance Logistic Regression model that predicts whether the attack will be successful or unsuccessful. 
	- Predicted probabilities for each subset have been exported into three CSV files.
	- I have created a tables that includes all of the coefficient estimates, standard errors, Degrees of Freedom, t values, p-values, and calculated odds.
- I have created bar charts examining the **distributions of attacks with a predicted probability of 95% or greater**. These can be used to determine similarities/differences in the success of varying components of a terrorist attack in three separate regions of the world.
- I have created two maps (Africa, Philippines) displaying the geographic distribution of attacks, colored by success.
- I have created a graphic showing the ROC-AUC Curves stratified by mission.
- I have used point plots stratified by OEF mission to display median predicted probabilities of success for each variable level.
- I have drawn conclusion based on the median predicted probabilities as to which characteristics of terrorist attacks are most likely to predict a successful attack.

## Problems Solved
- Why is the Degrees of Freedom for all variable levels in the Logistic Regression model infinite?
		- This is the default option for the HPLOGISTIC procedure in SAS, using the z distribution. Setting the DDFM model option to DDFM=RESIDUAL sets the DF to a finite value allowing the use of a t distibution. The two methods are almost identical when using a large sample.

## Background

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

For background information, refer to [Mapping Militants](https://cisac.fsi.stanford.edu/mappingmilitants). This website includes background information on most Islamic State terrorist cells in the world. 

## Notes
- 10/21: Multiple people killed and kidnapped at a hospital in Nigeria by militants.
- 10/30: "At least 100 people were killed in the car bomb attacks in Somalia's capital" (NPR Document in Google Drive)

I removed the Unknown levels from final results of the analysis of attacks due to there being no relevant insights gained from it. I also removed "Other" in Weapon Types for the same reason.

Interpretations:
- 50% of the philippines suicide have over 83% predicted probability of success, 
- 50% of the philippines attack that use suicide have there chance of success being over 92%. 
- There is a ...% chance that the model will be able to distinguish between successful attacks and unsuccessful attacks.
- I can conclude that changes in the characteristics of an attack are associated with changes in the probability that the attack is successful.

## Flash Presentation:
**"Terrorists aim to terrorize."**
- Use maps.
- "Join me..."
- Include variables that I am using to predict success.

