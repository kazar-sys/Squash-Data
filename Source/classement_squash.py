##########################################################################################



##########################################################################################



##########################################################################################



########## CALCUL DU NOMBRE DE POINTS CLASSEMENT SQUASH A LA DATE D'AUJOURD'HUI ##########



##########################################################################################



##########################################################################################



##########################################################################################







import pandas as pd



import matplotlib.pyplot as plt



from datetime import datetime, timedelta



from scipy.interpolate import interp1d



import numpy as np







### TRAITEMENT DES DONNEES







# Chemin vers votre fichier Excel

excel_file = "Data/Actions Simon.xlsx"



# Lire le fichier Excel

df = pd.read_excel(excel_file)



# Liste pour stocker les données

donnees = []



# Parcourir chaque ligne du DataFrame

for index, row in df.iterrows():

    # Ajouter la ligne à la liste de données
    if row['Points'] == int(row['Points']):
        donnees.append({'Points': int(row['Points']), 'Date': row['Date'], 'Expired': False, 'Type': row['Type de tournoi'], 'Localisation': row['Type de points']})
    else:
        donnees.append({'Points': float(row['Points']), 'Date': row['Date'], 'Expired': False, 'Type': row['Type de tournoi'], 'Localisation': row['Type de points']})



# Stocker les % de victoires et de défaites

win_rate = df.iloc[0]["Total Gagnés"]

lose_rate = df.iloc[0]["Total Perdus"]

rates = [win_rate, lose_rate]

labels = ["Pourcentage de victoires", "Pourcentage de défaites"]



# On met les actions de plus d'un an à expired=True



for row in donnees:



    if row['Date'] < datetime.now() - timedelta(days=365):



        row['Expired'] = True





#print(donnees)

# Afficher les actions enregistrées



print("\n", "Les actions enregistrées sont : ", "\n")



count = 0



for row in donnees:



    print(row['Points'], datetime.strftime(row['Date'], "%Y/%m/%d"), row['Expired'], row['Type'])



    count += 1







# Affichage du nombre total d'actions



print("\n", "Nombre Total d'actions : ", count,"\n")











### CALCUL DE LA MOYENNE DES POINTS







# Comptage du nombre d'actions



count = 0



for row in donnees:



    if not row['Expired']:



        count += 1







# Comptage du nombre d'actions de type Promotion retenues et suppression de l'excès (pas plus de 4)



nb_action_promotion = 0



for action in donnees:



    if action['Type'] == "Promotion":



        nb_action_promotion += 1



excess = max(0, nb_action_promotion-4)







# Filtrer les éléments de type 'Promotion'



promotions = [item for item in donnees if item['Type'] == 'Promotion']







# Trier les éléments de type 'Promotion' par points décroissants



promotions_sorted = sorted(promotions, key=lambda x: x['Points'], reverse=True)







# Supprimer les éléments de type 'Promotion' de la liste principale



for i in range(excess):



    donnees.remove(promotions_sorted[i])







# Création d'une liste avec les X meilleures actions, X dépend du nombre d'actions valides



best_actions = list()







if count < 12:



    print("\n", "Renseigner au moins 12 actions toujours valides SVP", "\n")



elif 12 <= count <= 15:



    target = 12



elif 16 <= count <= 19:



    target = 13



elif 20 <= count <= 23:



    target = 14



elif 24 <= count <= 27:



    target = 15



elif 28 <= count <= 31:



    target = 16



elif 32 <= count <= 35:



    target = 17



else:



    target = 18







while len(best_actions) < target:



    min_points = donnees[0]['Points']



    index = 0



    for i in range(1, len(donnees)):



        if donnees[i]['Points'] < min_points and not donnees[i]['Expired']:



            min_points = donnees[i]['Points']



            index = i







    best_actions.append(donnees[index])



    donnees.pop(index)







# Calcul de la moyenne de points



moy = 0



for action in best_actions:



    moy += action['Points']



moy /= target



moy = round(moy, 2)















### Calcul du niveau de classement







# Les valeurs y et leurs légendes (Rang Hommes min et max de chaque classement)



