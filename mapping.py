import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

oef_p = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\oef_p.csv')
oef_hoa = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\oef_hoa.csv')
oef_ts = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\oef_ts.csv')

#%% Mapping

mapcolor_hoa = "#EBE4A9"
mapcolor_p = "#f4f0cf" #DEF0F7
mapcolor_ts = "#F3BE9E"
outsidecolor = "lightgrey"
countrylinewidth = 0.25
pointsize=5
success_colors = {0:'#FF0000', 1:'#7CAD91'} #cccccccc #b4d0c0

#Importing in Philippines shapefile
philippines = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\philippines\philippines.shp')

#Plotting Philippines
f, ax = plt.subplots(figsize=(14,20))
philippines.plot(color=mapcolor_p, ax=ax, edgecolor='black', linewidth=countrylinewidth)
ax.scatter(oef_p['longitude'], oef_p['latitude'], c=oef_p['success'].map(success_colors), s=pointsize)
        #Legend does not work.
        #Copy and paste the legend from 'groupBarChartCountry()' onto the map in word doc.

#Importing in Trans-Sahara shapefiles
algeria = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\trans_sahara\algeria.shp')
burkinafaso = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\trans_sahara\burkinafaso.shp')
cameroon = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\trans_sahara\cameroon.shp')
chad = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\trans_sahara\chad.shp')
mali = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\trans_sahara\mali.shp')
mauritania = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\trans_sahara\mauritania.shp')
morocco = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\trans_sahara\morocco.shp')
niger = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\trans_sahara\niger.shp')
nigeria = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\trans_sahara\nigeria.shp')
senegal = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\trans_sahara\senegal.shp')
tunisia = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\trans_sahara\tunisia.shp')

#Importing in countries surrounding Trans-Sahara and the Horn of Africa:
benin = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\outside_countries\benin.shp')
central_africa = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\outside_countries\central_africa.shp')
cote_divoire = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\outside_countries\cote_divoire.shp')
egypt = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\outside_countries\egypt.shp')
gambia = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\outside_countries\gambia.shp')
ghana = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\outside_countries\ghana.shp')
guinea = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\outside_countries\guinea.shp')
guinea_bissau = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\outside_countries\guinea_bissau.shp')
liberia = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\outside_countries\liberia.shp')
libya = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\outside_countries\libya.shp')
sierra_leone = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\outside_countries\sierra_leone.shp')
togo = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\outside_countries\togo.shp')
western_sahara = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\outside_countries\western_sahara.shp')

#Importing in Horn of Africa shapefiles
djibouti = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\horn_of_africa\djibouti.shp')
eritrea = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\horn_of_africa\eritrea.shp')
ethiopia = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\horn_of_africa\ethiopia.shp')
kenya = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\horn_of_africa\kenya.shp')
somalia = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\horn_of_africa\somalia.shp')
south_sudan = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\horn_of_africa\south_sudan.shp')
sudan = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\horn_of_africa\sudan.shp')

#*******RUN ALL BELOW AT ONCE*******
#Plotting Trans-Sahara countries
f, ax = plt.subplots(figsize=(28, 20))
algeria.plot(color=mapcolor_ts, ax=ax, edgecolor='black', linewidth=countrylinewidth)
burkinafaso.plot(color=mapcolor_ts, ax=ax, edgecolor='black', linewidth=countrylinewidth)
cameroon.plot(color=mapcolor_ts, ax=ax, edgecolor='black', linewidth=countrylinewidth)
chad.plot(color=mapcolor_ts, ax=ax, edgecolor='black', linewidth=countrylinewidth)
mali.plot(color=mapcolor_ts, ax=ax, edgecolor='black', linewidth=countrylinewidth)
mauritania.plot(color=mapcolor_ts, ax=ax, edgecolor='black', linewidth=countrylinewidth)
morocco.plot(color=mapcolor_ts, ax=ax, edgecolor='black', linewidth=countrylinewidth)
niger.plot(color=mapcolor_ts, ax=ax, edgecolor='black', linewidth=countrylinewidth)
nigeria.plot(color=mapcolor_ts, ax=ax, edgecolor='black', linewidth=countrylinewidth)
senegal.plot(color=mapcolor_ts, ax=ax, edgecolor='black', linewidth=countrylinewidth)
tunisia.plot(color=mapcolor_ts, ax=ax, edgecolor='black', linewidth=countrylinewidth)
ax.scatter(oef_ts['longitude'], oef_ts['latitude'], c=oef_ts['success'].map(success_colors), s=pointsize)
plt.legend()

#Plotting Horn of Africa countries
djibouti.plot(color=mapcolor_hoa, ax=ax, edgecolor='black', linewidth=countrylinewidth)
eritrea.plot(color=mapcolor_hoa, ax=ax, edgecolor='black', linewidth=countrylinewidth)
ethiopia.plot(color=mapcolor_hoa, ax=ax, edgecolor='black', linewidth=countrylinewidth)
kenya.plot(color=mapcolor_hoa, ax=ax, edgecolor='black', linewidth=countrylinewidth)
somalia.plot(color=mapcolor_hoa, ax=ax, edgecolor='black', linewidth=countrylinewidth)
south_sudan.plot(color=mapcolor_hoa, ax=ax, edgecolor='black', linewidth=countrylinewidth)
sudan.plot(color=mapcolor_hoa, ax=ax, edgecolor='black', linewidth=countrylinewidth)
ax.scatter(oef_hoa['longitude'], oef_hoa['latitude'], c=oef_hoa['success'].map(success_colors), s=pointsize)

#Plotting surrounding countries:
benin.plot(color=outsidecolor, ax=ax, edgecolor='black', linewidth=countrylinewidth)
central_africa.plot(color=outsidecolor, ax=ax, edgecolor='black', linewidth=countrylinewidth)
cote_divoire.plot(color=outsidecolor, ax=ax, edgecolor='black', linewidth=countrylinewidth)
egypt.plot(color=outsidecolor, ax=ax, edgecolor='black', linewidth=countrylinewidth)
gambia.plot(color=outsidecolor, ax=ax, edgecolor='black', linewidth=countrylinewidth)
ghana.plot(color=outsidecolor, ax=ax, edgecolor='black', linewidth=countrylinewidth)
guinea.plot(color=outsidecolor, ax=ax, edgecolor='black', linewidth=countrylinewidth)
guinea_bissau.plot(color=outsidecolor, ax=ax, edgecolor='black', linewidth=countrylinewidth)
liberia.plot(color=outsidecolor, ax=ax, edgecolor='black', linewidth=countrylinewidth)
libya.plot(color=outsidecolor, ax=ax, edgecolor='black', linewidth=countrylinewidth)
sierra_leone.plot(color=outsidecolor, ax=ax, edgecolor='black', linewidth=countrylinewidth)
togo.plot(color=outsidecolor, ax=ax, edgecolor='black', linewidth=countrylinewidth)
western_sahara.plot(color=outsidecolor, ax=ax, edgecolor='black', linewidth=countrylinewidth)

