import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import sklearn
import sklearn.model_selection
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import seaborn as sns
from scipy.stats import gaussian_kde

df = pd.read_csv(r'C:\Users\Slaye\Documents\Courses\STAT_3130\sub_gtdatabase.csv')
libya = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\libya.shp')
egypt = gpd.read_file(r'C:\Users\Slaye\Documents\Courses\STAT_3130\shapefiles\egypt.shp')
algeria = gpd.read_file(r'C:\Users\Slaye\Documents\Courses\STAT_3130\shapefiles\algeria.shp')
morocco = gpd.read_file(r'C:\Users\Slaye\Documents\Courses\STAT_3130\shapefiles\morocco.shp')
tunisia = gpd.read_file(r'C:\Users\Slaye\Documents\Courses\STAT_3130\shapefiles\tunisia.shp')
world = gpd.read_file(r'C:\Users\Slaye\Documents\Courses\STAT_3130\shapefiles\world_countries_2020.shp')
# isis.to_csv(r'C:\Users\Slaye\Documents\Courses\STAT_3130\isis_gtdatabase.csv')

philippines = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\philippines.shp')

prob_hoa = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\prob_hoa.csv')
prob_hoa = prob_hoa.drop(["eventid"], axis=1)
prob_hoa = prob_hoa.drop_duplicates()

legend_maker = prob_grouped
legend_maker = legend_maker.replace('Philippines', 'Outside')
fig = plt.figure(figsize=(6, 8))
sns.pointplot(x='suicide', y='Pred', data=legend_maker, estimator='median', errorbar=None, hue='Mission',
              palette=dict(TransSahara="#F3BE9E", HOA="#EBE4A9", Outside="lightgrey"))
plt.show()

legend_maker = legend_maker.replace(['Nonsuicide', 'Suicide'], ['Unsuccessful', 'Successful'])
fig = plt.figure(figsize=(6, 8))
sns.pointplot(x='suicide', y='Pred', data=legend_maker, estimator='median', errorbar=None, hue='suicide',
              palette=dict(Unsuccessful="#FF0000", Successful="#7CAD91"))
plt.show()

# Examining combinations with a predicted probability of 95% or greater.
prob_hoa95 = prob_hoa.loc[(prob_hoa.Pred >= 0.90) & (prob_hoa.success == 1)]
prob_p95 = prob_p.loc[(prob_p.Pred >= 0.90) & (prob_hoa.success == 1)]
prob_ts95 = prob_ts.loc[(prob_ts.Pred >= 0.90) & (prob_hoa.success == 1)]

# Appending the three regional datasets into one dataset.
prob_hoa95["mission"] = "HOA"
prob_p95["mission"] = "Philippines"
prob_ts95["mission"] = "Trans-Sahara"
prob95_grouped = prob_hoa95.append([prob_p95, prob_ts95])

# Replacing variable level names with more concise names.
prob95_grouped = prob95_grouped.replace(
    ['Bombing/Explosion', 'Facility/Infrastructure Attack', 'Hostage Taking (Barricade Incident)',
     'Hostage Taking (Kidnapping)'],
    ['Bombing', 'Facility/Infrastructure', 'Hostage (Barricade)', 'Hostage (Kidnapping)'])

# Examining the number of correctly predicted successful terrorist attacks.
prob_hoa95.success.mean()  # 97.0% Correctly classified.
prob_p95.success.mean()  # 98.6% Correctly classified.
prob_ts95.success.mean()  # 97.2% Correctly classified.


