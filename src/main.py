from src.loader import load_and_clean_data
from src.analytics import process_ranking
from src.visualizer import generate_html_report

def run():
    actions, rates = load_and_clean_data()
    results = process_ranking(actions)
    
    if results:
        print(f"Moyenne: {results['avg']} | Rang: {results['rank']} | Niveau: {results['level']}")
        generate_html_report(results, rates)
    else:
        print("Erreur: Pas assez d'actions valides (min 12).")

if __name__ == "__main__":
    run()