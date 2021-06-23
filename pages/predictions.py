import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np


# Imports from this application
from app import app
from joblib import load


model = load('assets/firstmodel.joblib')

@app.callback(
    Output('prediction-values', 'children'),
    [Input('host_response_time', 'value'),
        Input('host_is_superhost', 'value'),
        Input('host_identity_verified', 'value'),
        Input('property_type', 'value'),
        Input('room_type', 'value'),
        Input('accommodates', 'value'),
        Input('bedrooms', 'value'),
        Input('beds', 'value')]
)

def predict(host_response_time, host_is_superhost,
    host_identity_verified, property_type, room_type,
    accommodates, bedrooms, beds):
    df = pd.DataFrame(
        columns = ['host_response_time', 'host_is_superhost',
                'host_identity_verified', 'property_type', 'room_type',
                'accommodates', 'bedrooms', 'beds'],
        data = [[host_response_time, host_is_superhost,
                host_identity_verified, property_type, room_type,
                accommodates, bedrooms, beds]]),
    y_pred = model.predict(df)[0]
    return f"You're rental price:, ${y_pred:.0f}"


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        #dbc.Label("Host's Response Time"),
        dcc.Markdown("### Response Time"),
        dcc.Dropdown(
            id='host_response_time',
            options=[
                {'label': 'within an hour', 'value': 'within an hour'},
                {'label': 'within a few hours', 'value': 'within a few hours'},
                {'label': 'within a day ', 'value': 'within a day'},
                {'label': 'a few days or more', 'value': 'a few days or more'}
                ],
            value='within an hour',
            className='mb-5',
        ),
        #dbc.Label('Host is superhost?'),
        dcc.Markdown("### Superhost?"),
        dcc.Dropdown(
            id='host_is_superhost',
            options = [{'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0}],
            value = 'No',
            className = 'mb-5',
        ),
        #dbc.Label('Host identity verified?'),
        dcc.Markdown("### Verified Identity?"),
        dcc.Dropdown(
                id = 'host_identity_verified',
                options=[{'label': 'Yes', 'value': 1},
                    {'label': 'No', 'value': 0}],
                value='No',
                className='mb-5',
        ),
        #dbc.Label('Property Type'),
        dcc.Markdown('#### Property Type'),
        dcc.Dropdown(
            id='property_type',
            options=[
                {"label": "Entire apartment", "value": "Entire apartment"},
                {"label": "Private room in apartment", "value": "Private room in apartment"},
                {"label": "Entire condominium","value": "Entire condominium"},
                {"label": "Private room in house ","value": "Private room in house"},
                {"label": "Entire house","value": "Entire house"},
                {"label": "Private room in condominium","value": "Private room in condominium"},                    
                {"label": "Entire guest suite","value": "Entire guest suite"},
                {"label": "Room in boutique hotel","value": "Room in boutique hotel"},
                {"label": "Entire serviced apartment","value": "Entire serviced apartment"},
                {"label": "Entire loft","value": "Entire loft"},
                {"label": "Entire townhouse","value": "Entire townhouse"},
                {"label": "Private room in townhouse","value": "Private room in townhouse"},                    
                {"label": "Private room in bungalow","value": "Private room in bungalow"},
                {"label": "Shared room in apartment","value": "Shared room in apartment"},
                {"label": "Entire guesthouse","value": "Entire guesthouse"},
                {"label": "Room in hotel","value": "Room in hotel"},
                {"label": "Private room in loft","value": "Private room in loft"},
                {"label": "Shared room in house","value": "Shared room in house"},                    
                {"label": "Private room in bed and breakfast","value": "Private room in bed and breakfast"},
                {"label": "Private room in guest suite","value": "Private room in guest suite"},
                {"label": "Entire bungalow","value": "Entire bungalow"},
                {"label": "Shared room in condominium","value": "Shared room in condominium"},
                {"label": "Room in serviced apartment","value": "Room in serviced apartment"},
                {"label": "Room in bed and breakfast","value": "Room in bed and breakfast"},
                {"label": "Private room in guesthouse","value": "Private room in guesthouse"},
                {"label": "Room in hostel","value": "Room in hostel"},
                {"label": "Private room in cottage","value": "Private room in cottage"},
                {"label": "Boat","value": "Boat"},
                {"label": "Entire cottage","value": "Entire cottage"},
                {"label": "Shared room in hostel","value": "Shared room in hostel"},
                {"label": "Tiny house","value": "Tiny house"},
                {"label": "Room in aparthotel","value": "Room in aparthotel"},
                {"label": "Private room in hostel","value": "Private room in hostel"},
                {"label": "Private room in tiny house","value": "Private room in tiny house"},
                {"label": "Private room in serviced apartment","value": "Private room in serviced apartment"},
                {"label": "Private room","value": "Private room"},
                {"label": "Private room in farm stay","value": "Private room in farm stay"},
                {"label": "Entire home/apt","value": "Entire home/apt"},
                {"label": "Campsite","value": "Campsite"},
                {"label": "Shared room in loft","value": "Shared room in loft"},
                {"label": "Shared room","value": "Shared room"},
                {"label": "Shared room in serviced apartment","value": "Shared room in serviced apartment"},
                {"label": "Entire villa","value": "Entire villa"},
                {"label": "Shared room in cave","value": "Shared room in cave"},
                {"label": "Shared room in bungalow","value": "Shared room in bungalow"},
                {"label": "Private room in villa","value": "Private room in villa"},
                {"label": "Private room in cabin","value": "Private room in cabin"},
                {"label": "Entire place ","value": "Entire place"}
                ],
            value='Campsite',
            className='mb-5',
        ),
        #dbc.Label('Room Type'),
        dcc.Markdown('#### Room Type'),
        dcc.Dropdown(
            id='room_type',
            options=[
                {"label": "Entire home/apt", "value": "Entire home/apt"},
                {"label": "Private room", "value": "Private room"},
                {"label": "Shared room","value": "Shared room"},
                {"label": "Hotel room","value": "Hotel room"}
                    ],
            value="Entire home/apt",
            className='mb-5',
        ),
        #dbc.Label('Accommodates'),
        dcc.Markdown('#### Accommodates'),
        dcc.Slider(
            id='accommodates',
            min=2,
            max=16,
            step=1,
            value=1,
            marks={n: str(n) for n in range(2,17,1)},
            className='mb-5',
        ),
        #dbc.Label('Bedrooms'),
        dcc.Markdown('#### Bedrooms'),
        dcc.Slider(
            id='bedrooms',
            min=1,
            max=50,
            step=1,
            value=1,
            marks={n: str(n) for n in range(1,51,1)},
            className='mb-5',
        ),
        #dbc.Label('Beds'),
        dcc.Markdown('#### Beds'),
        dcc.Slider(
            id='beds',
            min=1,
            max=50,
            step=1,
            value=1,
            marks={n: str(n) for n in range(1,51,1)},
            className='mb-5',
        )      
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('### RENT THIS MUCH!!!!'),
        html.H2('Test'),
        html.Div(id='prediction-values')
    ],
    md=4
)

layout = dbc.Row([column1,column2])