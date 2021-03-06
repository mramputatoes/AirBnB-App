# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Process

            Pickled a random forest model and applied to the application.


            """
        ),

    ],
)

layout = dbc.Row([column1])
