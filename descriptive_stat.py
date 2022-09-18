import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

oef_p = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\oef_p.csv')
oef_hoa = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\oef_hoa.csv')
oef_ts = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\oef_ts.csv')

#%% Univariate Analysis

def barchart(dataset, var, title, xlabel):
    table = dataset[var].value_counts().sort_index()
    table.plot.bar(figsize=(10,6),
                   xlabel=xlabel,
                   ylabel="Number of Attacks",
                   color="slategrey",
                   edgecolor="black")
    plt.xticks(rotation=90)
    plt.title(("Bar Chart of " + title), fontsize=15)

def barchartTop10(dataset, var, title, xlabel):
    table = dataset[var].value_counts().sort_values(ascending=False)
    table = table[0:10]
    table.plot.bar(figsize=(10,6),
                   xlabel=xlabel,
                   ylabel="Number of Attacks",
                   color="slategrey",
                   edgecolor="black")
    plt.xticks(rotation=90)
    plt.title(("Bar Chart of " + title), fontsize=15)
    
    

#Operation Freedom Eagle - OEF Philippines
barchart(oef_p, "year", "Attacks by Year", "Year")
barchart(oef_p, "country", "Attacks by Country", "Country")
barchart(oef_p, "region", "Attacks by Region", "Region")
barchartTop10(oef_p, "provstate", "Attacks by Province/Administrative District", "Province")
barchartTop10(oef_p, "city", "Attacks by City", "City")
barchart(oef_p, "specificity", "Attacks by Accuracy of Geographic Coordinates", "Accuracy Level")
barchart(oef_p, "vicinity", "Whether the attack was inside the city 0, or not 1", "In the city Indicator")
barchart(oef_p, "success", "Attacks by Success 1, or Unsuccessful 0", "Success Indicator")
barchart(oef_p, "suicide", "Attacks by Suicide", "Suicide Indicator")
barchart(oef_p, "attacktype1", "Attacks by Attack Method (First Level)", "Attack Type")
barchart(oef_p, "attacktype2", "Attacks by Attack Method (Secondary Level)", "Attack Type")
barchart(oef_p, "attacktype2", "Attacks by Attack Method (Tertiary Level)", "Attack Type")
barchart(oef_p, "targtype1", "Attacks by Target Type", "Target Type")
barchartTop10(oef_p, "targsubtype1", "Attacks by Specific Target Type", "Sub-Target Type")
barchartTop10(oef_p, "corp1", "Attacks by Corporate/Agency Enitity", "Corporate/Agency")
barchartTop10(oef_p, "target1", "Attacks by Specific Target", "Target")
barchartTop10(oef_p, "natlty1", "Attacks by Nationality", "Nationality")
barchart(oef_p, "gname", "Attacks by Group", "Group")
barchartTop10(oef_p, "gsubname", "Attacks by Sub-Group", "Sub-Group")
oef_p.nperps.describe()
oef_p.nperpcap.describe()
barchart(oef_p, "claimed", "Claimed/Unclaimed Attacks", "Claimed Attack")
barchart(oef_p, "weaptype1", "Attacks by Weapon Type", "Weapon Type") 
barchart(oef_p, "weapsubtype1", "Attacks by Specific Weapon Type", "Weapon Type")
oef_p.nkill.describe()
oef_p.nkillter.describe()
oef_p.nwound.describe()

#Operation Enduring Freedom - Horn of Africa
barchart(oef_hoa, "year", "Attacks by Year", "Year")
barchart(oef_hoa, "country", "Attacks by Country", "Country")
barchart(oef_hoa, "region", "Attacks by Region", "Region")
barchartTop10(oef_hoa, "provstate", "Attacks by Province/Administrative District", "Province")
barchartTop10(oef_hoa, "city", "Attacks by City", "City")
barchart(oef_hoa, "specificity", "Attacks by Accuracy of Geographic Coordinates", "Accuracy Level")
barchart(oef_hoa, "vicinity", "Whether the attack was inside the city 0, or not 1", "In the city Indicator")
barchart(oef_hoa, "success", "Attacks by Success 1, or Unsuccessful 0", "Success Indicator")
barchart(oef_hoa, "suicide", "Attacks by Suicide", "Suicide Indicator")
barchart(oef_hoa, "attacktype1", "Attacks by Attack Method (First Level)", "Attack Type")
barchart(oef_hoa, "attacktype2", "Attacks by Attack Method (Secondary Level)", "Attack Type")
barchart(oef_hoa, "attacktype2", "Attacks by Attack Method (Tertiary Level)", "Attack Type")
barchart(oef_hoa, "targtype1", "Attacks by Target Type", "Target Type")
barchartTop10(oef_hoa, "targsubtype1", "Attacks by Specific Target Type", "Sub-Target Type")
barchartTop10(oef_hoa, "corp1", "Attacks by Corporate/Agency Enitity", "Corporate/Agency")
barchartTop10(oef_hoa, "target1", "Attacks by Specific Target", "Target")
barchartTop10(oef_hoa, "natlty1", "Attacks by Nationality", "Nationality")
barchart(oef_hoa, "gname", "Attacks by Group", "Group")
barchartTop10(oef_hoa, "gsubname", "Attacks by Sub-Group", "Sub-Group")
oef_hoa.nperps.describe()
oef_hoa.nperpcap.describe()
barchart(oef_hoa, "claimed", "Claimed/Unclaimed Attacks", "Claimed Attack")
barchart(oef_hoa, "weaptype1", "Attacks by Weapon Type", "Weapon Type") 
barchart(oef_hoa, "weapsubtype1", "Attacks by Specific Weapon Type", "Weapon Type")
oef_hoa.nkill.describe()
oef_hoa.nkillter.describe()
oef_hoa.nwound.describe()


