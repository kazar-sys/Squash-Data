import requests
from bs4 import BeautifulSoup

URL = "https://www.squashnet.fr/index.php"

# Paramètres fixes issus de ta requête observée
payload_base = {
    'ic_a': '56ed9559ce254f5d94fdcf45090b370f',
    'ic_ajax': '1',
    'month': '35',        # mois classement
    'name': '',           # vide = tous
    'ligue': '-1',
    'catage': '20',       # catégorie Sénior Masculin (à adapter)
    'clt': '-1',          # offset/pagination
    'genre': '6',         # masculin
    'assimilate': '161',
    'integrate': '161',
    'ic_t': 'search_results',
    'ic_mform': '1',
    'id': 'catage',
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.squashnet.fr/classements",
}

session = requests.Session()

def get_page(clt_value):
    payload = payload_base.copy()
    payload['clt'] = str(clt_value)
    response = session.post(URL, data=payload, headers=headers)
    response.raise_for_status()
    return response.text

def parse_players(html):
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.select('div.list div.row')
    players = []
    for row in rows:
        if 'header' in row.get('class', []):
            continue
        # Extraction des champs
        rankm = row.select_one('div.rankm')
        name = row.select_one('div.name')
        clt = row.select_one('div.clt')
        rank = row.select_one('div.rank')
        moyenne = row.select_one('div.moyenne')
        licence = row.select_one('div.licence')
        ligue = row.select_one('div.ligue')
        club = row.select_one('div.club')
        catage = row.select_one('div.catage')

        if name:
            players.append({
                'rankm': rankm.text.strip() if rankm else '',
                'name': name.text.strip(),
                'clt': clt.text.strip() if clt else '',
                'rank': rank.text.strip() if rank else '',
                'moyenne': moyenne.text.strip() if moyenne else '',
                'licence': licence.text.strip() if licence else '',
                'ligue': ligue.text.strip() if ligue else '',
                'club': club.text.strip() if club else '',
                'catage': catage.text.strip() if catage else '',
            })
    return players

def main():
    clt = 1
    all_players = []
    while True:
        print(f"Récupération page avec clt={clt} ...")
        html = get_page(clt)
        players = parse_players(html)
        if not players:
            print("Plus de joueurs trouvés, fin de la récupération.")
            break
        all_players.extend(players)
        clt += len(players)  # avancer l’offset
    print(f"Nombre total de joueurs récupérés : {len(all_players)}")
    # Affichage des 10 premiers
    for p in all_players:
        print(p)

if __name__ == "__main__":
    main()
