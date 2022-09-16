import pandas as pd

df = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\gtd_research.csv')

'''Cleaning variable entries in main dataset'''
df['claimed'] = df['claimed'].replace([-9], 0)



'''Creating subsets for each component of OEF being analyzed.'''
#Operation Freedom Eagle - OEF Philippines
oef_p = df.loc[(df['country'] == "Philippines")
                &
                (df['year'] > 2001)
                ]

#Operation Enduring Freedom - Horn of Africa
oef_hoa = df.loc[((df['country'] == "Djibouti") |
                 (df['country'] == "Eritrea") |
                 (df['country'] == "Ethiopia") |
                 (df['country'] == "Kenya") |
                 (df['country'] == "Seychelles") |
                 (df['country'] == "Somalia") |
                 (df['country'] == "Sudan"))
                 &
                 (df['year'] > 2001)
                 ]

#Operation Juniper Shield - OEF Trans-Sahara
oef_ts = df.loc[((df['country'] == "Algeria") |   
                (df['country'] == "Burkina Faso") |
                (df['country'] == "Cameroon") | 
                (df['country'] == "Chad") |
                (df['country'] == "Mali") |
                (df['country'] == "Mauritania") |
                (df['country'] == "Morocco") |
                (df['country'] == "Niger") |
                (df['country'] == "Nigeria") |
                (df['country'] == "Senegal") |
                (df['country'] == "Tunisia"))
                &
                (df['year'] > 2001)
                ]



'''Exporting the three seperate subsets of data'''
oef_p.to_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\oef_p0.csv')
oef_hoa.to_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\oef_hoa0.csv')
oef_ts.to_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\oef_ts0.csv')
