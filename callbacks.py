from dash import html, Input, Output
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
import settings as st
import plotly.io as pio

# установка кастомной палетки цветов для всех графиков plotly
pio.templates['custom'] = pio.templates['plotly'].update(
    layout=dict(colorway=st.MY_PALETTE)
)
pio.templates.default = "custom"

# загрузка данных
df = pd.read_csv('data/penguins.csv')

def register_callbacks(app):
    @app.callback(
        Output('bill-length-scatter', 'figure'),
        Output('body-mass-histogram', 'figure'),
        Output('flipper-length-box', 'figure'),
        Output('species-pie', 'figure'),
        Output('stats-panel', 'children'),
        Input('species-filter', 'value'),
        Input('island-filter', 'value'),
        Input('sex-filter', 'value')
    )
    def update_graphs(selected_species, selected_islands, selected_sexes):
        
        # фильтрация данных
        filtered_df = df[
            (df['species'].isin(selected_species)) &
            (df['island'].isin(selected_islands)) &
            (df['sex'].isin(selected_sexes))
        ]

        # считаем статистику

        total_penguins = len(filtered_df)
        avg_mass = filtered_df['body_mass_g'].mean()
        avg_flipper = filtered_df['flipper_length_mm'].mean()
        species_counts =filtered_df['species'].value_counts()

        #блок графиков

        # Scatter

        scatter_fig = go.Figure()

        for species in filtered_df['species'].unique():
            species_df = filtered_df[filtered_df['species'] == species]
            scatter_fig.add_trace(go.Scatter(
                x=species_df['bill_length_mm'],
                y=species_df['bill_depth_mm'],
                mode='markers',
                name=species,
                marker=dict(
                    size=10,
                    opacity=0.7,
                    line=dict(width=1, color='DarkSlateGrey')
                )

            ))
        
        scatter_fig.update_layout(
            title="Длина и глубина клюва по видам",
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            xaxis_title="Длина клюва (мм)",
            yaxis_title="Глубина клюва (мм)",
            font=dict(family="Roboto, sans-serif"),
            xaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            # legend=dict(font=dict(size=st.GRAPH_FONT_SIZE),
            #             orientation='h',
            #             yanchor='bottom',
            #             y=1.02,
            #             xanchor='right',
            #             x=1),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,

        )

        # Histogram

        hist_fig = go.Figure()

        for species in filtered_df['species'].unique():
            species_df = filtered_df[filtered_df['species'] == species]
            hist_fig.add_trace(go.Histogram(
                x=species_df['body_mass_g'],
                name=species,
                opacity=0.7,
                marker=dict(line=dict(width=1, color='DarkSlateGrey'))
            ))

        hist_fig.update_layout(
            title="Распределение массы тела",
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            xaxis_title="Масса тела (г)",
            yaxis_title="Количество",
            xaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
            font=dict(family="Roboto, sans-serif"),
            barmode='overlay',
        )

        # Boxplots

        box_fig = go.Figure()

        for species, color in zip(filtered_df['species'].unique(), st.MY_PALETTE):
            species_df = filtered_df[filtered_df['species'] == species]
            box_fig.add_trace(go.Box(
                y=species_df['flipper_length_mm'],
                name=species,
                marker_color=color,
                boxmean=True
            ))

        box_fig.update_layout(
            title="Длина плавника по видам",
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            yaxis_title='Длина плавника (мм)',
            font=dict(family="Roboto, sans-serif"),
            xaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=st.GRAPH_FONT_SIZE, tickfont=dict(size=st.GRAPH_FONT_SIZE)),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,

        )

        # Pie

        pie_fig = go.Figure(
            go.Pie(
                labels=species_counts.index,
                values=species_counts.values,
                textinfo='percent'
            )
        )
        pie_fig.update_layout(
            title='Распределение по видам',
            title_font_size=st.GRAPH_TITLE_FONT_SIZE,
            title_x=st.GRAPH_TITLE_ALIGN,
            title_font_weight=st.GRAPH_TITLE_WEIGHT,
            font=dict(family="Roboto, sans-serif"),
            legend=dict(font=dict(size=st.GRAPH_FONT_SIZE)),
            plot_bgcolor=st.PLOT_BACKGROUND,
            paper_bgcolor=st.PAPER_BACKGROUND,
        )

        # Stats panel

        stats_panel = dbc.Card([
            dbc.CardHeader("Статистика выборки", className="stats-header"),
            dbc.CardBody([
                html.P(f"Всего пингвинов: {total_penguins}"),
                html.P(f"Средняя масса тела: {avg_mass:.0f} г."),
                html.P(f"Средняя длина плавника: {avg_flipper:.0f} мм")
            ])

        ])

        return scatter_fig, hist_fig, box_fig, pie_fig, stats_panel