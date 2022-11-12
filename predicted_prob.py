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

#Appending the three regional datasets into one dataset.
prob_hoa["Mission"] = "HOA"
prob_p["Mission"] = "Philippines"
prob_ts["Mission"] = "TransSahara"
prob_grouped = prob_hoa.append([prob_p, prob_ts])

#Replacing variable level names with more concise names.
prob_grouped = prob_grouped.replace(['Bombing/Explosion', 'Facility/Infrastructure Attack', 'Hostage Taking (Barricade Incident)', 
                                         'Hostage Taking (Kidnapping)'], 
                                        ['Bombing', 'Facility/Infrastructure', 'Hostage (Barricade)', 'Hostage (Kidnapping)'])
prob_grouped = prob_grouped.replace(['Government (Diplomatic)', 'Government (General)', 'Religious Figures/Institutions', 'Journalists & Media', 
                                     'Terrorists/Non-State Militia', 'Educational Institution', 'Private Citizens & Property'], 
                                    ['Diplomatic', 'Government', 'Religious Institutions', 'Journalists', 'Terrorists/Militias', 'Education', 'Private Citizens'])
prob_grouped = prob_grouped.replace(['Al-Qaida in the Islamic Maghreb (AQIM)', 'Jamaat Nusrat al-Islam wal Muslimin (JNIM)'],['Al-Qaida (AQIM)', 'Nusrat al-Islam (JNIM)'])
prob_grouped['suicide'] = prob_grouped['suicide'].replace([0, 1], ['Non-suicide', 'Suicide'])
prob_grouped['vicinity'] = prob_grouped['vicinity'].replace([0, 1], ['Outskirts of City', 'Inside City'])

