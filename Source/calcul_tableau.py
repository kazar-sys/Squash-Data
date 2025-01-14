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

    with open(f"Tableaux/Tableau {nom_tournoi}.txt", "w") as fichier:

        for games in tab:
            fichier.write(str(games[0]) + "\n" + str(games[1]) + "\n" + "\n")

    return None



# Input : liste de joueurs
nom_tournoi = "Tournoi Verrières 19 janvier 2025"
joueurs = [
    "SOHEIB BAARIR 3B 499",
    "DANY VERY 3B 577",
    "VINCENT POTTIER 3C 721",
    "FRANCK LEDOUX 3C 784",
    "NICOLAS ZEVACO 3C 787",
    "BRUNO JUBERT 3D 801",
    "ARTHUR WAISBLAT 3D 879",
    "SIMON ZARKA 3D 880",
    "NICOLAS NGUYEN 3D 947",
    "GAEL DERRE 4A 10593",
    "LAURENT MARIE 4A 1138",
    "JEREMY ROUANNE 4A 1278",
    "STEPHANE DUBOIS 4B 1462",
    "CHISTOPHE LECHENNE 4B 1506",
    "ARNAUD GESTAT DE GARAMBE 4B 1555",
    "GARY ATTAL 4B 1590"
]

createTab(joueurs, nom_tournoi)