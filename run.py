from flask import Flask
import dash
from dash import Dash, html, dcc

# Setting up the Flask server
server = Flask(__name__)

scripts = [
    'https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/ru.min.js',
    'https://www.googletagmanager.com/gtag/js?id=G-4PJELX1C4W',
    'https://media.ethicalads.io/media/client/ethicalads.min.js',
]

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    use_pages=True,
    external_scripts=scripts,
    update_title=None,
    server=server,
)

app.layout = html.Div(
    [
        dcc.Store(id='positions_store', storage_type='local', data={}),
        dash.page_container,
    ]
)

if __name__ == '__main__':
    app.run(debug=True, dev_tools_ui=True, dev_tools_props_check=True)
