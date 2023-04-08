import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Loading in all three datasets.
oef_hoa = pd.read_csv(r'C:\Users\slaye\Documents\KSU\Research_F22\datasets\oef_hoa.csv')
oef_p = pd.read_csv(r'C:\Users\slaye\Documents\KSU\Research_F22\datasets\oef_p.csv')
oef_ts = pd.read_csv(r'C:\Users\slaye\Documents\KSU\Research_F22\datasets\oef_ts.csv')

# Loading in newly created probability datasets.
prob_hoa = pd.read_csv(r'C:\Users\slaye\Documents\KSU\Research_F22\datasets\prob_hoa.csv')
prob_p = pd.read_csv(r'C:\Users\slaye\Documents\KSU\Research_F22\datasets\prob_p.csv')
prob_ts = pd.read_csv(r'C:\Users\slaye\Documents\KSU\Research_F22\datasets\prob_ts.csv')

# Dropping the unneeded logistic output columns.
prob_hoa = prob_hoa.drop(columns=["eventid", "_POST_", "Residual", "Pearson", "Xbeta", "_ROLE_"])
prob_p = prob_p.drop(columns=["eventid", "_POST_", "Residual", "Pearson", "Xbeta", "_ROLE_"])
prob_ts = prob_ts.drop(columns=["eventid", "_POST_", "Residual", "Pearson", "Xbeta", "_ROLE_"])

# Appending the three regional datasets into one dataset.
prob_hoa["Mission"] = "HOA"
prob_p["Mission"] = "Philippines"
prob_ts["Mission"] = "TransSahara"
prob_grouped = prob_hoa.append([prob_p, prob_ts])

# Replacing variable level names with more concise names.
prob_grouped = prob_grouped.replace(
    ['Bombing/Explosion', 'Facility/Infrastructure Attack', 'Hostage Taking (Barricade Incident)',
     'Hostage Taking (Kidnapping)'],
    ['Bombing', 'Facility/Infrastructure', 'Hostage (Barricade)', 'Hostage (Kidnapping)'])
prob_grouped = prob_grouped.replace(
    ['Government (Diplomatic)', 'Government (General)', 'Religious Figures/Institutions', 'Journalists & Media',
     'Terrorists/Non-State Militia', 'Educational Institution', 'Private Citizens & Property'],
    ['Diplomatic', 'Government', 'Religious Institutions', 'Journalists', 'Terrorists/Militias', 'Education',
     'Private Citizens'])
prob_grouped = prob_grouped.replace(
    ['Al-Qaida in the Islamic Maghreb (AQIM)', 'Jamaat Nusrat al-Islam wal Muslimin (JNIM)'],
    ['Al-Qaida (AQIM)', 'Nusrat al-Islam (JNIM)'])
prob_grouped['suicide'] = prob_grouped['suicide'].replace([0, 1], ['Non-suicide', 'Suicide'])
prob_grouped['vicinity'] = prob_grouped['vicinity'].replace([0, 1], ['Outskirts of City', 'Inside City'])


# %%


