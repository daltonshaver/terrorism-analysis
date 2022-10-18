import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.utils import validation
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns


#Importing ROC Curve datasets
roc_hoa = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\roc_hoa.csv')
roc_p = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\roc_p.csv')
roc_ts = pd.read_csv(r'C:\Users\Slaye\Documents\KSU\Research_F22\datasets\roc_ts.csv')

#Creating an indicator variable of region, then appending the three datasets
roc_hoa["Mission"] = "HOA"
roc_p["Mission"] = "Philippines"
roc_ts["Mission"] = "TransSahara"
roc = roc_hoa.append([roc_p, roc_ts])

#Plotting the stratified ROC-AUC Curves for the three Logistic Regression Models
plt.figure(figsize=(14,14))
ax = sns.lineplot(x="FPF", y="TPF", hue="Mission", data=roc, legend=True, palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"), lw=3)
plt.setp(ax.get_legend().get_texts(), fontsize='16')
plt.setp(ax.get_legend().get_title(), fontsize='20')
plt.title("ROC Curves For Three Logistic Regression Models Predicting Success", fontsize=18)
plt.xlabel("False Positive Rate (Sensitivity)", fontsize=14)
plt.xticks(fontsize=12)
plt.ylabel("True Positive Rate (1 - Specificity)", fontsize=14)
plt.yticks(fontsize=12)


































y = oef_p[['success']]
y = validation.column_or_1d(y)
X = oef_p[['attacktype1', 'targtype1', 'weaptype1', 'suicide', 'gname', 'vicinity']]
X = pd.get_dummies(X)


logreg = LogisticRegression(class_weight='balanced')
logreg.fit(X, y)
#logreg.score(X, y) #Accuracy

y_pred = logreg.predict(X)
#logreg.get_params()
#metrics.confusion_matrix(y, y_pred)
metrics.roc_auc_score(y, y_pred)


'''
poireg = PoissonRegressor()
poireg.fit(X, y)
poireg.predict(X2)
        # Wildy inaccurate model, need to use zero-inflated model
       ''' 