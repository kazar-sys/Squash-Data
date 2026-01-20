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

    with open(f"tabs/Tableau {nom_tournoi}.txt", "w") as fichier:
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
    "SERUSIER Jerome 2A 40",
    "BENOIT Matthieu 2A 51",
    "PINEAU Jean-Jacques 2B 66",
    "BONNIN Titouan 2B 85",
    "BOULDOIRE Benjamin 2B 91",
    "GRISON Jules 2C 143",
    "ZARKA Fabien 2C 189",
    "GOMBERT Flavian 2D 213",
    "LEROY Alexandre 2D 281",
    "FONTAINE Sylvain 2D 285",
    "HARRIAU Jules 2D 288",
    "PAILLER Kevin 2D 294",
    "ROUGET Stéphane 3A 329",
    "MEZIANE Mehdi 3A 421",
    "LE COQ Franck 3B 468",
    "COTELLE Fabrice 3B 528",
    "ZARKA Simon 3B 557",
    "JULIAN Tristan 3C 616",
    "MAGIERA Oscar 3C 628",
    "CRUZ Daniel 3C 630",
    "GUINE Yael 3C 657",
    "POTTIER Vincent 3C 685",
    "JORIS Florian 3C 749",
    "DEBAQUE Romuald 3D 852",
    "CYRILE Charly 3D 857",
    "LECOQ Christophe 3D 903",
    "BOUTET Hugues 3D 978",
    "LAASAMI Naim 4A 1178",
    "LAVIELLE Pascal 4B 1485",
    "GRANDPERRIN Jonathan 4B 1494",
    "TEMPLIER Maël 4B 1555",
    "BONHOMME Sebastien 4B 1570",
    "MARTINEZ Maxime 4B 1608",
    "PIERSON Raoul 4B 1610",
    "BULLIARD-JANNOT Tao 4B 1660",
    "CAYET Arnaud 4C 1709",
    "DO CARMO Jeremy 4C 2010",
    "RENON Ludovic 4C 2080",
    "VINCENT Charles 5A 3313",
    "MARTINEZ Guillaume 5A 3556",
    "BOUTET Emmanuel 5A 3589",
    "DESLANDES Guillaume 5A 3707",
    "MATHIEUX Nicolas 5D 7226"
]

createTab(joueurs, nom_tournoi)