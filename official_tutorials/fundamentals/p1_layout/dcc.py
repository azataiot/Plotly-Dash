from dash import Dash, html, dcc

app = Dash(__name__)

dropdown = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=['New York City', 'Montreal', 'San Francisco'],
        value='Montreal',
    ),
])

multi_select = html.Div([
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=['New York City', 'Montreal', 'San Francisco'],
        value=['Montreal', 'San Francisco'],
        multi=True,
    ),
], id='multi-select')

radio = html.Div([
    html.Label('Radio Items'),
    dcc.RadioItems(
        options=['New York City', 'Montreal', 'San Francisco'],
    ),
])

checkbox = html.Div([
    html.Label('Checkboxes'),
    dcc.Checklist(
        options=['New York City', 'Montreal', 'San Francisco'],
        value=['Montreal', 'San Francisco'],
    ),
])

text_input = html.Div([
    html.Label('Text Input'),
    dcc.Input(value='Montreal', type='text'),
])

slider = html.Div([
    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=5,
    ),
])

app.layout = html.Div([
    html.Div([
        dropdown,
        multi_select,
        radio,
    ], style={
        'padding': '10px',
        'flex': 1,
    }),
    html.Div([
        checkbox,
        text_input,
        slider,
    ], style={
        'padding': '10px',
        'flex': 1,
    }),
], style={'display': 'flex', 'flex-direction': 'row'})

if __name__ == '__main__':
    app.run_server(debug=True)
