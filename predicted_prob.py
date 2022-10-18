import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns

#Loading in all three datasets.
oef_hoa = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\oef_hoa.csv')
oef_p = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\oef_p.csv')
oef_ts = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\oef_ts.csv')

#Loading in newly created probability datasets.
prob_hoa = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\prob_hoa.csv')
prob_p = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\prob_p.csv')
prob_ts = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\prob_ts.csv')

#Dropping the unneeded logistic output columns.
prob_hoa = prob_hoa.drop(columns=["eventid", "_POST_", "Residual", "Pearson", "Xbeta", "_ROLE_"])
prob_p = prob_p.drop(columns=["eventid", "_POST_", "Residual", "Pearson", "Xbeta", "_ROLE_"])
prob_ts = prob_ts.drop(columns=["eventid", "_POST_", "Residual", "Pearson", "Xbeta", "_ROLE_"])

#Examining combinations with a predicted probability of 95% or greater.
prob_hoa95 = prob_hoa.loc[(prob_hoa.Pred >= 0.95) & (prob_hoa.success == 1)]
prob_p95 = prob_p.loc[(prob_p.Pred >= 0.95) & (prob_hoa.success == 1)]
prob_ts95 = prob_ts.loc[(prob_ts.Pred >= 0.95) & (prob_hoa.success == 1)]

#Appending the three regional datasets into one dataset.
prob_hoa95["mission"] = "HOA"
prob_p95["mission"] = "Philippines"
prob_ts95["mission"] = "Trans-Sahara"
prob95_grouped = prob_hoa95.append([prob_p95, prob_ts95])

#Replacing variable level names with more concise names.
prob95_grouped = prob95_grouped.replace(['Bombing/Explosion', 'Facility/Infrastructure Attack', 'Hostage Taking (Barricade Incident)', 
                                         'Hostage Taking (Kidnapping)'], 
                                        ['Bombing', 'Facility/Infrastructure', 'Hostage (Barricade)', 'Hostage (Kidnapping)'])

#Examining the number of correctly predicted successful terrorist attacks.
prob_hoa95.success.mean() #97.0% Correctly classified.
prob_p95.success.mean()   #98.6% Correctly classified.
prob_ts95.success.mean()  #97.2% Correctly classified.

#The four plots to compare frequency of predictor variables. Need to include suicide and vicinity.
def probBarchart(dataset, color_input):
    edgecolor_input = "black"
    label_font = 12
    figure_sizex = 10
    figure_sizey = 10
    
    plt.figure(figsize=(figure_sizex,figure_sizey), tight_layout=False)
    p1 = plt.bar(dataset['suicide'].value_counts().index, dataset['suicide'].value_counts(), edgecolor=edgecolor_input, color=color_input)
    plt.xticks(rotation=90)
    plt.bar_label(p1, padding=2, fontsize=label_font)
    plt.title("Barchart of Suicide Attacks")

    plt.figure(figsize=(figure_sizex,figure_sizey), tight_layout=True)
    p1 = plt.bar(dataset['vicinity'].value_counts().index, dataset['vicinity'].value_counts(), edgecolor=edgecolor_input, color=color_input)
    plt.xticks(rotation=90)
    plt.bar_label(p1, padding=2, fontsize=label_font)
    plt.title("Barchart of Vicinity")

    
    plt.figure(figsize=(figure_sizex,figure_sizey), tight_layout=True)
    p1 = plt.bar(dataset['gname'].value_counts().index, dataset['gname'].value_counts(), edgecolor=edgecolor_input, color=color_input)
    plt.xticks(rotation=90)
    plt.bar_label(p1, padding=2, fontsize=label_font)
    plt.title("Barchart of Terrorist Groups")
    
    plt.figure(figsize=(figure_sizex,figure_sizey), tight_layout=True)
    p1 = plt.bar(dataset['attacktype1'].value_counts().index, dataset['attacktype1'].value_counts(), edgecolor=edgecolor_input, color=color_input)
    plt.xticks(rotation=90)
    plt.bar_label(p1, padding=2, fontsize=label_font)
    plt.title("Barchart of Attack Types")
    
    plt.figure(figsize=(figure_sizex,figure_sizey), tight_layout=True)
    p1 = plt.bar(dataset['targtype1'].value_counts().index, dataset['targtype1'].value_counts(), edgecolor=edgecolor_input, color=color_input)
    plt.xticks(rotation=90)
    plt.bar_label(p1, padding=2, fontsize=label_font)
    plt.title("Barchart of Target Types")
    
    plt.figure(figsize=(figure_sizex,figure_sizey), tight_layout=True)
    p1 = plt.bar(dataset['weaptype1'].value_counts().index, dataset['weaptype1'].value_counts(), edgecolor=edgecolor_input, color=color_input)
    plt.xticks(rotation=90)
    plt.bar_label(p1, padding=2, fontsize=label_font)
    plt.title("Barchart of Weapon Types")
    
    return()

probBarchart(prob_hoa95, "#EBE4A9")
probBarchart(prob_p95, "#1D3C45")
probBarchart(prob_ts95, "#D2601A")

