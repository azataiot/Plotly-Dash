from dash import html, dcc

from official_tutorials.fundamentals.p1_layout.data import fig
from official_tutorials.fundamentals.p1_layout.style import colors

layout = html.Div([
    html.H1('Hello Dash', style={
        'textAlign': 'center',
        'color': colors['text'],
    }),

    html.Div('Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text'],
    }),

    dcc.Graph(
        id='example-graph',
        figure=fig,
    )
])
