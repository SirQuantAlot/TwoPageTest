# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:10:41 2023

@author: asgre
"""

import pandas as pd
import plotly.graph_objects as go
from dash import callback, Input, Output, State
from dash.exceptions import PreventUpdate
import json

# Saving Data_Table
@callback(
    Output("adding-rows-table", "data"),
    Input("editing-rows-button", "n_clicks"),
    State("adding-rows-table", "data"),
    State("adding-rows-table", "columns"),
)
def add_row(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.insert(0, {c["name"]: 0 for c in columns})
    return rows

# Saving Data_Table
@callback(Output('positions_store', 'data'),
    [Input('editing-rows-button', 'n_clicks'), Input('adding-rows-table', 'data')])
def save_test_data(n, data):
    print('Saving data...')
    print(data)
    print(type(data))
    # print(json.dumps(data))
    # print(type(json.dumps(data)))
    return data

# Exposure Graph:
@callback(
    Output("adding-rows-graph", "figure"),
    Input("positions_store", "data"),
)
def display_output(data):
    print('Starting graph...')
    print('data: ', data)
    print('data datatype: ',type(data))
    if data is None:
        raise PreventUpdate
    else:
        print('Getting to print...')
        y = pd.to_numeric([row["$ Amount"] for row in data])
        x = [row["Ticker"] for row in data]
        fig = go.Figure(go.Bar(y=y, x=x, marker_color="rgb(0, 0, 153)"))
        fig.update_layout(
            yaxis_range=[0, max(y)]
        )
        fig.layout.plot_bgcolor = "#fff"
        fig.layout.paper_bgcolor = "#fff"
    return fig