# Grouped bar charts to compare similarities/differences for components of successful terrorism between regions.
def groupBarCharts(var, title, xlab, ylab):
    table = pd.crosstab(prob_grouped[var], prob_grouped['Mission'])
    x = np.arange(start=0, stop=2 * len(table.index), step=2)

    # Converting columns to relative frequencies.
    table['HOA'] = table['HOA'] / table['HOA'].sum()
    table['Philippines'] = table['Philippines'] / table['Philippines'].sum()
    table['TransSahara'] = table['TransSahara'] / table['TransSahara'].sum()

    if var == 'attacktype1':
        table = table.drop(index="Unknown")
        x = np.arange(start=0, stop=2 * len(table.index), step=2)
    elif var == 'weaptype1':
        table = table.drop(index=["Unknown", "Other"])
        x = np.arange(start=0, stop=2 * len(table.index), step=2)

    if var == 'targtype1':
        table = table.loc[(table.index == "Business") |
                          (table.index == "Government (General)") |
                          (table.index == "Military") |
                          (table.index == "Police") |
                          (table.index == "Educational Institution") |
                          (table.index == "Private Citizens & Property")]
        x = np.arange(start=0, stop=2 * len(table.index), step=2)
        # Manually choosing to only display the top 6 levels of targets.
        # Need to merge the excluded levels into an 'other' category. *****

    fig, ax = plt.subplots(1, figsize=(18, 14))
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

    return ()


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

        fig = plt.figure(figsize=(18, 14))
        plt.title(title, fontsize=18)
        plt.axis('off')

        ax1 = fig.add_subplot(121)  # Change to 131 to have the same size as gname plots.
        plt.bar(table_hoa.index, table_hoa['relative'], width=0.7, color='#EBE4A9')
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

        fig = plt.figure(figsize=(18, 14))
        plt.title(title, fontsize=18)
        plt.axis('off')

        ax1 = fig.add_subplot(131)
        plt.bar(table_hoa.index, table_hoa['relative'], width=0.7, color='#EBE4A9')
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

    return ()


# Bar Charts of Predictor Variables
groupBarCharts('suicide',
               "Bar Chart of Suicide Attacks by Mission for Terrorist Attacks with a Predicted Probability of "
               "Success ≥ 95%",
               "SUICIDE INDICATOR", "Percentage")
groupBarCharts('vicinity',
               "Bar Chart of Vicinities of City by Mission for Terrorist Attacks with a Predicted Probability of "
               "Success ≥ 95%",
               "IN THE CITY INDICATOR", "Percentage")
groupBarCharts('attacktype1',
               "Bar Chart of Attack Types by Mission for Terrorist Attacks with a Predicted Probability of "
               "Success ≥ 95%",
               "ATTACK TYPE", "Percentage")
groupBarCharts('targtype1',
               "Bar Chart of Target Types by Mission for Terrorist Attacks with a Predicted Probability of "
               "Success ≥ 95%",
               "TARGET TYPE", "Percentage")
groupBarCharts('weaptype1',
               "Bar Chart of Weapon Types by Mission for Terrorist Attacks with a Predicted Probability of "
               "Success ≥ 95%",
               "WEAPON TYPE", "Percentage")
separatedBarCharts('gname',
                   "Bar Chart of Groups by Mission for Terrorist Attacks with a Predicted Probability of "
                   "Success ≥ 95%",
                   "IN THE CITY INDICATOR", "Percentage")
separatedBarCharts('country',
                   "Bar Chart of Countries by Mission for Terrorist Attacks with a Predicted Probability of "
                   "Success ≥ 95%",
                   "IN THE CITY INDICATOR", "Percentage")

prob_hoa["mission"] = "HOA"
prob_p["mission"] = "Philippines"
prob_ts["mission"] = "TransSahara"
prob_grouped = prob_hoa.append([prob_p, prob_ts])