levels = [



    (5480.01, 7436, "5D"),



    (4150.01, 5480, "5C"),



    (3200.01, 4150, "5B"),



    (2505.01, 3200, "5A"),



    (1985.01, 2505, "4D"),



    (1590.01, 1985, "4C"),



    (1270.01, 1590, "4B"),



    (1000.01, 1270, "4A"),



    (770.01, 1000, "3D"),



    (575.01, 770, "3C"),



    (415.01, 575, "3B"),



    (285.01, 415, "3A"),



    (185.01, 285, "2D"),



    (110.01, 185, "2C"),



    (60.01, 110, "2B"),



    (32.01, 60, "2A"),



    (12.01, 32, "1N"),



    (1, 12, "1I")



]







# Calcul du niveau de classement



i = 0



for element in levels:



    if element[0] <= moy <= element[1]:



        level_player = element[2]



        index_level_player = i



        break



    i += 1







thresholds = [element[1] for element in levels]



level = [element[2] for element in levels]









### Calcul du rang en fonction du nombre de points







# Données Rang Hommes et Moyenne



data_classements = [

    [1, 1],

    [12, 11.42],

    [13, 12],

    [32, 30],

    [33, 31.2],

    [60, 55.67],

    [61, 55.82],

    [90, 87.39],

    [110, 103.21],

    [111, 103.43],

    [111, 103.43],   

    [140, 129.33],

    [185, 187.75],

    [186, 189.53],

    [220, 227.08],

    [250, 254.08],

    [285, 290.42],

    [286, 291.19],

    [320, 323],

    [350, 344.67],

    [380, 373.25],

    [415, 401.17],

    [416, 402.22],

    [440, 427.08],

    [470, 457.59],

    [500, 494.08],

    [530, 522.85],

    [560, 545.92],

    [575, 558.42],

    [576, 561.08],

    [600, 600.35],

    [630, 632.76],

    [660, 658.35],

    [690, 687.5],

    [720, 715.59],

    [750, 740.45],

    [770, 764.83],

    [771, 765.67],

    [800, 793.58],

    [830, 824],

    [860, 856.2],

    [890, 897.5],

    [920, 937.5],

    [950, 956],

    [980, 984.1],

    [1000, 998.36],

    [1001, 998.42],

    [1270, 1306.5],

    [1271, 1308.25],

    [1590, 1663.2],

    [1591, 1664],

    [1985, 2194.92],

    [1986, 2195.07],

    [2505, 2927.77],

    [2506, 2928.5],

    [3200, 4043.17],

    [3201, 4043.57],

    [4150, 5538.33],

    [4151, 5539.72],

    [5480, 7479.62],

    [5481, 7482.25],

    [7436, 9317]

]







# Suppression des données en double (même nombre de points)



seen_values = set()



result = []



for sublist in data_classements:



    if sublist[1] not in seen_values:



        result.append(sublist)



        seen_values.add(sublist[1])







# Création d'une liste tab_x des nombres de points, d'une liste tab_y des classements correspondants



tab_x, tab_y = [element[1] for element in result], [element[0] for element in result]







# Création de la fonction d'interpolation



f_interp = interp1d(tab_x, tab_y, fill_value='extrapolate')







# Création de nos deux listes, le classement en fonction du nombre de points



nb_points = tab_x



classement = []



for i in range(len(nb_points)):



    classement.append(round(f_interp(nb_points[i]).item(), 0))











### CREATION DES GRAPHIQUES







# Graphique des paliers de classements 







# Définir les points x (3000 points)



x = range(3000)







# Indices des paliers à tracer



indices_to_plot = [index_level_player - 1, index_level_player, index_level_player + 1, index_level_player + 2, index_level_player + 3]









# Choisir les couleurs

background_color = '#f4f1de'  # Beige Clair

line_color = '#1f4e78'  # Bleu Marine



# Création de la figure et des axes

fig = plt.figure(figsize=(12, 12))



# Titre global pour la page entière

fig.suptitle('Classement du joueur', fontsize=12, fontweight='bold', y=1.001)



# Premier subplot (en haut)

