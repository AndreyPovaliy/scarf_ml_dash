import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc
import settings as st


df = pd.read_csv('data/df_retro.csv')

def create_layout():
    return dbc.Container([
        # Заголовок
        html.Div([
            html.H1("Рекомендательная система", className="header-title"),
            html.H2("Исследование дополнительных остеотомий", className="header-description")
        ], className="header"
        ),

        # Фильтры
        dbc.Row([
            dbc.Col([html.Label("Вид пингвина", className="filter-label"), 
                     dcc.Dropdown(id="species-filter",
                                  options=[{'label': s, 'value': s } for s in df['species'].unique()],
                                  value=df['species'].unique(),
                                  multi=True, 
                                  className="filter-dropdown",
                                  style=st.DROPDOWN_STYLE,
                                  )], md=4),

            dbc.Col([html.Label("Остров обитания", className="filter-label"), 
                     dcc.Dropdown(id="island-filter", 
                                  options=[{'label': i, 'value': i } for i in df['island'].unique()],
                                  value=df['island'].unique(),
                                  multi=True, 
                                  className="filter-dropdown", 
                                  style=st.DROPDOWN_STYLE)], md=4),

            dbc.Col([html.Label("Пол пингвина", className="filter-label"), 
                     dcc.Dropdown(id="sex-filter",
                                  options=[{'label': sx, 'value': sx } for sx in df['sex'].unique() if pd.notna(sx)],
                                  value=df['sex'].dropna().unique(),
                                  multi=True,   
                                  className="filter-dropdown", 
                                  style=st.DROPDOWN_STYLE)], md=4)
        ], className="filters-row"

        ),

        # Графики

        dbc.Row([dbc.Col([dcc.Graph(id='bill-length-scatter')], md=6), 
                 dbc.Col([dcc.Graph(id='body-mass-histogram')], md=6)
                 ]),
                 
        dbc.Row([dbc.Col([dcc.Graph(id='flipper-length-box')], md=6), 
                 dbc.Col([dcc.Graph(id='species-pie')], md=6)
                 ]),

        #информационная панель

        html.Div(id='stats-panel', className="stats-panel")


    ], fluid=True)