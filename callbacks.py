from dash import html, Input, Output, State
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
from assets import settings as st
import plotly.io as pio
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


pio.templates['custom'] = pio.templates['plotly'].update(
    layout = dict(colorway = st.MY_PALETTE)
)
pio.templates.default = "custom"

df = pd.read_csv("data/df_1_c.csv")
df_n = pd.read_csv('data/df_1_n.csv')
df_n = df_n.drop(['stiffness','recurrence','time'], axis=1)
df_n1 = df_n.drop(['metatarsalgia'], axis=1)

def register_callbacks(app):
    @app.callback(
        Output('age-scatter', 'figure'),
        Output('aofas_0-histogram', 'figure'),
        Output('sefas_0-box', 'figure'),
        Output('gender-pie', 'figure'),
        Output('stats-panel', 'children'),
        Input('submit-botton', 'n_clicks'),
        State('gender-filter', 'value'),
        State('tsp-filter', 'value'),
        State('age-input','value'),
        State('bmi-input','value'),
        State('aofas_0-input','value'),
        State('vasfa_0-input','value'),
        State('moxfq_0-input','value'),
        State('sefas_0-input','value'),
        State('fadi_0-input','value'),
        State('faam_0-input','value'),
        State('hvipa_0-input','value'),
        State('hva_0-input','value'),
        State('ima_0-input','value'),
        State('imaI-V-input','value'),
        State('imaIV_V_0-input','value'),
        State('dmaa-input','value'),
        State('base1-filter', 'value'),
        State('base2-filter', 'value'),
        State('base3-filter', 'value'),
        State('base4-filter', 'value'),
        State('met2-filter', 'value'),
        State('met3-filter', 'value'),
        State('met4-filter', 'value'),
        State('met5-filter', 'value')
               
    )
    
    def update_grafs(n_clicks,
                     selected_gender, 
                     selected_tsp,
                     selected_age,
                     selected_bmi,
                     selected_aofas_0,
                     selected_vasfa_0,
                     selected_moxfq_0,
                     selected_sefas_0,
                     selected_fadi_0,
                     selected_faam_0,
                     selected_hvipa_0,
                     selected_hva_0,
                     selected_ima_0,
                     selected_imaI_V,
                     selected_imaIV_V_0,
                     selected_dmaa_0,
                     selected_base_1,
                     selected_base_2,
                     selected_base_3,
                     selected_base_4,
                     selected_met2,
                     selected_met3,
                     selected_met4,
                     selected_met5):


        global df, df_n, df_n1

        if n_clicks and n_clicks > 0:
        # Convert selected values to strings
            selected_gender = [str(x) for x in selected_gender] if selected_gender else [str(x) for x in df['gender'].unique()]
            selected_tsp = [str(x) for x in selected_tsp] if selected_tsp else [str(x) for x in df['tsp_0'].unique()]

        # Convert dataframe columns to strings for filtering
            filtered_df = df[
                (df['gender'].astype(str).isin(selected_gender)) &
                (df['tsp_0'].astype(str).isin(selected_tsp)) &
                (df['age'].between(selected_age - 10, selected_age + 10)) &
                (df['bmi'].between(selected_bmi - 10, selected_bmi + 10)) &
                (df['aofas_0'].between(selected_aofas_0 - 10, selected_aofas_0 + 10))
            ]
        else:
            filtered_df = df
        
        total_pathients = len(filtered_df)
        avg_age = filtered_df['age'].mean()
        avg_aofas_24 = filtered_df['aofas_24'].mean()
        avg_vasfa_24 = filtered_df['vasfa_24'].mean()
        avg_moxfq_24 = filtered_df['moxfq_24'].mean()
        avg_sefas_24 = filtered_df['sefas_24'].mean()
        # gender_counts = filtered_df['gender'].value_counts()
        metatarlagia_counts = filtered_df['metatarsalgia'].value_counts()

        age_scatter_fig = go.Figure()

        for metatarsalgia in sorted(filtered_df['metatarsalgia'].unique(), reverse=True):
            metatarsalgia_df = filtered_df[filtered_df['metatarsalgia'] == metatarsalgia]
            age_scatter_fig.add_trace(go.Scatter(
                x = metatarsalgia_df['hva_0'],
                y = metatarsalgia_df['ima_0'],
                mode = 'markers',
                name = metatarsalgia,
                marker = dict(
                    size = 10,
                    opacity = 0.7,
                    line = dict(width = 1, color = "#c79dd7")
                )
            ))
        age_scatter_fig.update_layout(
            title = "Случаи метатарзалгии",
            title_font_size = st.GRAPH_HEADER_FONT_SIZE,
            title_x = st.GRAPH_HEADER_ALIGH,
            title_font_weight = st.GRAPH_TITLE_WEIGHTH,
            xaxis_title = "HVA (градусы)",
            xaxis = dict(title_font_size =st.GRAFT_FONT_SIZE,
                         tickfont = dict(size = st.GRAFT_FONT_SIZE)),
            yaxis_title = "IMA (градусы)",
            yaxis = dict(title_font_size =st.GRAFT_FONT_SIZE,
                         tickfont = dict(size = st.GRAFT_FONT_SIZE)),
            font = dict(family = 'Roboto, sans-serif'),
            legend = dict(font=dict(size = st.GRAFT_FONT_SIZE),
                          orientation = 'h',
                          yanchor = 'bottom',
                          y = 1.02,
                          xanchor = 'right',
                          x = 1),
            plot_bgcolor = st.PLOT_BACKGROUND
        )

        vasfa_0_histogram_fig = go.Figure()

        for metatarsalgia in sorted(filtered_df['metatarsalgia'].unique(),reverse= True):
            metatarsalgia_df = filtered_df[filtered_df['metatarsalgia'] == metatarsalgia]
            vasfa_0_histogram_fig.add_trace(go.Histogram(
                x = metatarsalgia_df['vasfa_24'],
                name = metatarsalgia,
                opacity = 0.7,
                marker = dict(line = dict(width = 1, color = "#c79dd7"))
            ))
        vasfa_0_histogram_fig.update_layout(
            title = "Оценка VAS FA",
            title_font_size = st.GRAPH_HEADER_FONT_SIZE,
            title_x = st.GRAPH_HEADER_ALIGH,
            title_font_weight = st.GRAPH_TITLE_WEIGHTH,
            xaxis_title = "Баллы",
            xaxis = dict(title_font_size =st.GRAFT_FONT_SIZE,
                         tickfont = dict(size = st.GRAFT_FONT_SIZE)),
            yaxis_title = "Количество",
            yaxis = dict(title_font_size =st.GRAFT_FONT_SIZE,
                         tickfont = dict(size = st.GRAFT_FONT_SIZE)),
            font = dict(family = 'Roboto, sans-serif'),
            barmode = 'overlay',
            legend = dict(font=dict(size = st.GRAFT_FONT_SIZE)),
            plot_bgcolor = st.PLOT_BACKGROUND
        )

        moxfq_24_box_fig = go.Figure()

        for metatarsalgia, color in zip(filtered_df['metatarsalgia'].unique(),st.MY_PALETTE):
            metatarsalgia_df = filtered_df[filtered_df['metatarsalgia'] == metatarsalgia]
            moxfq_24_box_fig.add_trace(go.Box(
                y = metatarsalgia_df['moxfq_24'],
                name = metatarsalgia,
                marker_color = color

            ))

        moxfq_24_box_fig.update_layout(
            title = "Оценка MOXFQ",
            title_font_size = st.GRAPH_HEADER_FONT_SIZE,
            title_x = st.GRAPH_HEADER_ALIGH,
            title_font_weight = st.GRAPH_TITLE_WEIGHTH,
            yaxis_title = "Баллы",
            yaxis = dict(title_font_size =st.GRAFT_FONT_SIZE,
                         tickfont = dict(size = st.GRAFT_FONT_SIZE)),
            font = dict(family = 'Roboto, sans-serif'),
            legend = dict(font=dict(size = st.GRAFT_FONT_SIZE)),
            plot_bgcolor = st.PLOT_BACKGROUND
        )

        gender_pie_fig = go.Figure(
            go.Pie(
                labels = metatarlagia_counts.index,
                values = metatarlagia_counts.values,
                textinfo = 'percent'
            )
        )
        gender_pie_fig.update_layout(
            title = "Метатарзалгия",
            title_font_size = st.GRAPH_HEADER_FONT_SIZE,
            title_x = st.GRAPH_HEADER_ALIGH,
            title_font_weight = st.GRAPH_TITLE_WEIGHTH,
            font = dict(family = 'Roboto'),
            legend = dict(font=dict(size = st.GRAFT_FONT_SIZE)),
            plot_bgcolor = st.PLOT_BACKGROUND
        )

        df_pred = pd.DataFrame({
            'gender': [selected_gender[0] if selected_gender and len(selected_gender) > 0 else df['gender'].iloc[0]],
            'tsp_0': [selected_tsp[0] if selected_tsp and len(selected_tsp) > 0 else df['tsp_0'].iloc[0]],
            'age': [selected_age if selected_age is not None else df['age'].mean()],
            'bmi': [selected_bmi if selected_bmi is not None else df['bmi'].mean()],
            'aofas_0': [selected_aofas_0 if selected_aofas_0 is not None else df['aofas_0'].mean()],
            'vasfa_0': [selected_vasfa_0 if selected_vasfa_0 is not None else df['vasfa_0'].mean()],
            'moxfq_0': [selected_moxfq_0 if selected_moxfq_0 is not None else df['moxfq_0'].mean()],
            'sefas_0': [selected_sefas_0 if selected_sefas_0 is not None else df['sefas_0'].mean()],
            'fadi_0': [selected_fadi_0 if selected_fadi_0 is not None else df['fadi_0'].mean()],
            'faam_0': [selected_faam_0 if selected_faam_0 is not None else df['faam_0'].mean()],
            'hvipa_0': [selected_hvipa_0 if selected_hvipa_0 is not None else df['hvipa_0'].mean()],
            'hva_0': [selected_hva_0 if selected_hva_0 is not None else df['hva_0'].mean()],
            'ima_0': [selected_ima_0 if selected_ima_0 is not None else df['ima_0'].mean()],
            'imaI_V_0': [selected_imaI_V if selected_imaI_V is not None else df['imaI_V'].mean()],
            'imaIV_V_0': [selected_imaIV_V_0 if selected_imaIV_V_0 is not None else df['imaIV_V_0'].mean()],
            'dmma_0': [selected_dmaa_0 if selected_dmaa_0 is not None else df['dmaa_0'].mean()],
            'base_1': [selected_base_1 if selected_base_1 is not None else 'нет'],
            'base_2': [selected_base_2 if selected_base_2 is not None else 'нет'],
            'base_3': [selected_base_3 if selected_base_3 is not None else 'нет'],
            'base_4': [selected_base_4 if selected_base_4 is not None else 'нет'],
            'met_2': [selected_met2 if selected_met2 is not None else 'нет'],
            'met_3': [selected_met3 if selected_met3 is not None else 'нет'],
            'met_4': [selected_met4 if selected_met4 is not None else 'нет'],
            'met_5': [selected_met5 if selected_met5 is not None else 'нет']
        })

        df_pred["gender"] = df_pred["gender"].apply(lambda x: 1 if x == df_pred["gender"].unique()[0]
                                            else 2)
        df_pred["tsp_0"] = df_pred["tsp_0"].apply(lambda x: 1 if x == "1"
                                            else 2 if x == "2"
                                            else 3 if x == "3"
                                            else 4 if x == "4"
                                            else 5 if x == "5"
                                            else 6 if x == "6"
                                            else 7)
        df_pred["base_1"] = df_pred["base_1"].apply(lambda x: 0 if x == "нет"
                                            else 1)
        df_pred["base_2"] = df_pred["base_2"].apply(lambda x: 0 if x == "нет"
                                            else 1)
        df_pred["base_3"] = df_pred["base_3"].apply(lambda x: 0 if x == "нет"
                                            else 1)
        df_pred["base_4"] = df_pred["base_4"].apply(lambda x: 0 if x == "нет"
                                            else 1)
        df_pred["met_2"] = df_pred["met_2"].apply(lambda x: 0 if x == "нет"
                                            else 1)
        df_pred["met_3"] = df_pred["met_3"].apply(lambda x: 0 if x == "нет"
                                            else 1)
        df_pred["met_4"] = df_pred["met_4"].apply(lambda x: 0 if x == "нет"
                                            else 1)
        df_pred["met_5"] = df_pred["met_5"].apply(lambda x: 0 if x == "нет"
                                            else 1)
        
        df_pred['bmi_cat'] = df_pred["bmi"].apply(lambda x: 1 if x <= 25
                                    else 2)
        df_pred["initial_deformation_grade"] = df_pred.apply(lambda row: 1 if (row["ima_0"] < 11 or row["hva_0"] < 25) 
                                                            else 2 if (row["ima_0"] < 16 or row["hva_0"] < 35) 
                                                            else 3, axis=1)
        df_pred["aofas_cat_0"] = df_pred["aofas_0"].apply(lambda x: 1 if x < 50
                                            else 2 if x < 75 and x >= 50
                                            else 3 if x < 90 and x >= 75
                                            else 4)
        
        pred_values = ['hvipa_12','hva_12', 'ima_12', 'imaI_V_12', 'imaIV_V_12', 'dmma_12', 'tsp_12',
                        'hvipa_24', 'hva_24', 'ima_24', 'imaI_V_24', 'imaIV_V_24', 'dmma_24',
                        'tsp_24', 'aofas_6', 'vasfa_6', 'moxfq_6', 'fadi_6', 'faam_6',
                        'sefas_6', 'aofas_12', 'vasfa_12', 'moxfq_12', 'fadi_12', 'faam_12',
                        'sefas_12', 'aofas_24', 'vasfa_24', 'moxfq_24', 'fadi_24', 'faam_24',
                        'sefas_24']
        

        df_n1_l = df_n1.drop(pred_values, axis=1)
        df_pred = df_pred[df_n1_l.columns]

        df_pred1 = pd.DataFrame()

        for value in pred_values:
            X = df_n1_l
            y = df_n[value]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            model = LinearRegression()
            model.fit(X_train, y_train)
            df_pred1[value] = model.predict(df_pred)

        df_pred= pd.concat([df_pred, df_pred1], axis=1)

        df_n1 = df_n.drop(['metatarsalgia'], axis=1)
        df_pred=df_pred[df_n1.columns]


                
        X= df_n.drop('metatarsalgia', axis=1)
        y = df_n['metatarsalgia']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

        rf = RandomForestClassifier(
               n_estimators=500, 
                max_depth=2, 
                max_features=2, 
                bootstrap=True, 
                min_samples_split=2,
                min_samples_leaf=1, 
                random_state=42,
                class_weight=None,
                verbose=1,
                n_jobs=-1
        )

        rf.fit(X_train, y_train)
        def predict_with_threshold(model, X, threshold=0.2):
            proba = model.predict_proba(X)[:, 1]
            return (proba >= threshold).astype(int)



        df_pred['metatarsalgia'] = predict_with_threshold(rf, df_pred, threshold=0.1)

        df_pred["way"] = df_pred["metatarsalgia"].apply(lambda x: 'Вероятна метатарзалгия' if x == 1
                                    else 'Метатарзалгия не прогнозируется')
        way_to = df_pred["way"][0]




        stats_panel = dbc.Card([
            dbc.CardHeader("Статистика выборки"),
            dbc.CardBody([
                html.H3(f"{way_to}", className="predict"),
                html.P(f"Всего пациентов: {total_pathients}"),
                html.P(f"Средний возраст: {avg_age:.0f}"),
                html.P(f"Средний AOFAS на 24 месяц: {avg_aofas_24:.0f}"),
                html.P(f"Средний VASFA на 24 месяц: {avg_vasfa_24:.0f}"),
                html.P(f"Средний MOXFQ на 24 месяц: {avg_moxfq_24:.0f}"),
                html.P(f"Средний SEFAS на 24 месяц: {avg_sefas_24:.0f}")
                
            ])

        ])

        return age_scatter_fig, vasfa_0_histogram_fig, moxfq_24_box_fig, gender_pie_fig, stats_panel