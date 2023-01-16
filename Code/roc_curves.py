import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing ROC Curve datasets
roc_hoa = pd.read_csv(r'C:\Users\dalto\Documents\KSU\Research_F22\datasets\roc_hoa.csv')
roc_p = pd.read_csv(r'C:\Users\dalto\Documents\KSU\Research_F22\datasets\roc_p.csv')
roc_ts = pd.read_csv(r'C:\Users\dalto\Documents\KSU\Research_F22\datasets\roc_ts.csv')

# Creating an indicator variable of region, then appending the three datasets
roc_hoa["Mission"] = "HOA"
roc_p["Mission"] = "Philippines"
roc_ts["Mission"] = "TransSahara"
roc = roc_hoa.append([roc_p, roc_ts])

# Plotting the stratified ROC-AUC Curves for the three Logistic Regression Models
plt.figure(figsize=(6, 6))
ax = sns.lineplot(x="FPF", y="TPF", hue="Mission", data=roc, legend=True, lw=3, palette=dict(HOA="#EBE4A9",
                                                                                             Philippines="#7CA5BE",
                                                                                             TransSahara="#F3BE9E"))
plt.setp(ax.get_legend().get_texts())
plt.setp(ax.get_legend().get_title())
plt.title("Figure 1: ROC Curves For Three Logistic\nRegression Models Predicting Success", fontsize=18)
plt.xlabel("False Positive Rate (Sensitivity)", fontsize=15)
plt.xticks(fontsize=10)
plt.ylabel("True Positive Rate (1 - Specificity)", fontsize=15)
plt.yticks(fontsize=10)
