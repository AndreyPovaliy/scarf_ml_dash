import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc


df = pd.read_csv("data/retro_data.csv")

def create_layout():
    return dbc.Container([
        html.Div([
            html.H1("Анализ выполнения дополнительных остеотомий", className= "header-title"),
            html.H2("Исследование ключеывых факторов для определения метатарзалгий при остетомии scarf", className= "header-description")
    ],className= "header"),
    dbc.Row([
        dbc.Col([html.Label("Пол",                             
                            className= 'filter-label'), 
                 dcc.Dropdown(id = 'gender-filter',
                              options = [{'label' : gender, 'value': gender} for gender in df['gender'].unique()],
                              value = df['gender'].unique(),
                              className= 'filter-dropdown')]),
        dbc.Col([html.Label("Степень деформации", 
                            className= 'filter-label'), 
                 dcc.Dropdown(id = 'defdegree-filter',
                              options = [{'label' : defdegree, 'value': defdegree} for defdegree in df['initial_deformation_grade'].unique()],
                              value = df['initial_deformation_grade'].unique(),
                              className= 'filter-dropdown')]),
        dbc.Col([html.Label("Akin", 
                            className= 'filter-label'), 
                 dcc.Dropdown(id = 'akin-filter',
                              options = [{'label' : akin, 'value': akin} for akin in df['is_akin'].unique()],
                              value = df['is_akin'].unique(),
                              className= 'filter-dropdown')]),
        dbc.Col([html.Label("Дополнительные остеотомии", 
                            className= 'filter-label'), 
                 dcc.Dropdown(id = 'additional-filter',
                              options = [{'label' : additional, 'value': additional} for additional in df['is_additional'].unique()],
                              value = df['is_additional'].unique(),
                              className= 'filter-dropdown')]),
             ],className='filters-row'),

        dbc.Row([
                    dbc.Col([dcc.Graph()]),
                    dbc.Col([dcc.Graph()])

        ]),
        dbc.Row([
                    dbc.Col([dcc.Graph()]),
                    dbc.Col([dcc.Graph()])

        ])



        ], fluid= True)

