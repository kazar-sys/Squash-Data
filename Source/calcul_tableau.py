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
nom_tournoi = "Tournoi de Vincennes 13-14 décembre"
joueurs = [
    "TULLIS MALCOLM 2B 81",
    "BONHOMME THOMAS 2C 141",
    "ZRIHEN GUILLAUME 2C 191",
    "QUENNEHEN BORIS 2D 218",
    "BARBET JULES 2D 261",
    "LECOQ MARCEAU 2D 282",
    "MAUSSION JULIEN 3A 314",
    "CAYET LAURENT 3B 459",
    "DE ZEEUW JEAN-LUC 3B 462",
    "BEAU AXEL 3B 502",
    "PHAM-GIA VINH 3B 515",
    "SCHOCH GILLES 3B 541",
    "CANDUS EMMANUEL 3B 554",
    "RAMEAU NATHANIEL 3B 563",
    "VERY DANY 3B 581",
    "RAMEAU ADAM 3C 617",
    "MESSINESI PAUL 3C 625",
    "PIQUERAS JULES 3C 654",
    "LLEDO ANTOINE 3C 659",
    "ROUSSET ANTONIN 3C 677",
    "FAUTHOUX YOHAN 3D 792",
    "WAISBLAT ARTHUR 3D 907",
    "MOHAMMAD SAQUIB 3D 909",
    "ZARKA SIMON 3D 968"
]

createTab(joueurs, nom_tournoi)