import dash
from dash import html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
from dash.dependencies import ClientsideFunction

FONT_AWESOME = ("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY, FONT_AWESOME])

app.title = "Clinical Analytics Dashboard"


app.config["suppress_callback_exceptions"] = True
server = app.server
app.scripts.config.serve_locally = True