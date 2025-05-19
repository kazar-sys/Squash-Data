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
    "SERUSIER Jerome 2A 44",
    "BENOIT Matthieu 2A 52",
    "PINEAU Jean-Jacques 2B 66",
    "BOULDOIRE Benjamin 2B 92",
    "BONNIN Titouan 2B 84",
    "GRISON Jules 2C 148",
    "ZARKA Fabien 2C 188",
    "GOMBERT Flavian 2D 221",
    "FONTAINE Sylvain 2D 282",
    "PAILLER Kevin 3A 301",
    "LEROY Alexandre 2D 280",
    "HARRIAU Jules 3A 323",
    "MEZIANE Mehdi 3A 422",
    "LE COQ Franck 3B 467",
    "COTELLE Fabrice 3B 556",
    "ZARKA Simon 3B 560",
    "CRUZ Daniel 3C 622",
    "MAGIERA Oscar 3C 641",
    "LOUP Jean-Baptiste 3C 646",
    "JULIAN Tristan 3C 647",
    "SOULEILLAN Gregory 3C 652",
    "LUBINEAU Olivier 3C 662",
    "GUINE Yael 3C 695",
    "POTTIER Vincent 3C 699",
    "JORIS Florian 3C 767",
    "CLEMENT Paul 3D 801",
    "DEBAQUE Romuald 3D 859",
    "LECOQ Christophe 3D 910",
    "BOUTET Hugues 3D 957",
    "LAASAMI Naim 4A 1252",
    "TEMPLIER Maël 4B 1515",
    "BREUILLAUD Antoine 4B 1506",
    "GRANDPERRIN Jonathan 4B 1573",
    "MARTINEZ Maxime 4B 1598",
    "BONHOMME Sebastien 4B 1607",
    "CAYET Arnaud 4B 1684",
    "JAMOT Edouard 4C 1848",
    "BULLIARD-JANNOT Tao 4C 1862",
    "BILQUARD Jean-Chrales 4C 1875",
    "RENON Ludovic 4C 2104",
    "CLEMENT Franck 4D 2746",
    "GERBIER Julien 4D",
    "BRETON Philippe 5A 2924",
    "BOUTET Emmanuel 5A 3396",
    "MARTINEZ Guillaume 5A 3468",
    "MATHIEUX Nicolas 5D 7249"
]

createTab(joueurs, nom_tournoi)