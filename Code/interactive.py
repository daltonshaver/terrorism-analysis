import pandas as pd
import geopandas as gpd
import folium
import matplotlib.pyplot as plt
import seaborn as sns

oef_p = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\oef_p.csv')
philippines = gpd.read_file(r'C:\Users\Slaye\Documents\KSU\Research_F22\shapefiles\philippines\philippines.shp')

oef_p2 = oef_p.dropna(subset=['latitude', 'longitude'])
oef_p2 = oef_p2.reset_index(drop=True)
#oef_p2 = oef_p2.loc[0:1000]
oef_p2['success'] = oef_p2['success'].replace([0, 1], ['red', 'green'])


coordinates = oef_p2[['latitude', 'longitude']]
coordinates = coordinates.values.tolist()

philippinesmap = folium.Map(location=[11.947, 123.195], zoom_start=7)
#clusters = folium.MarkerCluster().add_to(philippinesmap)
for point in range(0, len(oef_p2)):
    text = f"Group: <strong>{oef_p2['gname'][point]}</strong></br> \
             Target Type: <strong>{oef_p2['targtype1'][point]}</strong></br> \
             Attack Type: <strong>{oef_p2['attacktype1'][point]}</strong></br> \
             Weapon Type: <strong>{oef_p2['weaptype1'][point]}</strong></br> \
             Suicide: <strong>{oef_p2['suicide'][point]}</strong></br>"    
    
    folium.Circle(location=coordinates[point],
                        tooltip=text,
                        color=oef_p2['success'][point],
                        radius=50,
                        fill=True).add_to(philippinesmap)


philippinesmap.save('philippinesmap.html')
