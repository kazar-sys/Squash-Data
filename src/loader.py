import pandas as pd
from datetime import datetime, timedelta

def clean_points(value):
    try:
        return int(str(value).replace(",", "").replace(" ", "").split('.')[0])
    except (ValueError, TypeError, AttributeError):
        return 0

def load_and_clean_data():
    excel_file = "data/Actions Simon.xlsx"
    
    df = pd.read_excel(excel_file)

    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
    
    df = df.dropna(subset=['Date'])
    
    df['Points'] = df['Points'].apply(clean_points)
    
    try:
        win_rate = df['Total Gagnés'].dropna().iloc[0] if 'Total Gagnés' in df.columns else 0
        lose_rate = df['Total Perdus'].dropna().iloc[0] if 'Total Perdus' in df.columns else 0
    except (IndexError, KeyError):
        win_rate, lose_rate = 0, 0
    
    actions = []
    expiry_limit = datetime.now() - timedelta(days=365)
    
    for _, row in df.iterrows():
        actions.append({
            'Points': row['Points'],
            'Date': row['Date'],
            'Expired': row['Date'] < expiry_limit,
            'Type': str(row.get('Type de tournoi', 'Inconnu')),
            'Localisation': str(row.get('Type de points', 'Inconnu'))
        })
        
    return actions, [float(win_rate), float(lose_rate)]