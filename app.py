# Code From here: https://dash.plot.ly/deployment
# Replacement code from here: https://dash.plot.ly/getting-started


# import os

# import dash
# import dash_core_components as dcc
# import dash_html_components as html


# app = dash.Dash(__name__)
# server = app.server

# app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# app.layout = html.Div([
#     html.H2('Hello World'),
#     dcc.Dropdown(
#         id='dropdown',
#         options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
#         value='LA'
#     ),
#     html.Div(id='display-value')
# ])

# @app.callback(dash.dependencies.Output('display-value', 'children'),
#               [dash.dependencies.Input('dropdown', 'value')])
# def display_value(value):
#     return 'You have selected "{}"'.format(value)

# if __name__ == '__main__':
#     app.run_server(debug=True)



# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
server = app.server # Added by me

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)