#Operation Juniper Shield - OEF Trans-Sahara
barchart(oef_ts, "year", "Attacks by Year", "Year")
barchart(oef_ts, "country", "Attacks by Country", "Country")
barchart(oef_ts, "region", "Attacks by Region", "Region")
barchartTop10(oef_ts, "provstate", "Attacks by Province/Administrative District", "Province")
barchartTop10(oef_ts, "city", "Attacks by City", "City")
barchart(oef_ts, "specificity", "Attacks by Accuracy of Geographic Coordinates", "Accuracy Level")
barchart(oef_ts, "vicinity", "Whether the attack was inside the city 0, or not 1", "In the city Indicator")
barchart(oef_ts, "success", "Attacks by Success 1, or Unsuccessful 0", "Success Indicator")
barchart(oef_ts, "suicide", "Attacks by Suicide", "Suicide Indicator")
barchart(oef_ts, "attacktype1", "Attacks by Attack Method (First Level)", "Attack Type")
barchart(oef_ts, "attacktype2", "Attacks by Attack Method (Secondary Level)", "Attack Type")
barchart(oef_ts, "attacktype2", "Attacks by Attack Method (Tertiary Level)", "Attack Type")
barchart(oef_ts, "targtype1", "Attacks by Target Type", "Target Type")
barchartTop10(oef_ts, "targsubtype1", "Attacks by Specific Target Type", "Sub-Target Type")
barchartTop10(oef_ts, "corp1", "Attacks by Corporate/Agency Enitity", "Corporate/Agency")
barchartTop10(oef_ts, "target1", "Attacks by Specific Target", "Target")
barchartTop10(oef_ts, "natlty1", "Attacks by Nationality", "Nationality")
barchart(oef_ts, "gname", "Attacks by Group", "Group")
barchartTop10(oef_ts, "gsubname", "Attacks by Sub-Group", "Sub-Group")
oef_ts.nperps.describe()
oef_ts.nperpcap.describe()
barchart(oef_ts, "claimed", "Claimed/Unclaimed Attacks", "Claimed Attack")
barchart(oef_ts, "weaptype1", "Attacks by Weapon Type", "Weapon Type") 
barchart(oef_ts, "weapsubtype1", "Attacks by Specific Weapon Type", "Weapon Type")
oef_ts.nkill.describe()
oef_ts.nkillter.describe()
oef_ts.nwound.describe()












def barchart3(var, title, xlabel):
    table1 = pd.DataFrame(oef_hoa[var].value_counts().sort_index())
    table2 = pd.DataFrame(oef_p[var].value_counts().sort_index())
    table3 = pd.DataFrame(oef_ts[var].value_counts().sort_index())   
    
    max_len = max([len(table1), len(table2), len(table3)])
    
    x_axis1 = []
    for i in range(max_len):
        x_axis1.append(i * 4) 
    x_axis2 = []
    for i in range(max_len):
        x_axis2.append(i * 4 + 0.8)
    x_axis3 = []
    for i in range(max_len):
        x_axis3.append(i * 4 + 1.6)
    x_ticks = []
    for i in range(max_len):
        x_ticks.append(i * 4)

    f, ax = plt.subplots(1, figsize=(12, 7))
    plt.bar(x_axis1, table1.iloc[:, 0:1].squeeze(), width=0.8, color='firebrick')   
    plt.bar(x_axis2, table2.iloc[:, 0:1].squeeze(), width=0.8, color='lightsteelblue')    
    plt.bar(x_axis3, table3.iloc[:, 0:1].squeeze(), width=0.8, color='darkseagreen')    
            #y-values must be in Pandas Series format, therefore it requires the method .squeeze() to convert DataFrame to Series.

    plt.xticks(x_ticks, table1.index, rotation=90)
    plt.title(("Bar Chart of " + title), fontsize=15)
    
    firebrick_patch = mpatches.Patch(color='firebrick', label='OEF-Horn of Africa')
    lightsteelblue_patch = mpatches.Patch(color='lightsteelblue', label='OEF-Philippines')
    darkseagreen_patch = mpatches.Patch(color='darkseagreen', label='OEF-Trans Sahara')    
    plt.legend(handles=[firebrick_patch, lightsteelblue_patch, darkseagreen_patch])