ax1 = plt.subplot(3, 1, 1)  # Notez que maintenant nous avons 3 sous-graphiques au lieu de 2

ax1.set_facecolor(background_color)



# Tracer les droites horizontales spécifiques et ajouter les légendes en gras

for idx in indices_to_plot:

    if 0 <= idx < len(thresholds):  # Vérifier si l'indice est valide

        y = thresholds[idx]

        label = level[idx]

        ax1.plot(x, [y] * len(x), color=line_color)

        ax1.text(len(x) + 20, y - 50, label, fontsize=10, fontname='verdana', weight='bold', verticalalignment='bottom', color=line_color)  # Ajuster la position du texte



# Ajouter le point spécifique

ax1.plot(x[int(len(x)/2)], moy, 'ko')



# Ajouter une annotation pour le point

annotation_text = "Joueur : " + str(moy) +  " Points"

ax1.text(x[int(len(x)/2)] + 50, moy - 0.0027*moy, annotation_text, fontsize=8, color='k', weight='bold', fontname='verdana', verticalalignment='center', horizontalalignment='left')



# Enlever les graduations de l'axe x

ax1.set_xticks([])  # Enlève les graduations

ax1.set_xticklabels([])  # Enlève les étiquettes des graduations



# Ajouter les labels des axes

ax1.set_ylabel('Points du joueur')



# Configurer les limites des axes

ax1.set_xlim(0, 3000)

ax1.set_ylim(thresholds[index_level_player + 3] - 100, thresholds[index_level_player - 1] + 100)



### CREATION DU DEUXIEME GRAPHIQUE ###



# Deuxième subplot (au milieu)

ax2 = plt.subplot(3, 1, 2)

ax2.set_facecolor(background_color)



# Tracer la courbe représentant le classement en fonction du nombre de points

fine_points = np.linspace(min(nb_points), max(nb_points), 1000)  # Créer un ensemble de points fin pour la courbe

smooth_classement = f_interp(fine_points)  # Interpoler pour obtenir les classements correspondants



# Tracé de la courbe

ax2.plot(fine_points, smooth_classement, color='blue', label='Classement en fonction des points')



# Ajouter le point spécifique du joueur

ax2.scatter(moy, round(f_interp(moy).item(), 0), color='k', label='Point du joueur', s=20)



# Annotation pour le point spécifique

ax2.text(moy + 100, round(f_interp(moy).item(), 0) - 100,

         f'Classement du joueur : {int(f_interp(moy).item())}',

         fontsize=8, fontname='verdana', weight='bold', color='k')



# Ajouter les labels des axes

ax2.set_ylabel('Classement')

ax2.set_xlabel('Nombre de points')



# Ajouter une légende

ax2.legend()



# Troisième subplot (en bas) pour le pie chart

ax3 = plt.subplot(3, 1, 3)

ax3.set_facecolor(background_color)



# Tracer le pie chart

lightblue = "#ADD8E6"

cornflowerblue = "#6495ED"

ax3.pie(rates, labels=labels, colors=[lightblue, cornflowerblue], autopct='%1.1f%%')



# Ajuster l'espace entre les subplots

plt.subplots_adjust(hspace=0.3)  # Ajustement de l'espace vertical entre les sous-graphiques



# Ajustement automatique de la disposition

plt.tight_layout()







### AFFICHAGES FINAUX







# Affichage des meilleures actions prises en compte



print("\n", "Les", target, "meilleures actions qui ont été retenues sont :", "\n")



for action in best_actions:



    print(action['Points'], datetime.strftime(action['Date'], "%Y/%m/%d"), action['Type'], action['Localisation'])





# Calcul du rang du joueur

rank = int(f_interp(moy).item())



# Calcul du pourcentage du niveau de classement

percent_rank_level = int(round(100 * (moy - levels[index_level_player][0]) / (levels[index_level_player][1] - levels[index_level_player][0]), 0))



# Affichages finaux



print(f"\nClassement : {level_player} (Dans les {percent_rank_level} %)")

print(f"Rang : {rank}ème")

print(f"Moyenne : {str(moy).replace('.', ',')} points\n")



# Afficher le graphique



plt.show()