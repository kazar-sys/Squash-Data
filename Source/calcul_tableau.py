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
        i = 0
        for games in tab:
            fichier.write(str(games[0]) + "\n" + str(games[1]) + "\n" + "\n")
            i += 1
            if i%2 == 0:
                fichier.write("\n")
                fichier.write("\n")
                fichier.write("\n")
    return None



# Input : liste de joueurs
nom_tournoi = "Tournoi de Blois 7 et 8 juin 2025"
joueurs = [
    "SERUSIER Jérôme 2A 47",
    "BENOIT Matthieu 2A 54",
    "PINEAU Jean-Jacques 2A 59",
    "BOULDOIRE Benjamin 2B 91",
    "ZARKA Fabien 2C 189",
    "PEREZ Thibault 2D 254",
    "FONTAINE Sylvain 2D 286",
    "PAILLER Kevin 3A 304",
    "LEROY Alexandre 2D 295",
    "HARRIAU Jules 3A 367",
    "MEZIANE Mehdi 3A 428",
    "LE COQ Franck 3B 480",
    "COTELLE Fabrice 3B 542",
    "ZARKA Simon 3B 580",
    "LOUP Jean-Baptiste 3C 659",
    "CRUZ Daniel 3C 667",
    "MAGIERA Oscar 3C 673",
    "SOULEILLAN Gregory 3C 695",
    "JULIAN Tristan 3C 668",
    "POTTIER Vincent 3C 711",
    "GARBIN Laurent 3C 721",
    "JORIS Florian 3C 732",
    "GUINE Yael 3C 754",
    "LUBINEAU Olivier 3D 793",
    "CLEMENT Paul 3D 840",
    "DEBAQUE Romuald 3D 869",
    "LECOQ Christophe 3D 924",
    "BOUTET Hugues 3D 950",
    "LAASAMI Naim 4B 1363",
    "TEMPLIER Maël 4B 1573",
    "BREUILLAUD Antoine 4B 1526",
    "MARTINEZ Maxime 4B 1562",
    "BONHOMME Sebastien 4B 1640",
    "GRANDPERRIN Jonathan 4B 1668",
    "CAYET Arnaud 4C 1693",
    "BULLIARD-JANNOT Tao 4C 1860",
    "JAMOT Edouard 4C 1873",
    "BILQUARD Jean-Chrales 4C 1903",
    "RENON Ludovic 4C 2068",
    "BRETON Philippe 4D 2518",
    "GUERIN Frederic 4D 2587",
    "CLEMENT Franck 4D 2776",
    "BOUTET Emmanuel 5A 3299",
    "MARTINEZ Guillaume 5A 3349",
    "LEROY Maurice 5C 5782",
    "MATHIEUX Nicolas 5D 7233"
]

createTab(joueurs, nom_tournoi)