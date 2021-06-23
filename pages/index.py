import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app


column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Whats your predicted price?

            Do you spend hours trying to price you AirBnB rooms?

            Optimal AirBnB Price Calculator will figure out what you should 
            price your rental at to get the best returns!

            """
        ),
        dcc.Link(dbc.Button('Calculator', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/airbnb_1.jpeg', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])