#Grouped bar charts to compare similarities/differences for components of successful terrorism between regions.
def groupBarCharts(var, title, xlab, ylab):

    table = pd.crosstab(prob95_grouped[var], prob95_grouped['mission'])
    x = np.arange(start=0, stop=2*len(table.index), step=2)
    
    #Converting columns to relative frequencies.
    table['HOA'] = table['HOA'] / table['HOA'].sum()
    table['Philippines'] = table['Philippines'] / table['Philippines'].sum()
    table['Trans-Sahara'] = table['Trans-Sahara'] / table['Trans-Sahara'].sum()
    
    if var == 'attacktype1':
        table = table.drop(index="Unknown")
        x = np.arange(start=0, stop=2*len(table.index), step=2)
    elif var == 'weaptype1':
        table = table.drop(index=["Unknown", "Other"])
        x = np.arange(start=0, stop=2*len(table.index), step=2)
    
    if var == 'targtype1':
        table = table.loc[(table.index == "Business") | 
                          (table.index == "Government (General)") | 
                          (table.index == "Military") | 
                          (table.index == "Police") | 
                          (table.index == "Educational Institution") |
                          (table.index == "Private Citizens & Property")]
        x = np.arange(start=0, stop=2*len(table.index), step=2)
            #Manually choosing to only display the top 6 levels of targets.
            #Need to merge the excluded levels into an 'other' category. *****
    
    fig, ax = plt.subplots(1, figsize=(18,14))
    plt.bar(x - 0.4, table['HOA'], width=0.4, color='#EBE4A9')
    plt.bar(x + 0.0, table['Philippines'], width=0.4, color='#7CA5BE')
    plt.bar(x + 0.4, table['Trans-Sahara'], width=0.4, color='#F3BE9E')
    ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.3)
    plt.xticks(x, table.index, rotation=45, fontsize=12)
    plt.title(title, fontsize=18)
    plt.xlabel(xlab, fontsize=14)
    plt.ylabel(ylab, fontsize=14)
    
    if var == 'targtype1':
        plt.legend(['HOA', 'Philippines', 'Trans-Sahara'], loc='upper left', ncol=3, fontsize=16)
    else:
        plt.legend(['HOA', 'Philippines', 'Trans-Sahara'], loc='upper right', ncol=3, fontsize=16)
    
    for bars in ax.containers:
        ax.bar_label(bars, fmt='%.2f', fontsize=12)
    
    return()

groupBarCharts('suicide', "Suicide Attacks by Mission of Terrorist Attacks with a Predicted Probability of Success <= 95%",
               "SUICIDE INDICATOR", "Percentage")
groupBarCharts('vicinity', "Vicinity of City by Mission of Terrorist Attacks with a Predicted Probability of Success <= 95%",
               "IN THE CITY INDICATOR", "Percentage")
groupBarCharts('attacktype1', "Attack Type by Mission of Terrorist Attacks with a Predicted Probability of Success <= 95%",
               "ATTACK TYPE", "Percentage") 
groupBarCharts('targtype1', "Target Type by Mission of Terrorist Attacks with a Predicted Probability of Success <= 95%",
               "TARGET TYPE", "Percentage")
groupBarCharts('weaptype1', "Weapon Type by Mission of Terrorist Attacks with a Predicted Probability of Success <= 95%",
               "WEAPON TYPE", "Percentage")




#Plot differently
groupBarCharts('gname')
#groupBarChartCountry()

def groupBarChartCountry():

    grouped_df = prob95_grouped.loc[(prob95_grouped.mission == "HOA") | (prob95_grouped.mission == "Trans-Sahara")]
    
    table = pd.crosstab(grouped_df['country'], grouped_df['mission'])
    x = np.arange(0, len(table.index))
    table['HOA'] = table['HOA'] / table['HOA'].sum()
    table['Trans-Sahara'] = table['Trans-Sahara'] / table['Trans-Sahara'].sum()
    
    fig, ax = plt.subplots(1, figsize=(18,14))
    plt.bar(x - 0.1, table['HOA'], width = 0.2, color ='#EBE4A9')
    plt.bar(x + 0.1, table['Trans-Sahara'], width = 0.2, color ='#D2601A')
    plt.xticks(x, table.index, rotation=90)
    ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.2)
    plt.legend(['HOA', 'Trans-Sahara'], loc='upper right', ncol=2)

    return()


























#(Philippines) While armed assualts and bombings are more frequent, nearly 50% of unique attacks with a predicted probability of 95% or greater involve kidnappings.
#(Philippines) The analysis indicates private citizens are more susceptible to possible successful terrorist attacks than any other target type.






#Checking to make sure the original dataset (oef_p) and the predicted probability dataset (prob_p) 
#have the same number of unique combination for predictor variables.
oef_p = oef_p.drop(columns=['eventid', 'year', 'month', 'day', 'country', 'region', 'provstate',
       'city', 'latitude', 'longitude', 'specificity',
       'attacktype2', 'attacktype3',
       'targsubtype1', 'corp1', 'target1', 'natlty1', 'gsubname',
       'nperps', 'nperpcap', 'claimed', 'weapsubtype1', 'nkill',
       'nkillter', 'nwound'])
oef_p = oef_p.drop_duplicates()



prob_hoa["region"] = "HOA"
prob_p["region"] = "Philipinnes"
prob_ts["region"] = "Trans-Sahara"
prob = prob_hoa.append([prob_p, prob_ts])

#These boxplots display the distribution of probabilities resulting from my model.
#It shows us the skew of predicted probabilities of success when a specific variable is involved.
plt.figure(figsize=(10,10))
sns.boxplot(x='Pred', y='attacktype1', hue="region", data=prob)
plt.xticks(rotation=0)

#My model predicts that Kidnapping and Facility attacks more likely to be successful than other methods of attack.
#Need to attach frequency counts or % next to boxplots.
