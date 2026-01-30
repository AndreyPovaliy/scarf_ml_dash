from dash import html, Input, Output
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc


df = pd.read_csv("data/retro_data.csv")

def register_callbacks(app):
    pass
