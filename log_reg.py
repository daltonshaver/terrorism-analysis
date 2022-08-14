import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import PoissonRegressor
from sklearn.utils import validation
from sklearn import metrics
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\gtd_sub.csv')
df = data.loc[(data['iyear'] >= 2001) & (data['country_txt'] == "Philippines")]
df = df.dropna(subset=['nkill'])
df = df.reset_index(drop=True)

y = df[['success']]
y = validation.column_or_1d(y)
X = df[['attacktype1_txt', 'targtype1_txt', 'targsubtype1_txt', 
        'weaptype1_txt', 'weapsubtype1_txt', 'suicide', 'gname', 'vicinity', 'nkill',
        'imonth', 'provstate']]
X = pd.get_dummies(X)


logreg = LogisticRegression()
logreg.fit(X, y)
logreg.score(X, y) #Accuracy

y_pred = logreg.predict(X)
metrics.confusion_matrix(y, y_pred)


'''
poireg = PoissonRegressor()
poireg.fit(X, y)
poireg.predict(X2)
        # Wildy inaccurate model, need to use zero-inflated model
        '''