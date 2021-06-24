# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# Imports from this application
from app import app, server
from pages import index, predictions, process


navbar = dbc.NavbarSimple(
    brand='Optimal AirBnB Price',
    brand_href='/',
    children=[
        dbc.NavItem(
            dcc.Link(
                'Predictions', href='/predictions', className='nav-link')),
        dbc.NavItem(
            dcc.Link(
                'Process', href='/process', className='nav-link')),
    ],
    sticky='top',
    color='light',
    light=True,
    dark=False
)

# Footer
footer = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            [
                                html.Span('Jeremiah Evangelista',
                                          className='mr-2'),
                                html.A(
                                    html.I(
                                        className='fab fa-github-square mr-1'),
                                    href='https://github.com/mramputatoes'),
                            ],
                            className='lead'
                        )
                    ]
                ),
                dbc.Col(
                    [
                        html.P(
                            [
                                html.Span('Allen Dela Virgen',
                                          className='mr-2'),
                                html.A(
                                    html.I(
                                        className='fab fa-github-square mr-1'),
                                    href='https://github.com/Abdelapv53'),
                            ],
                            className='lead'
                        )
                    ]
                ),
                dbc.Col(
                    [
                        html.P(
                            [
                                html.Span('Angello Reyes', className='mr-2'),
                                html.A(
                                    html.I(
                                        className='fab fa-github-square mr-1'),
                                    href='https://github.com'),
                            ],
                            className='lead'
                        )
                    ]
                ),
            ]
        )
    ]
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dbc.Container(id='page-content', className='mt-4'),
    html.Hr(),
    footer
])


# URL Routing for Multi-Page Apps: https://dash.plot.ly/urls
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/predictions':
        return predictions.layout
    elif pathname == '/process':
        return process.layout
    else:
        return dcc.Markdown('## Page not found')


# Run app server: https://dash.plot.ly/getting-started
if __name__ == '__main__':
    app.run_server(debug=True)