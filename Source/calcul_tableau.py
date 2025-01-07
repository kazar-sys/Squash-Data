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
nom_tournoi = "Championnat 3eme série IDF"
joueurs = [
    "NOLANN BALLAY 3A 340",
    "GREGORY SREBNIK 3A 390",
    "BENJAMIN RIFFLE 3B 457",
    "LIONEL MOISAN 3B 450",
    "AXEL BEAU 3B 476",
    "TITOUAN COCHERIL 3B 497",
    "VINH PHAM-GIA 3B 506",
    "ADAM RAMEAU 3B 528",
    "FLORENT CARUANA 3B 532",
    "FABRICE COTELLE 3B 532",
    "ETIENNE MANNESSIER 3B 547",
    "NATHANIEL RAMEAU 3B 557",
    "SIMON QUEMIN 3B 579",
    "JULIEN MAILLIARD 3B 583",
    "RENAUD MERLAND 3B 586",
    "JONAS DUGUE 3C 620",
    "JULES PIQUERAS 3C 623",
    "ANTOINE LLEDO 3C 637",
    "PAUL HAMERY 3C 651",
    "JEAN-MARC FOURNIER 3C 655",
    "ANTONIN ROUSSET 3C 668",
    "SYLVAIN SELERIER 3C 696",
    "YOHAN SIMON 3C 776",
    "STEPHANE QUIQUEMPOIS 3D 800",
    "BRUNO JUBERT 3D 801",
    "MICKAEL HESSE 3D 843",
    "THIBAUD CARLASSARE 3D 852",
    "MARC SCHLUMBERGER 3D 878",
    "SIMON ZARKA 3D 880",
    "PAUL CLEMENT 3D 958",
    "ERIC DELTRIEUX 3D 983",
    "PIERRE MANTEZ 3D 989",
    "SILVIO-PAOLO DA COSTA 3D 998",
    "MUTTI LEO 3D 1010",
    "JEREMY PAULIN 4A 1058",
    "THOMAS MAS 4A 1061",
    "GREGORY MERCIER 4A 1058",
    "CHRISTOPHE LECOQ 4A 1087",
    "GUILLAUME VASLIN 4A 1093",
    "TUNG DINH-HOANG 4A 1158",
    "BORRELY JEAN-FRANCOIS 4A 1174",
    "ACQUAVIVA JEAN-CHRISTOPHE 4A 1187",
    "MALHEURTY ERIC 4A 1222",
    "FILIPE DA SILVA 4A 1253",
    "JEREMY ROUANNE 4A 1278",
    "JEAN-PIERRE BORDES 4B 1359",
    "BAPTISTE LARGENTON 4B 1484",
    "KEVIN GISLIER 4B 1550",
    "BRUNO NGUYEN 4B 1589",
    "LAURENT COZETTE 4B 1632",
    "NAIM LAASSAMI 4B 1664",
    "ERIC MOURLANETTE 4C 1664",
    "TADIJA VUJEVA 4C 1775",
    "GILLOT OLIVIER 4C 1804",
    "NICOLAS DUBRASQUET 4C 2004",
    "JONATHAN GRANDPERRIN 4C 2012",
    "MAXENCE COBO 4C 2049",
    "PIERRE VIALA 4D 2164",
    "ERIC VASSOR 4D 2258",
    "NICOLAS ROSSARD 4D 2406",
    "ANTOINE COEUR 5B 4510"
]

createTab(joueurs, nom_tournoi)