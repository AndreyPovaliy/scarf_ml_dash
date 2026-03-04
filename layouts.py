import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc


df = pd.read_csv("data/df_1_c.csv")

def create_layout():
    return dbc.Container([
        html.Div([
            html.H1("Анализ выполнения дополнительных остеотомий", className= "header-title"),
            html.H2("Исследование ключеывых факторов для определения метатарзалгий при остетомии scarf", className= "header-description")
    ],className= "header"),

    

    dbc.Row([
        html.H2("Данные пациента", className= "header-description"),
        dbc.Col([
            
            html.Label("Пол",                             
                            className= 'filter-label'), 
                 dcc.Dropdown(id = 'gender-filter',
                              options = [{'label' : gender, 'value': gender} for gender in df['gender'].unique()],
                              multi = True,
                              value = df['gender'].unique(),
                              className= 'filter-dropdown')], md = 6),

        dbc.Col([html.Label("Позиция сесамовидных", 
                            className= 'filter-label'), 
                 dcc.Dropdown(id = 'tsp-filter',
                              options = ['7', '6', '5', '4', '3', '2', '1'],
                              multi = True,
                              value = ['7', '6', '5', '4', '3', '2', '1'],
                              className= 'filter-dropdown')], md = 6),
        dbc.Col([html.Label("Возраст", 
                            className= 'input-label'), 
                 dcc.Input(id='age-input', type='number', min=df['age'].min(), max=df['age'].max(), step=1, value=df['age'].mean().round(decimals=0))], md = 6),
        dbc.Col([html.Label("ИМТ", 
                            className= 'input-label'), 
                 dcc.Input(id='bmi-input', type='number', min=df['bmi'].min(), max=df['bmi'].max()+20, step=0.1, value=df['bmi'].mean().round(decimals=1))], md = 6),
        dbc.Col([html.Label("AOFAS", 
                            className= 'input-label'), 
                 dcc.Input(id='aofas_0-input', type='number', min=df['aofas_0'].min(), max=df['aofas_0'].max(), step=0.1, value=df['aofas_0'].mean().round(decimals=1))], md = 2),
        dbc.Col([html.Label("VASFA", 
                            className= 'input-label'), 
                 dcc.Input(id='vasfa_0-input', type='number', min=df['vasfa_0'].min(), max=df['vasfa_0'].max(), step=0.1, value=df['vasfa_0'].mean().round(decimals=1))], md = 2),
        dbc.Col([html.Label("MOXFQ", 
                            className= 'input-label'), 
                 dcc.Input(id='moxfq_0-input', type='number', min=df['moxfq_0'].min(), max=df['moxfq_0'].max(), step=0.1, value=df['moxfq_0'].mean().round(decimals=1))], md = 2),
        dbc.Col([html.Label("SEFAS", 
                            className= 'input-label'), 
                 dcc.Input(id='sefas_0-input', type='number', min=df['sefas_0'].min(), max=df['sefas_0'].max(), step=0.1, value=df['sefas_0'].mean().round(decimals=1))], md = 2),
        dbc.Col([html.Label("FAAM", 
                            className= 'input-label'), 
                 dcc.Input(id='faam_0-input', type='number', min=df['faam_0'].min(), max=df['faam_0'].max(), step=0.1, value=df['faam_0'].mean().round(decimals=1))], md = 2),
        dbc.Col([html.Label("FADI", 
                            className= 'input-label'), 
                 dcc.Input(id='fadi_0-input', type='number', min=df['fadi_0'].min(), max=df['fadi_0'].max(), step=0.1, value=df['fadi_0'].mean().round(decimals=1))], md = 2),
        dbc.Col([html.Label("HVIPA", 
                            className= 'input-label'), 
                 dcc.Input(id='hvipa_0-input', type='number', min=df['hvipa_0'].min(), max=df['hvipa_0'].max(), step=0.1, value=df['hvipa_0'].mean().round(decimals=1))], md = 2),
        dbc.Col([html.Label("HVA", 
                            className= 'input-label'), 
                 dcc.Input(id='hva_0-input', type='number', min=df['hva_0'].min(), max=df['hva_0'].max(), step=0.1, value=df['hva_0'].mean().round(decimals=1))], md = 2),
        dbc.Col([html.Label("IMA I-II", 
                            className= 'input-label'), 
                 dcc.Input(id='ima_0-input', type='number', min=df['ima_0'].min(), max=df['ima_0'].max(), step=0.1, value=df['ima_0'].mean().round(decimals=1))], md = 2),
        dbc.Col([html.Label("IMA I-V", 
                            className= 'input-label'), 
                 dcc.Input(id='imaI-V-input', type='number', min=df['imaI_V_0'].min(), max=df['imaI_V_0'].max(), step=0.1, value=df['imaI_V_0'].mean().round(decimals=1))], md = 2),
        dbc.Col([html.Label("IMA IV-V", 
                            className= 'input-label'), 
                 dcc.Input(id='imaIV_V_0-input', type='number', min=df['imaIV_V_0'].min(), max=df['imaIV_V_0'].max(), step=0.1, value=df['imaIV_V_0'].mean().round(decimals=1))], md = 2),
        dbc.Col([html.Label("DMAA", 
                            className= 'input-label'), 
                 dcc.Input(id='dmaa-input', type='number', min=df['dmma_0'].min(), max=df['dmma_0'].max(), step=0.1, value=df['dmma_0'].mean().round(decimals=1))], md = 2),

        dbc.Row([
        html.H2("Решение хирурга", className= "header-description"),
                                  dbc.Col([html.Label("Остетомия I основной фаланги", 
                            className= 'filter-label'), 
                 dcc.Dropdown(id = 'base1-filter',
                              options = [{'label' : base1, 'value': base1} for base1 in df['base_1'].unique()],
                              value = sorted(df['base_1'].unique())[1],
                              className= 'filter-dropdown')], md = 3),
        dbc.Col([html.Label("Остетомия II основной фаланги", 
                            className= 'filter-label'), 
                 dcc.Dropdown(id = 'base2-filter',
                              options = [{'label' : base2, 'value': base2} for base2 in df['base_2'].unique()],
                              value = sorted(df['base_2'].unique())[1],
                              className= 'filter-dropdown')], md = 3),
        dbc.Col([html.Label("Остетомия III основной фаланги", 
                            className= 'filter-label'), 
                 dcc.Dropdown(id = 'base3-filter',
                              options = [{'label' : base3, 'value': base3} for base3 in df['base_3'].unique()],
                              value = sorted(df['base_3'].unique())[1],
                              className= 'filter-dropdown')], md = 3),
        dbc.Col([html.Label("Остетомия IV основной фаланги", 
                            className= 'filter-label'), 
                 dcc.Dropdown(id = 'base4-filter',
                              options = [{'label' : base4, 'value': base4} for base4 in df['base_4'].unique()],
                              value = sorted(df['base_4'].unique())[1],
                              className= 'filter-dropdown')], md = 3),
        dbc.Col([html.Label("Остетомия II плюсневой кости", 
                            className= 'filter-label'), 
                 dcc.Dropdown(id = 'met2-filter',
                              options = [{'label' : met2, 'value': met2} for met2 in df['met_2'].unique()],
                              value = sorted(df['met_2'].unique())[1],
                              className= 'filter-dropdown')], md = 3),
        dbc.Col([html.Label("Остетомия III плюсневой кости", 
                            className= 'filter-label'), 
                 dcc.Dropdown(id = 'met3-filter',
                              options = [{'label' : met3, 'value': met3} for met3 in df['met_3'].unique()],
                              value = sorted(df['met_3'].unique())[1],
                              className= 'filter-dropdown')], md = 3),
        dbc.Col([html.Label("Остетомия IV плюсневой кости", 
                            className= 'filter-label'), 
                 dcc.Dropdown(id = 'met4-filter',
                              options = [{'label' : met4, 'value': met4} for met4 in df['met_4'].unique()],
                              value = sorted(df['met_4'].unique())[1],
                              className= 'filter-dropdown')], md = 3),
        dbc.Col([html.Label("Остетомия V плюсневой кости", 
                            className= 'filter-label'), 
                 dcc.Dropdown(id = 'met5-filter',
                              options = [{'label' : met5, 'value': met5} for met5 in df['met_5'].unique()],
                              value = sorted(df['met_5'].unique())[1],
                              className= 'filter-dropdown')], md = 3),
                              ])
        ],className='filters-row'),
    
    html.Div(id = 'botton-panel', className= 'botton-panel'),
    dbc.Row([dbc.Col([ 
                 html.Button('Расчитать', id='submit-botton', n_clicks=0,
            className="custom-submit-button")], md = 12)]),



    html.Div(id = 'stats-panel', className= 'stats-panel'),

        dbc.Row([
                    dbc.Col([dcc.Graph(id = 'ima-scatter')], md = 4),
                    dbc.Col([dcc.Graph(id = 'metatars-pie')], md = 4),
                    dbc.Col([dcc.Graph(id = 'dmma-scatter')], md = 4)
                    

        ])

        



        ], fluid= True)

