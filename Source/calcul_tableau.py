from math import log2

def createTab(joueurs, nom_tournoi):
    
    if log2(len(joueurs)) == int(log2(len(joueurs))):
        n = 2**(int(log2(len(joueurs))))
    else:
        n = 2**(int(log2(len(joueurs))) + 1)

    tours = [[] for _ in range(int(log2(n)))]

    tours[0] = [[1, 2]]

    for i in range(1, len(tours)):
        
        for matchs in tours[i-1]:

            tours[i].append([matchs[0], 2**(i+1)+1-matchs[0]])
            tours[i].append([2**(i+1)+1-matchs[1], matchs[1]])

    
    for i in range(n-len(joueurs)):
        joueurs.append("Bye")

    tab = tours[-1]

    for game in tab:
        game[0] = "[" + str(game[0]) + "]" + " " + joueurs[game[0]-1]
        game[1] = "[" + str(game[1]) + "]" + " " + joueurs[game[1]-1]

    with open(f"Tableau {nom_tournoi}.txt", "w") as fichier:

        for games in tab:
            fichier.write(str(games[0]) + "\n" + str(games[1]) + "\n" + "\n")

    return None



# Input : liste de joueurs
nom_tournoi = "Tournoi de Blois 30 novembre"
joueurs = [
    "MERLAND RENAUD 3B 572",
    "JULIAN TRISTAN 3C 741",
    "MAGUERA OSCAR 3D 964",
    "BOUTET HUGUES 4A 1069",
    "GUINE YAEL 4A 1111",
    "CYRILE CHARLY 4A 1153",
    "LAVIELLE PASCAL 4A 1268",
    "ZARKA SIMON 4B 1603"
]

createTab(joueurs, nom_tournoi)