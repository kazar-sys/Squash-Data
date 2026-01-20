import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_report(player_data):
    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=("Position par rapport aux paliers", "Courbe de progression", "Répartition Victoires/Défaites"),
        vertical_spacing=0.1,
        specs=[[{"type": "xy"}], [{"type": "xy"}], [{"type": "domain"}]]
    )

    fig.add_trace(go.Scatter(x=[0], y=[player_data['avg']], mode='markers+text', 
                             text=[f"Rang: {player_data['rank']}"], textposition="top center",
                             name="Joueur"), row=1, col=1)

    fig.add_trace(go.Pie(labels=['Victoires', 'Défaites'], values=player_data['rates']), row=3, col=1)

    fig.update_layout(height=900, title_text="Tableau de Bord Squash", showlegend=True)
    fig.write_html("rapport_squash.html")
    print("Page 'rapport_squash.html' générée.")