# Point Plots to examine average predicted probabilities of success for each predictor variable.
def point_plots():
    font_size_labels = 18
    font_size_title = 22
    x_ticks_size = 12
    ylab = "Probability of Success"

    # SUICIDE
    plt.figure(figsize=(7, 8))  # (6, 7) Analytics Day, (6, 6.5) C-Day, (6, 6.5) Harvard, (7, 8) NCUR
    sns.pointplot(x='suicide', y='Pred', data=prob_grouped, estimator='median', errorbar=None, hue='Mission',
                  palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"))
    plt.xticks(rotation=0, fontsize=x_ticks_size)
    plt.xlabel("SUICIDE INDICATOR", fontsize=font_size_labels)
    plt.ylabel(ylab, fontsize=font_size_labels)
    plt.grid(axis='both', color='gray', linestyle='dashed', alpha=0.3)
    plt.title("Figure 10: Point Plot of Median\nPredicted Probabilities of Success\nfor Suicide Attacks by Mission",
              fontsize=font_size_title)
    plt.show()

    # VICINITY
    plt.figure(figsize=(7, 8))  # (6, 7) Analytics Day, (6, 6.5) C-Day, (6, 6.5) Harvard, (7, 8) NCUR
    sns.pointplot(x='vicinity', y='Pred', data=prob_grouped, estimator='median', errorbar=None, hue='Mission',
                  palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"))
    plt.xticks(rotation=0, fontsize=x_ticks_size)
    plt.xlabel("IN THE CITY INDICATOR", fontsize=font_size_labels)
    plt.ylabel(ylab, fontsize=font_size_labels)
    plt.grid(axis='both', color='gray', linestyle='dashed', alpha=0.3)
    plt.title("Figure 9: Point Plot of Median Predicted\nProbabilities of Success for\nCity Vicinity by Mission",
              fontsize=font_size_title)
    plt.show()

    # ATTACKTYPE
    plt.figure(figsize=(9.5, 6.15))  # (6, 6.5) Analytics Day, (13, 4.5) C-Day, (10, 5.5) Harvard, (9.5, 6.15) NCUR
    prob_grouped_attack = prob_grouped[(prob_grouped['attacktype1'] != "Unknown")]
    sns.pointplot(x='attacktype1', y='Pred', data=prob_grouped_attack, estimator='median', errorbar=None, hue='Mission',
                  palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"),
                  order=['Assassination', 'Armed Assault', 'Bombing', 'Hijacking',
                         'Hostage (Kidnapping)', 'Facility/Infrastructure',
                         'Unarmed Assault', 'Hostage (Barricade)'])
    plt.xticks(rotation=45, fontsize=x_ticks_size)
    plt.xlabel("ATTACK TYPES", fontsize=font_size_labels)
    plt.ylabel(ylab, fontsize=font_size_labels)
    plt.grid(axis='both', color='gray', linestyle='dashed', alpha=0.3)
    plt.title("Figure 5: Point Plot of Median Predicted Probabilities\nof Success for Attack Type by Mission",
              fontsize=font_size_title)
    plt.show()

    # WEAPTYPE
    plt.figure(figsize=(11.75, 6))  # (6, 6.5) Analytics Day, (6, 6.5) C-Day, (9, 4.5) Harvard, (11.75, 6) NCUR
    prob_grouped_weap = prob_grouped[(prob_grouped['weaptype1'] != "Unknown") & (prob_grouped['weaptype1'] != "Other")]
    sns.pointplot(x='weaptype1', y='Pred', data=prob_grouped_weap, estimator='median', errorbar=None, hue='Mission',
                  palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"),
                  order=['Biological', 'Fake Weapons', 'Explosives', 'Firearms', 'Sabotage Equipment', 'Melee',
                         'Incendiary', 'Chemical'])
    plt.xticks(rotation=45, fontsize=x_ticks_size)
    plt.xlabel("WEAPON TYPES", fontsize=font_size_labels)
    plt.ylabel(ylab, fontsize=font_size_labels)
    plt.grid(axis='both', color='gray', linestyle='dashed', alpha=0.3)
    plt.title("Figure 2: Point Plot of Median Predicted Probabilities of\nSuccess for Weapon Type by Mission",
              fontsize=font_size_title)
    plt.show()

    # GNAME
    plt.figure(figsize=(13.55, 5.3))  # (13.5, 4) Analytics Day, (13, 4.5) C-Day, (9, 4.5) Harvard, (13.55, 5.3) NCUR
    prob_grouped_gname = prob_grouped[(prob_grouped['gname'] != "Unknown")]
    sns.pointplot(x='gname', y='Pred', data=prob_grouped_gname, estimator='median', errorbar=None, hue='Mission',
                  palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"),
                  order=["New People's Army (NPA)", 'Moro Insurgents', 'Abu Sayyaf Group (ASG)',
                         'Islamic Extremists', 'Nusrat al-Islam (JNIM)', 'Boko Haram',
                         'Al-Qaida (AQIM)', 'Fulani extremists', 'Al-Shabaab',
                         'Political Organization', 'Regional Militias/Tribes', 'Janjaweed'])
    plt.xticks(rotation=45, fontsize=x_ticks_size)
    plt.xlabel("TERRORIST GROUPS", fontsize=font_size_labels)
    plt.ylabel(ylab, fontsize=font_size_labels)
    plt.grid(axis='both', color='gray', linestyle='dashed', alpha=0.3)
    plt.title("Figure 7: Point Plot of Median Predicted Probabilities of\nSuccess for Terrorist Group by Mission",
              fontsize=font_size_title)
    plt.show()

    # COUNTRY
    plt.figure(figsize=(13.55, 5.3))  # (13.5, 4) Analytics Day, (13, 4.5) C-Day, (9, 4.5) Harvard, (13.55, 5.3) NCUR
    sns.pointplot(x='country', y='Pred', data=prob_grouped, estimator='median', errorbar=None, hue='Mission',
                  palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"),
                  order=['Mauritania', 'Tunisia', 'Algeria', 'Burkina Faso', 'Mali', 'Nigeria', 'Cameroon',
                         'Niger', 'Chad', 'Senegal', 'Morocco', 'Kenya', 'Somalia', 'Sudan', 'Ethiopia',
                         'Djibouti', 'Eritrea'])
    plt.xticks(rotation=45, fontsize=x_ticks_size)
    plt.xlabel("COUNTRIES", fontsize=font_size_labels)
    plt.ylabel(ylab, fontsize=font_size_labels)
    plt.grid(axis='both', color='gray', linestyle='dashed', alpha=0.3)
    plt.title("Figure 6: Point Plot of Median Predicted Probabilities of\nSuccess for Country by Mission",
              fontsize=font_size_title)
    plt.show()

    # TARGTYPE
    plt.figure(figsize=(13.75, 5.35))  # (13.5, 4) Analytics Day, (13, 4.5) C-Day, (10, 5.5) Harvard, (13.75, 5.35) NCUR
    prob_grouped_targ = prob_grouped[(prob_grouped['targtype1'] != "Unknown") & (prob_grouped['targtype1'] != "Other")]
    sns.pointplot(x='targtype1', y='Pred', data=prob_grouped_targ, estimator='median', errorbar=None, hue='Mission',
                  palette=dict(HOA="#EBE4A9", Philippines="#7CA5BE", TransSahara="#F3BE9E"),
                  order=['Diplomatic', 'Airports & Aircraft', 'Maritime', 'Government', 'Utilities',
                         'Journalists', 'Education', 'NGO', 'Tourists', 'Military',
                         'Transportation', 'Religious Institutions', 'Private Citizens',
                         'Business', 'Telecommunication', 'Police', 'Food or Water Supply',
                         'Violent Political Party', 'Terrorists/Militias'])
    plt.xticks(rotation=45, fontsize=x_ticks_size)
    plt.xlabel("TARGET TYPES", fontsize=font_size_labels)
    plt.ylabel(ylab, fontsize=font_size_labels)
    plt.grid(axis='both', color='gray', linestyle='dashed', alpha=0.3)
    plt.title("Figure 8: Point Plot of Median Predicted Probabilities\nof Success for Target Type by Mission",
              fontsize=font_size_title)
    plt.show()

    return ()


point_plots()