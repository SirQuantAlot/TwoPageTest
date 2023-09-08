from os import environ

import pickle as pkl
import dash
import dash_mantine_components as dmc
from dash import html, dash_table,html, callback, Output, Input, State, dcc
from dash_iconify import DashIconify
import callbacks
import os

dash.register_page(
    __name__,
    "/upload_portfolio",
    title="Test Page 2",
    description="Testing",
)


home_dir = os.getcwd()
returns_pickle = open(home_dir + "/assets/returns_df_AlphaVantage.pkl", "rb")
returns_df = pkl.load(returns_pickle)

layout = dmc.Container(
    [
        dmc.Title("Upload Positions", color="blue", size="h3"),
        html.Br(),
        dmc.Grid(
            [
                dmc.Col(
                    [
                        html.Button(
                            "+ Position...",
                            id="editing-rows-button",
                            style={
                                "font-size": "12px",
                                "width": "140px",
                                "border": "1px solid grey",
                                "display": "inline-block",
                                "margin-bottom": "10px",
                                "margin-right": "5px",
                                "height": "37px",
                                "verticalAlign": "top",
                            },
                            n_clicks=0,
                        ),
                        # dcc.Store(id="positions_store", storage_type="local")
                    ],
                    span=12,
                ),
                dmc.Col(
                    [
                        dash_table.DataTable(
                            id="adding-rows-table",
                            columns=[
                                {
                                    "id": "Ticker",
                                    "name": "Ticker",
                                    "presentation": "dropdown",
                                },
                                {"id": "$ Amount", "name": "$ Amount"},
                            ],
                            data=[{"Ticker": "", "$ Amount": 0}],
                            editable=True,
                            row_deletable=True,
                            style_table={
                                "height": "calc(15vh + 100px)",
                                "overflowX": "auto",
                            },
                            style_data={"border": "1px solid grey"},
                            style_header={
                                "border": "1px solid black",
                                "textAlign": "center",
                            },
                            style_cell={"textAlign": "center"},
                            style_data_conditional=[
                                {
                                    "if": {
                                        "state": "selected"
                                    },  # 'active' | 'selected'
                                    "backgroundColor": "rgba(0, 116, 217, 0.3)",
                                    "border": "1px solid blue",
                                },
                                {
                                    "if": {"state": "active"},  # 'active' | 'selected'
                                    "backgroundColor": "rgba(0, 116, 217, 0.3)",
                                    "border": "1px solid rgb(0, 116, 217)",
                                }],
                            dropdown={
                                "Ticker": {
                                    "options": [
                                        {"label": str(i), "value": str(i)}
                                        for i in list(returns_df.columns.values)
                                    ]
                                }
                            },
                        )
                    ],
                    span=4,  # default is 12 per page width
                ),
            ]
        )
    ]
)