barchart3('attacktype1', "Attacks by Attack Method (First Level)", "Attack Type")
barchart3('success', "Attacks by Success 1, or Unsuccessful 0", "Success Indicator")
barchart3('suicide', "Attacks by Suicide", "Suicide Indicator")
barchart3('targtype1', "Attacks by Target Type", "Target Type")
barchart3('weaptype1', "Attacks by Weapon Type", "Weapon Type") 











#%% Bivariate Analysis

def freq_table_success(var):
    table = pd.crosstab(oef_ts[var], oef_ts['success'])
    table['percent'] = table[1] / (table[0] + table[1])
    return table

def bivariate_success(var, title):
    cross_tab = pd.crosstab(oef_ts[var], oef_ts['success'])
    plt.bar(cross_tab.index, cross_tab[0], color='red')
    plt.bar(cross_tab.index, cross_tab[1], bottom=cross_tab[0], color='green')
    plt.title(title)
    plt.xticks(rotation = 90)
    plt.show()

def bivariate_success_relative(var, title):
    cross_tab = pd.crosstab(oef_ts[var], oef_ts['success'], normalize="index")
    plt.bar(cross_tab.index, cross_tab[0], color='red')
    plt.bar(cross_tab.index, cross_tab[1], bottom=cross_tab[0], color='green')
    plt.title('100% Stacked Bar Chart of ' + title)
    plt.xticks(rotation = 90)
    plt.show()

export_table = freq_table_success('gname')
export_table = freq_table_success('attacktype1')
export_table = freq_table_success('targtype1')
export_table = freq_table_success('targsubtype1')
export_table = freq_table_success('suicide')
export_table = freq_table_success('weaptype1')

bivariate_success('year', 'Stacked Bar Chart of Success by Year')

bivariate_success_relative('gname', 'Success by Group')
bivariate_success_relative('attacktype1_txt', 'Success by Attack Type')
bivariate_success_relative('targtype1_txt', 'Success by Target Type')
bivariate_success_relative('targsubtype1_txt', 'Success by Target Sub Type')
        #Needs to be expanded figsize(20,6)
bivariate_success_relative('suicide', 'Success by Suicide Attack')
bivariate_success_relative('weaptype1_txt', 'Success by Weapon')
bivariate_success_relative('year', 'Success by Year')


table = freq_table_success('nkill')




#Code Graveyard

def cat_univariate_attacktype(var, title, xlabel):
    attack_names = ["Assassination", "Hijacking", "Kidnapping", 
                        "Barricade Incident", "Bombing/Explosion", "Armed Assault", 
                        "Unarmed Assault", "Facility/Infrastructure Attack", "Unknown"]
    attack_hierarchy = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    dict_attack = {'types':attack_names, 'hierarchy':attack_hierarchy}
    attacktypes = pd.DataFrame(dict_attack, columns=['types', 'hierarchy'])
    
    table = oef_hoa[var].value_counts()
    table = pd.DataFrame(table)
    
    table = table.merge(attacktypes, left_on='attack_names', right_on='types')
    table = table.sort_values(by='hierarchy', ascending=False)
    
    table.plot.bar(figsize=(10,6),
                   #xlabel=xlabel,
                   ylabel="Number of Attacks",
                   color="slategrey",
                   edgecolor="black")
    plt.xticks(rotation=90)
    plt.title(("Bar Chart of " + title), fontsize=15)


def barchart_long(var, title, xlabel):
    table = oef_hoa[var].value_counts().sort_values(ascending=False)
    table = table[0:10]
    table.plot.bar(figsize=(10,6),
                   xlabel=xlabel,
                   ylabel="Number of Attacks",
                   color="slategrey",
                   edgecolor="black")
    plt.xticks(rotation=90)
    plt.title(("Bar Chart of " + title), fontsize=15)
        #Only shows top 10 frequencies.

def num_univariate_analysis(var):
    return (oef_p[var].describe())



corr_matrix = df.corr()
test = df.groupby(['gname', 'attacktype1_txt']).agg({'success': ['mean', 'min', 'max']})
test = df.groupby(['attacktype1_txt', 'targtype1_txt'])['success'].mean()

df['date'] = pd.to_datetime(df[['day', 'month', 'year']])
df = df.set_index('date')
table = df.groupby(pd.Grouper(freq="M")).sum()
table.plot(y=['success', 'event', 'suicide', 'claimed'], figsize=(12,6), title='Aggregated by Month~Year')

table.plot(y='event', figsize=(15,6), title='Events Aggregated by Month~Year')
table.plot(y=['nkill', 'nkillter', 'nwound'], figsize=(15,6), title='Casualties & Fatalities Aggregated by Month~Year')
#table.plot.bar(y='success', figsize=(10,6))

plt.bar(table.index, table['success'], color='red')
plt.bar(table.index, table['event'], bottom=table['success'], color='green')


table_natlty = df.natlty1_txt.value_counts()
table_top_natlty = table_natlty[:10]
table_top_natlty.plot.bar(figsize=(10,6), title = 'Bar Chart of Attacks by Nationality (Top 10)', xlabel = 'Nationality', \
                          ylabel = 'Number of Attacks', color='lightseagreen', edgecolor='black')
plt.xticks(rotation = 45)