sns.catplot(x='gname', y='Pred', data=prob_grouped, kind="point", errorbar=None, hue='mission',
            palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"))
plt.xticks(rotation=90)
sns.catplot(x='country', y='Pred', data=prob_grouped, kind="point", errorbar=None, hue='mission',
            palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"))
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


# sns.regplot(x='Pred', y='success', data=prob_grouped, logistic=True, ci=None),
# scatter_kws={'color': 'black'}, line_kws={'color': 'red'})


# %% Code Graveyard

# fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(nrows=1, ncols=7, figsize=(20,12), sharey=True)


# The four plots to compare frequency of predictor variables. Need to include suicide and vicinity.
def probBarchart(dataset, color_input):
    edgecolor_input = "black"
    label_font = 12
    figure_sizex = 10
    figure_sizey = 10

    plt.figure(figsize=(figure_sizex, figure_sizey), tight_layout=False)
    p1 = plt.bar(dataset['suicide'].value_counts().index, dataset['suicide'].value_counts(), edgecolor=edgecolor_input,
                 color=color_input)
    plt.xticks(rotation=90)
    plt.bar_label(p1, padding=2, fontsize=label_font)
    plt.title("Barchart of Suicide Attacks")

    plt.figure(figsize=(figure_sizex, figure_sizey), tight_layout=True)
    p1 = plt.bar(dataset['vicinity'].value_counts().index, dataset['vicinity'].value_counts(),
                 edgecolor=edgecolor_input, color=color_input)
    plt.xticks(rotation=90)
    plt.bar_label(p1, padding=2, fontsize=label_font)
    plt.title("Barchart of Vicinity")

    plt.figure(figsize=(figure_sizex, figure_sizey), tight_layout=True)
    p1 = plt.bar(dataset['gname'].value_counts().index, dataset['gname'].value_counts(), edgecolor=edgecolor_input,
                 color=color_input)
    plt.xticks(rotation=90)
    plt.bar_label(p1, padding=2, fontsize=label_font)
    plt.title("Barchart of Terrorist Groups")

    plt.figure(figsize=(figure_sizex, figure_sizey), tight_layout=True)
    p1 = plt.bar(dataset['attacktype1'].value_counts().index, dataset['attacktype1'].value_counts(),
                 edgecolor=edgecolor_input, color=color_input)
    plt.xticks(rotation=90)
    plt.bar_label(p1, padding=2, fontsize=label_font)
    plt.title("Barchart of Attack Types")

    plt.figure(figsize=(figure_sizex, figure_sizey), tight_layout=True)
    p1 = plt.bar(dataset['targtype1'].value_counts().index, dataset['targtype1'].value_counts(),
                 edgecolor=edgecolor_input, color=color_input)
    plt.xticks(rotation=90)
    plt.bar_label(p1, padding=2, fontsize=label_font)
    plt.title("Barchart of Target Types")

    plt.figure(figsize=(figure_sizex, figure_sizey), tight_layout=True)
    p1 = plt.bar(dataset['weaptype1'].value_counts().index, dataset['weaptype1'].value_counts(),
                 edgecolor=edgecolor_input, color=color_input)
    plt.xticks(rotation=90)
    plt.bar_label(p1, padding=2, fontsize=label_font)
    plt.title("Barchart of Weapon Types")

    return ()


probBarchart(prob_hoa95, "#EBE4A9")
probBarchart(prob_p95, "#1D3C45")
probBarchart(prob_ts95, "#D2601A")

# (Philippines) While armed assualts and bombings are more frequent, nearly 50% of unique attacks with a predicted
# probability of 95% or greater involve kidnappings.
# (Philippines) The analysis indicates private citizens are more susceptible to possible successful terrorist attacks
# than any other target type.


# Checking to make sure the original dataset (oef_p) and the predicted probability dataset (prob_p)
# have the same number of unique combination for predictor variables.
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

# These boxplots display the distribution of probabilities resulting from my model.
# It shows us the skew of predicted probabilities of success when a specific variable is involved.
plt.figure(figsize=(10, 10))
sns.violinplot(x='attacktype1', y='Pred', hue="mission", data=prob_grouped, orient="v")
plt.xticks(rotation=90)

# My model predicts that Kidnapping and Facility attacks more likely to be successful than other methods of attack.
# Need to attach frequency counts or % next to boxplots.


################################# ISLAMIC STATE OF IRAQ AND SYRIA
# df = df.loc[df['iyear'] >= 2000]
# df['islamicState'] = df['gname'].str.find('Islamic')
# df.loc[df['islamicState'] >= 0, 'islamicState'] = 1
# df.loc[df['islamicState'] < 0, 'islamicState'] = 0
# df = df.loc[df['islamicState'] == 1]
# Boko Haram, Caucusus, Bangladesh, East Asia, Greater Sahara

isis = df.loc[(df['gname'] == 'Islamic State of Iraq and the Levant (ISIL)') | (
            df['gname'] == 'Sinai Province of the Islamic State') |
              (df['gname'] == 'Tripoli Province of the Islamic State') | (
                          df['gname'] == 'Barqa Province of the Islamic State') |
              (df['gname'] == 'Hadramawt Province of the Islamic State') | (
                          df['gname'] == 'Sanaa Province of the Islamic State') |
              (df['gname'] == 'Islamic State in Egypt') | (df['gname'] == 'Fezzan Province of the Islamic State') |
              (df['gname'] == 'Najd Province of the Islamic State') | (
                          df['gname'] == 'Algeria Province of the Islamic State') |
              (df['gname'] == 'Hijaz Province of the Islamic State') | (
                          df['gname'] == 'Bahrain Province of the Islamic State') |
              (df['gname'] == 'Shabwah Province of the Islamic State') | (
                          df['gname'] == 'Lahij Province of the Islamic State') |
              (df['gname'] == 'Al Bayda Province of the Islamic State') | (
                          df['gname'] == 'Adan-Abyan Province of the Islamic State')]
isis = isis.loc[isis['iyear'] >= 2013]
isis = isis.loc[isis['region'] == 10]
isis = isis.reset_index()
isis['event'] = 1

isis = isis.rename(columns={'iyear': 'year', 'imonth': 'month', 'iday': 'day'})
isis['date'] = pd.to_datetime(isis[['day', 'month', 'year']])
isis = isis.set_index('date')

### GROUP BY MONTH~YEAR
table = isis.groupby(pd.Grouper(freq="M")).sum()
table = table.drop(['index', 'eventid', 'year', 'month', 'day', 'region', 'latitude', 'longitude',
                    'success', 'suicide', 'claimed', 'property', 'propextent'], axis=1)
table.plot(figsize=(15, 6), title='Events/Casualties/Fatalities Aggregated by Month~Year')

table.plot(y='event', figsize=(15, 6), title='Events Aggregated by Month~Year')
table.plot(y=['nkill', 'nwound'], figsize=(15, 6), title='Casualties & Fatalities Aggregated by Month~Year')

### DESCRIPTIVE STATISTICS
isis['gname'].value_counts()
targtypes = pd.crosstab(isis['gname'], isis['targtype1_txt'])
attacktypes = pd.crosstab(isis['gname'], isis['attacktype1_txt'])
organizations = pd.crosstab(isis['gname'], isis['iyear'])
attackfatality = isis.groupby('attacktype1_txt')['nkill'].sum().sort_values(ascending=False)
isis['success'].describe()
isis.groupby(['gname'])['success'].mean().sort_values(ascending=False)
isis.groupby(['iyear'])['success'].mean()
isis.groupby(['gname'])['nkill'].mean().sort_values(ascending=False)

table2 = pd.crosstab(isis['gname'], isis['year'], values=isis['nkill'], aggfunc=np.mean)

table1 = isis.groupby(['iyear'])['success'].mean()
table2 = isis.groupby(['iyear'])['nkill'].mean()
table = pd.concat([table, table2], axis=1)
plt.scatter(table.index, table['success'])

### STATISTICAL DISTRIBUTIONS
plt.hist(is_df['iyear'])
is_df['iday'].hist(by=is_df['gname'], figsize=(17, 17), sharex=True)

### ANNUAL ATTACKS PLOTTING
annual_attacks = pd.crosstab(isis['iyear'], isis['gname'])
annual_attacks.plot(figsize=(15, 6))
plt.title('Islamic State Attacks by Year 2001-2019', size=15)

### TARGET TREND
annual_targets = pd.crosstab(isis['year'], isis['targtype1_txt'])
annual_targets.plot.bar(figsize=(15, 6))

### ATTACK TYPE TREND
annual_methods = pd.crosstab(isis['year'], isis['attacktype1_txt'])
annual_methods.plot.bar(figsize=(15, 6))

###### CUMULATIVE SUM OF ATTACKS
table = isis['date'].value_counts()
table = pd.DataFrame(table)
table = table.rename(columns={'date': 'move'})
table['date'] = table.index
table['sum'] = table['move']
table = table.drop(columns=['move'])
table = table.sort_values(by='date')
table = table.reset_index(drop=True)
table['Total'] = table['sum'].cumsum()

### ISIL
isil = isis.loc[isis['gname'] == 'Islamic State of Iraq and the Levant (ISIL)']
table2 = isil['date'].value_counts()
table2 = pd.DataFrame(table2)
table2 = table2.rename(columns={'date': 'move'})
table2['date'] = table2.index
table2['sum'] = table2['move']
table2 = table2.drop(columns=['move'])
table2 = table2.sort_values(by='date')
table2 = table2.reset_index(drop=True)
table2['ISIL'] = table2['sum'].cumsum()

### TRIPOLI
trip = isis.loc[isis['gname'] == 'Tripoli Province of the Islamic State']
table = trip['date'].value_counts()
table = pd.DataFrame(table)
table = table.rename(columns={'date': 'move'})
table['date'] = table.index
table['sum'] = table['move']
table = table.drop(columns=['move'])
table = table.sort_values(by='date')
table = table.reset_index(drop=True)
table['Tripoli'] = table['sum'].cumsum()

table1 = table

f, ax = plt.subplots(1, figsize=(10, 10))
table1.plot(x='date', y='Total', ax=ax)
table2.plot(x='date', y='ISIL', ax=ax)
table3.plot(x='date', y='Tripoli', ax=ax)
plt.title('Total Attacks by ISIS 2013-2019')
plt.xlabel('Date')
plt.ylabel('Number of Attacks')

### DENSITY PLOTTING
isis = isis[isis['longitude'].notna()]
isis = isis[isis['latitude'].notna()]
xy = np.vstack([isis.longitude, isis.latitude])
z = gaussian_kde(xy)(xy)

f, ax = plt.subplots(figsize=(15, 15))
libya.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
egypt.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
algeria.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
morocco.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
tunisia.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
iraq.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
syria.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
israel.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
syria.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
saudi_arabia.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
jordan.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
yemen.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
lebanon.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
ax.scatter(isis['longitude'], isis['latitude'], c=z)
plt.title('Islamic State Attacks in MENA 2013-2019', size=15)

f, ax = plt.subplots(figsize=(15, 15))
world.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
ax.scatter(isis['longitude'], isis['latitude'], c=z)
plt.title('Islamic State Attacks in MENA Region 2013-2019', size=15)

### GROUP PLOTTING
colors = {'Sinai Province of the Islamic State': 'red', 'Algerian Islamic Extremists': 'green',
          'Tripoli Province of the Islamic State': 'blue',
          'Barqa Province of the Islamic State': 'yellow', 'Islamic State of Iraq and the Levant (ISIL)': 'orange',
          'Fezzan Province of the Islamic State': 'brown'}
f, ax = plt.subplots(figsize=(15, 15))
libya.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
egypt.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
algeria.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
morocco.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
tunisia.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
ax.scatter(is_df['longitude'], is_df['latitude'], c=is_df['gname'].map(colors))
plt.title('Islamic State Attacks by Groups 2001-2019', size=15)

### SUCCESS PLOTTING
colors = {1: 'green', 0: 'red'}
f, ax = plt.subplots(figsize=(15, 15))
libya.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
egypt.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
algeria.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
morocco.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
tunisia.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
iraq.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
syria.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
israel.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
syria.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
saudi_arabia.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
jordan.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
yemen.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
lebanon.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
ax.scatter(isis['longitude'], isis['latitude'], c=isis['success'].map(colors))
plt.title('Successful Islamic State Attacks 2013-2019', size=15)

### SUCCESS PLOTTING IRAQ/SYRIA
colors = {1: 'green', 0: 'red'}
isil = isis.loc[(isis['country_txt'] == 'Iraq') | (isis['country_txt'] == 'Syria')]
f, ax = plt.subplots(figsize=(15, 15))
iraq.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
syria.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
ax.scatter(isil['longitude'], isil['latitude'], c=isil['success'].map(colors))
plt.title('Successful Islamic State Attacks 2013-2019', size=15)

### RANDOM FOREST MODEL
RandomForest = pd.get_dummies(is_df,
                              columns=['attacktype1_txt', 'targtype1_txt', 'targsubtype1_txt', 'provstate', 'gname'])
RandomForest = RandomForest.drop(columns=['country_txt', 'region_txt', 'eventid', 'imonth', 'iday', 'city', 'latitude',
                                          'longitude', 'summary', 'corp1', 'target1', 'region', 'suicide', 'claimed',
                                          'weapsubtype1_txt', 'weapdetail', 'property',
                                          'natlty1_txt', 'weaptype1_txt', 'nkillter', 'nwound', 'propextent_txt',
                                          'propextent'])
RandomForest['nkill'] = RandomForest['nkill'].fillna(0)
RandomForest = RandomForest.reset_index(drop=True)

X = RandomForest.drop(columns=['success'])
y = RandomForest['success']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

metrics.accuracy_score(y_test, y_pred)  # 91.93% accuracy
metrics.confusion_matrix(y_test, y_pred)
table = metrics.classification_report(y_test, y_pred)
importances = clf.feature_importances_

### Clean up MENA dataset
### Apply Random Forest model
### Plot nodes

group_table = pd.crosstab(mena_df['gname'], mena_df['iyear'])
mena_df['attacktype1_txt'].value_counts()
mena_df['targtype1_txt'].value_counts()
mena_df['natlty1_txt'].value_counts()

####### Plotting
f, ax = plt.subplots(figsize=(10, 10))
libya.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
egypt.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
ax.scatter(libya_egypt_df['longitude'], libya_egypt_df['latitude'], c=libya_egypt_df['gname'])

le_df = libya_egypt_df.loc[(libya_egypt_df['gname'] == 'Sinai Province of the Islamic State') |
                           (libya_egypt_df['gname'] == 'Tripoli Province of the Islamic State') |
                           (libya_egypt_df['gname'] == 'Muslim extremists') |
                           (libya_egypt_df['gname'] == 'ABarqa Province of the Islamic State') |
                           (libya_egypt_df['gname'] == 'Ansar al-Sharia (Libya)') |
                           (libya_egypt_df['gname'] == 'Ansar Bayt al-Maqdis (Ansar Jerusalem)') |
                           (libya_egypt_df['gname'] == 'Muslim Brotherhood') |
                           (libya_egypt_df['gname'] == 'Fezzan Province of the Islamic State') |
                           (libya_egypt_df['gname'] == 'Ajnad Misr')]

## colors = {'North America':'red', 'Europe':'green', 'Asia':'blue', 'Australia':'yellow'}

rf_df = pd.get_dummies(le_df, columns=['attacktype1_txt', 'targtype1_txt', 'provstate'])
rf_df = rf_df.drop(columns=['country_txt', 'region_txt', 'eventid', 'imonth', 'iday', 'city', 'latitude',
                            'longitude', 'summary', 'targsubtype1_txt', 'corp1', 'target1',
                            'natlty1_txt', 'weaptype1_txt', 'nkillter', 'nwound', 'propextent_txt', 'addnotes'])
rf_df['nkill'] = rf_df['nkill'].fillna(0)
rf_df = rf_df.reset_index(drop=True)

X = rf_df.drop(columns=['gname'])
y = rf_df['gname']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
metrics.accuracy_score(y_test, y_pred)
# 87.02% accuracy

metrics.confusion_matrix(y_test, y_pred)
metrics.classification_report(y_test, y_pred)

X1 = X_test[0:1]

########################################################################################
aqim = df.loc[(df['gname'] == 'Al-Qaida in the Islamic Maghreb (AQIM)')]
aqim.describe()
attack_table = pd.crosstab(aqim['gname'], aqim['attacktype1_txt']) / aqim['attacktype1_txt'].value_counts().sum()
region_table = pd.crosstab(aqim['gname'], aqim['region_txt']) / aqim['region_txt'].value_counts().sum()
target_table = pd.crosstab(aqim['gname'], aqim['targtype1_txt']) / aqim['targtype1_txt'].value_counts().sum()
country_table = pd.crosstab(aqim['gname'], aqim['country_txt'])
year_table = pd.crosstab(aqim['gname'], aqim['iyear'])

algeria = df.loc[(df['country_txt'] == 'Algeria')]
algeria['gname'].value_counts()

#### Classification ML Model to determine responsible terrorist organization
import sklearn
import sklearn.model_selection
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

new_islam_terr = pd.get_dummies(islam_terr, columns=['region_txt', 'country_txt', 'attacktype1_txt', 'targtype1_txt'])
new_islam_terr = new_islam_terr.drop(columns=['eventid', 'imonth', 'iday', 'provstate', 'city', 'latitude',
                                              'longitude', 'summary', 'targsubtype1_txt', 'corp1', 'target1',
                                              'natlty1_txt', 'weaptype1_txt', 'nkillter', 'nwound', 'propextent_txt',
                                              'addnotes'])
new_islam_terr['nkill'] = new_islam_terr['nkill'].fillna(0)
new_islam_terr = new_islam_terr.reset_index(drop=True)

X = new_islam_terr.drop(columns=['gname'])
y = new_islam_terr['gname']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
metrics.accuracy_score(y_test, y_pred)

### X = year, region -> 68.799% accuracy
### X = year, region, country -> 99.649% accuracy
### X = year, region, country, attack_type -> 99.458% accuracy
### X = year, region, country, attack_type, target_type -> 99.395% accuracy

test_X = X[6479:6480]
clf.predict(test_X)
