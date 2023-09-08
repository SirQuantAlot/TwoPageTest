from os import environ

import dash
import dash_mantine_components as dmc
from dash import html, dash_table,html, dcc, callback, Output, Input
import callbacks
from datetime import datetime

dash.register_page(
    __name__,
    "/exposures",
    title="Test Page 2",
    description="Testing",
)

def layout():
    return dmc.Container(
    [
        # dmc.Title("Exposures", color="blue", size="h3"),
        dmc.Title(str(datetime.now().strftime("%H:%M:%S")), color="blue", size="h3"),
        html.Br(),
        dmc.Grid(
            [
                dmc.Title("$ Invested", color="blue", size="h4"),
                dmc.Col([dcc.Graph(id="adding-rows-graph")]),
            ]
        )
    ]
)

