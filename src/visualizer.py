import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import webbrowser
import os
from datetime import datetime
from src.config import LEVELS

def generate_html_report(res, rates):
    color_win = "#2ecc71"
    color_loss = "#e74c3c"
    primary_blue = "#0984e3" 
    line_dark = "#2d3436"
    grid_light = "#f1f2f6"
    zebra_color = "#f1f2f6" 
    main_font = "Montserrat, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    
    months_fr = {
        1: "Janvier", 2: "Février", 3: "Mars", 4: "Avril", 
        5: "Mai", 6: "Juin", 7: "Juillet", 8: "Août", 
        9: "Septembre", 10: "Octobre", 11: "Novembre", 12: "Décembre"
    }
    
    now = datetime.now()
    display_month = months_fr[now.month]
    display_year = now.year
    
    total_height = 1750 
    
    fig = make_subplots(
        rows=3, cols=2,
        vertical_spacing=0.08, 
        column_widths=[0.75, 0.25], 
        specs=[
            [{"type": "xy"}, {"type": "domain"}],
            [{"type": "xy", "colspan": 2}, None],
            [{"type": "table", "colspan": 2}, None]
        ],
        subplot_titles=(
            "Paliers de Classement", "Ratio Victoires / Défaites",
            "Rang en fonction des points",
            "Détail des Meilleures Actions"
        ),
        row_heights=[0.25, 0.22, 0.53] 
    )

    idx = res['index_level']
    indices_to_plot = range(max(0, idx - 3), min(len(LEVELS), idx + 2))
    
    fig.add_shape(
        type="rect", xref="x1", yref="y1",
        x0=0, x1=1, 
        y0=LEVELS[max(0, idx - 3)][1] - 50, 
        y1=LEVELS[min(len(LEVELS)-1, idx + 1)][1] + 50,
        fillcolor="#fdfcf0", layer="below", line_width=0,
        row=1, col=1
    )

    for i in indices_to_plot:
        y_val = LEVELS[i][1]
        lvl_name = LEVELS[i][2]
        fig.add_shape(type="line", x0=0, x1=1, y0=y_val, y1=y_val,
                      line=dict(color="#b2bec3", width=1.5, dash="dash"),
                      xref="x1", yref="y1", row=1, col=1)
        fig.add_annotation(
            x=1.02, y=y_val, text=f"<b>{lvl_name}</b>", 
            showarrow=False, xanchor="left", yanchor="middle",
            xref="x1", yref="y1", font=dict(size=12, color=line_dark),
            row=1, col=1
        )

    fig.add_trace(go.Scatter(
        x=[0.5], y=[res['avg']],
        mode="markers+text",
        text=[f"<b>Moi ({res['rank']}e)</b>"],
        textposition="top center",
        marker=dict(size=15, color=primary_blue, line=dict(width=3, color="white")),
        showlegend=False
    ), row=1, col=1)

    fig.update_xaxes(showticklabels=False, showgrid=False, range=[0, 1.15], row=1, col=1)
    fig.update_yaxes(tickmode='linear', tick0=0, dtick=100, gridcolor=grid_light, 
                     range=[LEVELS[max(0, idx - 3)][1] - 80, LEVELS[min(len(LEVELS)-1, idx + 1)][1] + 80], row=1, col=1)

    fig.add_trace(go.Pie(
        labels=["Victoires", "Défaites"], values=rates, hole=.6,
        domain={'x': [0.75, 1.0], 'y': [0.75, 0.98]},
        marker=dict(colors=[color_win, color_loss], line=dict(color='white', width=3)),
        textinfo='none', hoverinfo='label+percent', showlegend=False 
    ), row=1, col=2)

    fine_x = np.linspace(min(res['tab_x']), max(res['tab_x']), 1000)
    fig.add_trace(go.Scatter(
        x=fine_x, y=res['f_interp'](fine_x), mode='lines',
        line=dict(color=color_win, width=4, shape='spline'), showlegend=False
    ), row=2, col=1)

    fig.add_trace(go.Scatter(
        x=[res['avg']], y=[res['rank']], mode="markers",
        marker=dict(size=12, color=primary_blue, line=dict(width=2, color="white")), showlegend=False
    ), row=2, col=1)
    
    fig.update_xaxes(title="Points", gridcolor=grid_light, row=2, col=1)
    fig.update_yaxes(title="Rang", gridcolor=grid_light, row=2, col=1)

    headers = ["Points", "Date", "Type", "Localisation"]
    sorted_best = sorted(res['best'], key=lambda x: x['Points'], reverse=False)
    
    num_rows = len(sorted_best)
    row_colors = [zebra_color if i % 2 == 0 else "white" for i in range(num_rows)]

    table_data = [
        [f"<b>{a['Points']}</b>" for a in sorted_best],
        [a['Date'].strftime('%d/%m/%Y') for a in sorted_best],
        [a['Type'] for a in sorted_best],
        [a['Localisation'] for a in sorted_best]
    ]

    fig.add_trace(go.Table(
        header=dict(
            values=[f"<b>{h}</b>" for h in headers],
            fill_color=primary_blue,
            align='center', 
            font=dict(color='white', size=15, family=main_font),
            height=45,
            line_width=0
        ),
        cells=dict(
            values=table_data, 
            fill_color=[row_colors * len(headers)], 
            align='center', 
            font=dict(size=13, color=line_dark, family=main_font),
            height=35, 
            line_width=0
        )
    ), row=3, col=1)

    header_subtitle = (f"<br><span style='font-size: 16px; color: #636e72;'>"
                      f"{display_month} {display_year}  |  "
                      f"Niveau : <b>{res['level']}</b> ({res['percent']}%)  |  "
                      f"Rang : <b>{res['rank']}e</b>"
                      f"</span><br><br>")

    fig.update_layout(
        font=dict(family=main_font, color=line_dark),
        height=total_height,
        paper_bgcolor="white",
        plot_bgcolor="white",
        title=dict(
            text=f"<span style='font-size: 34px;'><b>Dashboard de Simon</b></span>{header_subtitle}",
            x=0.5, xanchor='center', y=0.98
        ),
        margin=dict(t=150, b=50, l=120, r=120),
        showlegend=False 
    )
    
    for i in fig['layout']['annotations']:
        i['font'] = dict(size=20, color=line_dark, family=main_font)
        i['yshift'] = 35

    output_filename = "dashboard.html"
    fig.write_html(output_filename, include_plotlyjs='cdn')
    webbrowser.open(f"file://{os.path.abspath(output_filename)}")
    print(f"✅ Dashboard généré avec succès !")