#Point Plots to examine average predicted probabilities of success for each predictor variable.
def pointPlots():
    fontsize_labels = 14
    fontsize_title = 16
    ylab = "Probability of Success"
    #axis_label_offsetx = 5
    #axis_label_offsety = 0.5
    
    #SUICIDE
    fig = plt.figure(figsize=(6,7))
    sns.pointplot(x='suicide', y='Pred', data=prob_grouped, estimator='median', errorbar=None, hue='Mission',
                palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"))
    plt.xticks(rotation=0)
    plt.xlabel("SUICIDE INDICATOR", fontsize=fontsize_labels)
    plt.ylabel(ylab, fontsize=fontsize_labels)
    plt.grid(axis='both', color='gray', linestyle='dashed', alpha=0.3)
    plt.title("Figure 8: Point Plot of Median\nPredicted Probabilities of Success\nfor Suicide Attacks by Mission", fontsize=fontsize_title)
    plt.show()
    
    #VICINITY
    fig = plt.figure(figsize=(6,7))
    sns.pointplot(x='vicinity', y='Pred', data=prob_grouped, estimator='median', errorbar=None, hue='Mission',
                palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E")) 
    plt.xticks(rotation=0)
    plt.xlabel("IN THE CITY INDICATOR", fontsize=fontsize_labels)
    plt.ylabel(ylab, fontsize=fontsize_labels)
    plt.grid(axis='both', color='gray', linestyle='dashed', alpha=0.3)
    plt.title("Figure 9: Point Plot of Median Predicted\nProbabilities of Success for\nCity Vicinity by Mission", fontsize=fontsize_title)
    plt.show()
    
    #ATTACKTYPE
    fig = plt.figure(figsize=(6,6.5))
    prob_grouped_attack = prob_grouped[(prob_grouped['attacktype1'] != "Unknown")]
    sns.pointplot(x='attacktype1', y='Pred', data=prob_grouped_attack, estimator='median', errorbar=None, hue='Mission', 
                palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"),
                order=['Assassination', 'Armed Assault', 'Bombing', 'Hijacking', 
                         'Hostage (Kidnapping)', 'Facility/Infrastructure', 
                        'Unarmed Assault', 'Hostage (Barricade)'])
    plt.xticks(rotation=45)
    plt.xlabel("ATTACK TYPES", fontsize=fontsize_labels)
    plt.ylabel(ylab, fontsize=fontsize_labels)
    plt.grid(axis='both', color='gray', linestyle='dashed', alpha=0.3)
    plt.title("Figure 6: Point Plot of Median Predicted Probabilities\nof Success for Attack Type by Mission", fontsize=fontsize_title)
    plt.show()
    
    #WEAPTYPE
    fig = plt.figure(figsize=(6,6.5))
    prob_grouped_weap = prob_grouped[(prob_grouped['weaptype1'] != "Unknown") & (prob_grouped['weaptype1'] != "Other")]
    sns.pointplot(x='weaptype1', y='Pred', data=prob_grouped_weap, estimator='median', errorbar=None, hue='Mission',
                palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"),
                order=['Biological', 'Fake Weapons', 'Explosives', 'Firearms', 'Sabotage Equipment', 'Melee', 'Incendiary', 'Chemical'])
    plt.xticks(rotation=45)
    plt.xlabel("WEAPON TYPES", fontsize=fontsize_labels)
    plt.ylabel(ylab, fontsize=fontsize_labels)
    plt.grid(axis='both', color='gray', linestyle='dashed', alpha=0.3)
    plt.title("Figure 7: Point Plot of Median Predicted Probabilities \nof Success for Weapon Type by Mission", fontsize=fontsize_title)
    plt.show()
    
    #GNAME
    fig = plt.figure(figsize=(13.5,4))
    prob_grouped_gname = prob_grouped[(prob_grouped['gname'] != "Unknown")]
    sns.pointplot(x='gname', y='Pred', data=prob_grouped_gname, estimator='median', errorbar=None, hue='Mission', 
                palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"),
                order=["New People's Army (NPA)",'Moro Insurgents', 'Abu Sayyaf Group (ASG)', 
                       'Islamic Extremists', 'Nusrat al-Islam (JNIM)', 'Boko Haram', 
                       'Al-Qaida (AQIM)', 'Fulani extremists', 'Al-Shabaab', 
                       'Political Organization', 'Regional Militias/Tribes', 'Janjaweed'])
    plt.xticks(rotation=45)
    plt.xlabel("TERRORIST GROUPS", fontsize=fontsize_labels)
    plt.ylabel(ylab, fontsize=fontsize_labels)
    plt.grid(axis='both', color='gray', linestyle='dashed', alpha=0.3)
    plt.title("Figure 4: Point Plot of Median Predicted Probabilities of\nSuccess for Terrorist Group by Mission", fontsize=fontsize_title)
    plt.show()
    
    #COUNTRY
    fig = plt.figure(figsize=(13.5,4))
    sns.pointplot(x='country', y='Pred', data=prob_grouped, estimator='median', errorbar=None, hue='Mission', 
                palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"),
                order=['Mauritania', 'Tunisia', 'Algeria', 'Burkina Faso', 'Mali', 'Nigeria', 'Cameroon', 
                       'Niger', 'Chad', 'Senegal', 'Morocco', 'Kenya', 'Somalia', 'Sudan', 'Ethiopia',
                       'Djibouti', 'Eritrea'])
    plt.xticks(rotation=45)
    plt.xlabel("COUNTRIES", fontsize=fontsize_labels)
    plt.ylabel(ylab, fontsize=fontsize_labels)
    plt.grid(axis='both', color='gray', linestyle='dashed', alpha=0.3)
    plt.title("Figure 10: Point Plot of Median Predicted Probabilities of\nSuccess for Country by Mission", fontsize=fontsize_title)
    plt.show()

    #TARGTYPE
    fig = plt.figure(figsize=(13.5,4))
    prob_grouped_targ = prob_grouped[(prob_grouped['targtype1'] != "Unknown") & (prob_grouped['targtype1'] != "Other")]
    sns.pointplot(x='targtype1', y='Pred', data=prob_grouped_targ, estimator='median', errorbar=None, hue='Mission', 
                palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"),
                order=['Diplomatic', 'Airports & Aircraft', 'Maritime', 'Government', 'Utilities', 
                       'Journalists', 'Education', 'NGO', 'Tourists', 'Military', 
                       'Transportation', 'Religious Institutions', 'Private Citizens', 
                       'Business', 'Telecommunication', 'Police', 'Food or Water Supply', 
                       'Violent Political Party', 'Terrorists/Militias'])
    plt.xticks(rotation=45)
    plt.xlabel("TARGET TYPES", fontsize=fontsize_labels)
    plt.ylabel(ylab, fontsize=fontsize_labels)
    plt.grid(axis='both', color='gray', linestyle='dashed', alpha=0.3)
    plt.title("Figure 5: Point Plot of Median Predicted Probabilities\nof Success for Target Type by Mission", fontsize=fontsize_title)
    plt.show()
    
    return()

pointPlots()
    #Create tiny subplots to describe variable level frequencies.




legend_maker = prob_grouped
legend_maker = legend_maker.replace('Philippines', 'Outside')
fig = plt.figure(figsize=(6,8))
sns.pointplot(x='suicide', y='Pred', data=legend_maker, estimator='median', errorbar=None, hue='Mission',
            palette=dict(TransSahara="#F3BE9E", HOA="#EBE4A9", Outside="lightgrey"))
plt.show()

legend_maker = legend_maker.replace(['Nonsuicide', 'Suicide'], ['Unsuccessful', 'Successful'])
fig = plt.figure(figsize=(6,8))
sns.pointplot(x='suicide', y='Pred', data=legend_maker, estimator='median', errorbar=None, hue='suicide',
            palette=dict(Unsuccessful="#FF0000", Successful="#7CAD91"))
plt.show()








#Examining combinations with a predicted probability of 95% or greater.
prob_hoa95 = prob_hoa.loc[(prob_hoa.Pred >= 0.90) & (prob_hoa.success == 1)]
prob_p95 = prob_p.loc[(prob_p.Pred >= 0.90) & (prob_hoa.success == 1)]
prob_ts95 = prob_ts.loc[(prob_ts.Pred >= 0.90) & (prob_hoa.success == 1)]

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

#Grouped bar charts to compare similarities/differences for components of successful terrorism between regions.
def groupBarCharts(var, title, xlab, ylab):

    table = pd.crosstab(prob_grouped[var], prob_grouped['Mission'])
    x = np.arange(start=0, stop=2*len(table.index), step=2)
    
    #Converting columns to relative frequencies.
    table['HOA'] = table['HOA'] / table['HOA'].sum()
    table['Philippines'] = table['Philippines'] / table['Philippines'].sum()
    table['TransSahara'] = table['TransSahara'] / table['TransSahara'].sum()
    
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
    plt.bar(x + 0.4, table['TransSahara'], width=0.4, color='#F3BE9E')
    ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.3)
    plt.xticks(x, table.index, rotation=45, fontsize=12)
    plt.title(title, fontsize=18)
    plt.xlabel(xlab, fontsize=14)
    plt.ylabel(ylab, fontsize=14)
    
    if var == 'targtype1':
        plt.legend(['HOA', 'Philippines', 'TransSahara'], loc='upper left', ncol=3, fontsize=16)
    else:
        plt.legend(['HOA', 'Philippines', 'TransSahara'], loc='upper right', ncol=3, fontsize=16)
    
    for bars in ax.containers:
        ax.bar_label(bars, fmt='%.2f', fontsize=12)
    
    return()


def separatedBarCharts(var, title, xlab, ylab):

    if var == 'country':
        x1 = np.arange(start=0, stop=len(oef_hoa[var].value_counts().index))
        x3 = np.arange(start=0, stop=len(oef_ts[var].value_counts().index))
    
        table_hoa = oef_hoa[var].value_counts()
        table_hoa = table_hoa.to_frame()
        table_hoa['relative'] = table_hoa[var] / table_hoa[var].sum()
                
        table_ts = oef_ts[var].value_counts()
        table_ts = table_ts.to_frame()
        table_ts['relative'] = table_ts[var] / table_ts[var].sum()
        
        fig = plt.figure(figsize=(18,14))
        plt.title(title, fontsize=18)
        plt.axis('off')
        
        ax1 = fig.add_subplot(121) #Change to 131 to have the same size as gname plots.
        plt.bar(table_hoa.index, table_hoa['relative'], width=0.7, color ='#EBE4A9')
        ax1.yaxis.grid(color='gray', linestyle='dashed', alpha=0.3)
        plt.xticks(x1, table_hoa.index, rotation=45, fontsize=12)
        plt.ylabel(ylab, fontsize=14)
        ax1.yaxis.set_label_coords(-0.2, 0.5)
        ax1.legend(['HOA'], fontsize=16)
            
        ax3 = fig.add_subplot(122, sharey=ax1)
        plt.bar(table_ts.index, table_ts['relative'], width=0.8, color='#F3BE9E')
        ax3.yaxis.grid(color='gray', linestyle='dashed', alpha=0.3)
        plt.xticks(x3, table_ts.index, rotation=45, fontsize=12)
        ax3.legend(['Trans-Sahara'], fontsize=16)
    
    else: 
        x1 = np.arange(start=0, stop=len(oef_hoa[var].value_counts().index))
        x2 = np.arange(start=0, stop=len(oef_p[var].value_counts().index))
        x3 = np.arange(start=0, stop=len(oef_ts[var].value_counts().index))

        table_hoa = oef_hoa[var].value_counts()
        table_hoa = table_hoa.to_frame()
        table_hoa['relative'] = table_hoa[var] / table_hoa[var].sum()
        
        table_p = oef_p[var].value_counts()
        table_p = table_p.to_frame()
        table_p['relative'] = table_p[var] / table_p[var].sum()
        
        table_ts = oef_ts[var].value_counts()
        table_ts = table_ts.to_frame()
        table_ts['relative'] = table_ts[var] / table_ts[var].sum()
        
        fig = plt.figure(figsize=(18,14))
        plt.title(title, fontsize=18)
        plt.axis('off')
        
        ax1 = fig.add_subplot(131)
        plt.bar(table_hoa.index, table_hoa['relative'], width=0.7, color ='#EBE4A9')
        ax1.yaxis.grid(color='gray', linestyle='dashed', alpha=0.3)
        plt.xticks(x1, table_hoa.index, rotation=45, fontsize=12)
        plt.ylabel(ylab, fontsize=14)
        ax1.yaxis.set_label_coords(-0.2, 0.5)
        ax1.legend(['HOA'], fontsize=16)
        
        ax2 = fig.add_subplot(132, sharey=ax1)
        plt.bar(table_p.index, table_p['relative'], width=0.6, color='#7CA5BE')
        ax2.yaxis.grid(color='gray', linestyle='dashed', alpha=0.3)
        plt.xticks(x2, table_p.index, rotation=45, fontsize=12)
        plt.xlabel(xlab, fontsize=14)
        ax2.xaxis.set_label_coords(0.5, -0.2)
        ax2.legend(['Philippines'], fontsize=16)
    
        ax3 = fig.add_subplot(133, sharey=ax1)
        plt.bar(table_ts.index, table_ts['relative'], width=0.8, color='#F3BE9E')
        ax3.yaxis.grid(color='gray', linestyle='dashed', alpha=0.3)
        plt.xticks(x3, table_ts.index, rotation=45, fontsize=12)
        ax3.legend(['Trans-Sahara'], fontsize=16)

    return()

#Bar Charts of Predictor Variables
groupBarCharts('suicide', "Bar Chart of Suicide Attacks by Mission for Terrorist Attacks with a Predicted Probability of Success ≥ 95%",
               "SUICIDE INDICATOR", "Percentage")
groupBarCharts('vicinity', "Bar Chart of Vicinities of City by Mission for Terrorist Attacks with a Predicted Probability of Success ≥ 95%",
               "IN THE CITY INDICATOR", "Percentage")
groupBarCharts('attacktype1', "Bar Chart of Attack Types by Mission for Terrorist Attacks with a Predicted Probability of Success ≥ 95%",
               "ATTACK TYPE", "Percentage") 
groupBarCharts('targtype1', "Bar Chart of Target Types by Mission for Terrorist Attacks with a Predicted Probability of Success ≥ 95%",
               "TARGET TYPE", "Percentage")
groupBarCharts('weaptype1', "Bar Chart of Weapon Types by Mission for Terrorist Attacks with a Predicted Probability of Success ≥ 95%",
               "WEAPON TYPE", "Percentage")
separatedBarCharts('gname', "Bar Chart of Groups by Mission for Terrorist Attacks with a Predicted Probability of Success ≥ 95%",
               "IN THE CITY INDICATOR", "Percentage")
separatedBarCharts('country', "Bar Chart of Countries by Mission for Terrorist Attacks with a Predicted Probability of Success ≥ 95%",
               "IN THE CITY INDICATOR", "Percentage")




prob_hoa["mission"] = "HOA"
prob_p["mission"] = "Philippines"
prob_ts["mission"] = "TransSahara"
prob_grouped = prob_hoa.append([prob_p, prob_ts])



sns.catplot(x='gname', y='Pred', data=prob_grouped, kind="point", errorbar=None, hue='mission', palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"))
plt.xticks(rotation=90)
sns.catplot(x='country', y='Pred', data=prob_grouped, kind="point", errorbar=None, hue='mission', palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"))
plt.xticks(rotation=90)












sns.stripplot(x='suicide', y='Pred', data=prob_ts)

sns.boxenplot(x='suicide', y='Pred', data=prob_grouped, hue='mission')



m = prob_ts.attacktype1.map(ord)
prob_ts["Pred"] += m

# Initialize the FacetGrid object
pal = sns.cubehelix_palette(10, rot=-.25, light=.7)


rp = sns.FacetGrid(prob_ts, row="vicinity", hue="vicinity", aspect=5, height=1.25, palette=pal)
rp.map(sns.kdeplot, 'Pred', clip_on=False,
       shade=True, alpha=0.7, lw=4, bw=.2)
  
rp.map(plt.axhline, y=0, lw=4, clip_on=False)


# Draw the densities in a few steps
g.map(sns.kdeplot, "Pred",
      bw_adjust=.5, clip_on=False,
      fill=True, alpha=1, linewidth=1.5)
g.map(sns.kdeplot, "Pred", clip_on=False, color="w", lw=2, bw_adjust=.5)

# passing color=None to refline() uses the hue mapping
g.refline(y=0, linewidth=2, linestyle="-", color=None, clip_on=False)
g.figure.subplots_adjust(hspace=-.25)
#sns.regplot(x='Pred', y='success', data=prob_grouped, logistic=True, ci=None), 
#scatter_kws={'color': 'black'}, line_kws={'color': 'red'})








#%% Code Graveyard

#fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(nrows=1, ncols=7, figsize=(20,12), sharey=True)


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
sns.violinplot(x='attacktype1', y='Pred', hue="mission", data=prob_grouped, orient="v")
plt.xticks(rotation=90)

#My model predicts that Kidnapping and Facility attacks more likely to be successful than other methods of attack.
#Need to attach frequency counts or % next to boxplots.
