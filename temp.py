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
#isis.to_csv(r'C:\Users\Slaye\Documents\Courses\STAT_3130\isis_gtdatabase.csv')

philippines = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\philippines.shp')




prob_hoa = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\prob_hoa.csv')
prob_hoa = prob_hoa.drop(["eventid"], axis=1)
prob_hoa = prob_hoa.drop_duplicates()
























################################# ISLAMIC STATE OF IRAQ AND SYRIA
#df = df.loc[df['iyear'] >= 2000]
#df['islamicState'] = df['gname'].str.find('Islamic')
#df.loc[df['islamicState'] >= 0, 'islamicState'] = 1
#df.loc[df['islamicState'] < 0, 'islamicState'] = 0
#df = df.loc[df['islamicState'] == 1]
# Boko Haram, Caucusus, Bangladesh, East Asia, Greater Sahara

isis = df.loc[(df['gname'] == 'Islamic State of Iraq and the Levant (ISIL)') | (df['gname'] == 'Sinai Province of the Islamic State') | 
              (df['gname'] == 'Tripoli Province of the Islamic State') | (df['gname'] == 'Barqa Province of the Islamic State') | 
              (df['gname'] == 'Hadramawt Province of the Islamic State') | (df['gname'] == 'Sanaa Province of the Islamic State') |
              (df['gname'] == 'Islamic State in Egypt') | (df['gname'] == 'Fezzan Province of the Islamic State') | 
              (df['gname'] == 'Najd Province of the Islamic State') | (df['gname'] == 'Algeria Province of the Islamic State') |
              (df['gname'] == 'Hijaz Province of the Islamic State') | (df['gname'] == 'Bahrain Province of the Islamic State') |
              (df['gname'] == 'Shabwah Province of the Islamic State') | (df['gname'] == 'Lahij Province of the Islamic State') |
              (df['gname'] == 'Al Bayda Province of the Islamic State')  | (df['gname'] == 'Adan-Abyan Province of the Islamic State')]
isis = isis.loc[isis['iyear'] >= 2013]
isis = isis.loc[isis['region'] == 10]
isis = isis.reset_index()
isis['event'] = 1

isis = isis.rename(columns = {'iyear':'year', 'imonth':'month', 'iday':'day'})
isis['date'] = pd.to_datetime(isis[['day', 'month', 'year']])
isis = isis.set_index('date')

### GROUP BY MONTH~YEAR
table = isis.groupby(pd.Grouper(freq="M")).sum()
table = table.drop(['index', 'eventid', 'year', 'month', 'day', 'region', 'latitude', 'longitude',
       'success', 'suicide', 'claimed', 'property', 'propextent'], axis=1)
table.plot(figsize=(15,6), title='Events/Casualties/Fatalities Aggregated by Month~Year')

table.plot(y='event', figsize=(15,6), title='Events Aggregated by Month~Year')
table.plot(y=['nkill', 'nwound'], figsize=(15,6), title='Casualties & Fatalities Aggregated by Month~Year')






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
is_df['iday'].hist(by=is_df['gname'], figsize=(17,17), sharex=True)

### ANNUAL ATTACKS PLOTTING
annual_attacks = pd.crosstab(isis['iyear'], isis['gname'])
annual_attacks.plot(figsize=(15,6))
plt.title('Islamic State Attacks by Year 2001-2019', size=15)

### TARGET TREND
annual_targets = pd.crosstab(isis['year'], isis['targtype1_txt'])
annual_targets.plot.bar(figsize=(15,6))

### ATTACK TYPE TREND
annual_methods = pd.crosstab(isis['year'], isis['attacktype1_txt'])
annual_methods.plot.bar(figsize=(15,6))


###### CUMULATIVE SUM OF ATTACKS
table = isis['date'].value_counts()
table = pd.DataFrame(table)
table = table.rename(columns = {'date':'move'})
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
table2 = table2.rename(columns = {'date':'move'})
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
table = table.rename(columns = {'date':'move'})
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

f, ax = plt.subplots(figsize=(15,15))
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


f, ax = plt.subplots(figsize=(15,15))
world.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
ax.scatter(isis['longitude'], isis['latitude'], c=z)
plt.title('Islamic State Attacks in MENA Region 2013-2019', size=15)


### GROUP PLOTTING
colors = {'Sinai Province of the Islamic State':'red', 'Algerian Islamic Extremists':'green', 'Tripoli Province of the Islamic State':'blue', 
          'Barqa Province of the Islamic State':'yellow', 'Islamic State of Iraq and the Levant (ISIL)':'orange', 'Fezzan Province of the Islamic State':'brown'}
f, ax = plt.subplots(figsize=(15,15))
libya.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
egypt.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
algeria.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
morocco.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
tunisia.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
ax.scatter(is_df['longitude'], is_df['latitude'], c=is_df['gname'].map(colors))
plt.title('Islamic State Attacks by Groups 2001-2019', size=15)

### SUCCESS PLOTTING
colors = {1:'green', 0:'red'}
f, ax = plt.subplots(figsize=(15,15))
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
colors = {1:'green', 0:'red'}
isil = isis.loc[(isis['country_txt'] == 'Iraq') | (isis['country_txt'] == 'Syria')]
f, ax = plt.subplots(figsize=(15,15))
iraq.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
syria.plot(color='lightyellow', ax=ax, edgecolor='black', linewidth=0.25)
ax.scatter(isil['longitude'], isil['latitude'], c=isil['success'].map(colors))
plt.title('Successful Islamic State Attacks 2013-2019', size=15)

















### RANDOM FOREST MODEL
RandomForest = pd.get_dummies(is_df, columns=['attacktype1_txt', 'targtype1_txt', 'targsubtype1_txt', 'provstate', 'gname'])
RandomForest = RandomForest.drop(columns=['country_txt', 'region_txt', 'eventid', 'imonth', 'iday', 'city', 'latitude',
       'longitude', 'summary', 'corp1', 'target1', 'region', 'suicide', 'claimed', 'weapsubtype1_txt', 'weapdetail', 'property',
       'natlty1_txt', 'weaptype1_txt', 'nkillter', 'nwound', 'propextent_txt', 'propextent'])
RandomForest['nkill'] = RandomForest['nkill'].fillna(0)
RandomForest = RandomForest.reset_index(drop=True)

X = RandomForest.drop(columns=['success'])
y = RandomForest['success']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

clf = RandomForestClassifier(n_estimators = 100)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

metrics.accuracy_score(y_test, y_pred) # 91.93% accuracy
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
f, ax = plt.subplots(figsize=(10,10))
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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)

clf = RandomForestClassifier(n_estimators = 100)
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
       'natlty1_txt', 'weaptype1_txt', 'nkillter', 'nwound', 'propextent_txt', 'addnotes'])
new_islam_terr['nkill'] = new_islam_terr['nkill'].fillna(0)
new_islam_terr = new_islam_terr.reset_index(drop=True)


X = new_islam_terr.drop(columns=['gname'])
y = new_islam_terr['gname']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)

clf = RandomForestClassifier(n_estimators = 100)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
metrics.accuracy_score(y_test, y_pred)


### X = year, region -> 68.799% accuracy
### X = year, region, country -> 99.649% accuracy
### X = year, region, country, attack_type -> 99.458% accuracy
### X = year, region, country, attack_type, target_type -> 99.395% accuracy

test_X = X[6479:6480]
clf.predict(test_X)


