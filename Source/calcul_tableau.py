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
nom_tournoi = "Championnet IDF 2eme série 2025 Squash 95"
joueurs = [
    "SERUSIER Jérôme 2A 43",
    "BAUDRY Théo 2B 62",
    "LECORDIER Ethan 2B 79",
    "VIMAL DE MURS Lilian 2B 105",
    "SCIANIMANICO Thierry 2C 113",
    "LAUTIER Mathis 2C 115",
    "MAUROY Guillaume 2C 134",
    "RAMEAU Samuel 2C 156",
    "MOSLEHI Kousha 2C 179",
    "LAURENT Rémi 2C 194",
    "SANIEZ Henri 2D 207",
    "BARBET Jules 2D 238",
    "CAVE Thomas 2D 273",
    "WEISZ Frederic 3A 308",
    "BALLAY Nolann 3A 336",
    "SOUDAZ Thomas 3A 354",
    "RETIERE Maxence 3A 400",
    "SAIZ Franck 3A 421",
    "BERTHE Yann-Hoel 3B 431",
    "RIFFLE Benjamin 3B 433",
    "COCHERIL Titouan 3B 451",
    "RAMEAU Adam 3B 462",
    "DE ZEEUM Jean-Luc 3B 463",
    "GABORIT Romain 3B 475",
    "PHAM-GIA Vinh 3B 475",
    "INDERBITZIN Matthieu 3B 521",
    "LY Benjamin 3B 528",
    "PIQUERAS Jules 3B 530",
    "CARUANA Florent 3B 533",
    "MAILLIARD Julien 3B 546",
    "LLEDO Antoine 3B 545",
    "MERLAND Renaud 3B 585",
    "PETIT Benjamin 3C 602",
    "GAESLER Nicolas 3C 623",
    "HAMERY Paul 3C 664",
    "ROUSSET Antonin 3C 679",
    "ZARKA Simon 3C 736",
    "QUINQUEMPOIS Stéphane 3C 743",
    "ZUBIALDE Jérôme 3C 748",
    "MANTEZ Pierre 3D 799",
    "SCHLUMBERGER Marc 3D 872",
    "WAISBLAT Arthur 3D 879",
    "PAULIN Jeremy 3D 930",
    "MERCIER Grégory 4A 1043",
    "DEMOT Eric 4A 1062",
    "BORDES Jean-Pierre 4A 1073",
    "DA SILVA Filipe 4A 1277",
    "ALIET David 4B 1535",
    "PIQUERAS José 4C 2037"
]

createTab(joueurs, nom_tournoi)