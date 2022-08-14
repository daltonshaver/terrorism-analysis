import pandas as pd
from pomegranate import *
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\gtd_sub.csv')
df = data.loc[(data['iyear'] >= 2001) & (data['country_txt'] == "Philippines")]
df = df.reset_index(drop=True)
df['event'] = 1

table = df.groupby(['attacktype1_txt',
                    'targtype1_txt',
                    'targsubtype1_txt',
                    'suicide',
                    'weaptype1_txt',
                    'weapsubtype1_txt',
                    'vicinity',
                    'claimed'])['success', 'nkill'].mean()
table2 = df.groupby(['attacktype1_txt',
                    'targtype1_txt',
                    'targsubtype1_txt',
                    'suicide',
                    'weaptype1_txt',
                    'weapsubtype1_txt',
                    'vicinity',
                    'claimed'])['event', 'nkill'].sum()
table = pd.merge(table, table2, left_index=True, right_index=True)




X = df[['attacktype1_txt', 'targtype1_txt', 'targsubtype1_txt']]
X = X.dropna()

table = JointProbabilityTable.from_samples(X)
table.probability(('Bombing/Explosion', 'Military', 'Military Unit/Patrol/Convoy'))
        #I want the probabilities of success for each combination,
        #not the probability of a combination occuring.

