from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

# section Filter
filter_x = html.Div([
    dcc.Dropdown(
        id='xaxis-column',
        options=[{'label': i, 'value': i} for i in df['Indicator Name'].unique()],
        value='Fertility rate, total (births per woman)',
    ),
    dcc.RadioItems(
        id='xaxis-type',
        options=['Linear', 'Log'],
        value='Linear',
        inline=True,
    ),
], style={
    'width': '48%',
    'display': 'inline-block',
})
filter_y = html.Div([
    dcc.Dropdown(
        id='yaxis-column',
        options=df['Indicator Name'].unique(),
        value='Life expectancy at birth, total (years)',
    ),
    dcc.RadioItems(
        id='yaxis-type',
        options=['Linear', 'Log'],
        value='Linear',
        inline=True,
    ),
], style={
    'width': '48%',
    'display': 'inline-block',
    'float': 'right',
})

# section Graph
graph = dcc.Graph(id='indicator-graphic')

# section slider
slider = dcc.Slider(
    id='year--slider',
    min=df['Year'].min(),
    max=df['Year'].max(),
    step=None,
    value=df['Year'].max(),
    marks={str(year): str(year) for year in df['Year'].unique()},
)

# section layout
app.layout = html.Div([
    filter_x,
    filter_y,
    graph,
    slider,
])


# section callback
@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value'),
    Input('yaxis-type', 'value'),
    Input('year--slider', 'value'),
)
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    dff = df[df['Year'] == year_value]

    fig = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
                     y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
                     hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

    fig.update_layout(
        margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
        hovermode='closest',
        xaxis={
            'title': xaxis_column_name,
            'type': 'linear' if xaxis_type == 'Linear' else 'log'
        },
        yaxis={
            'title': yaxis_column_name,
            'type': 'linear' if yaxis_type == 'Linear' else 'log'
        },
        transition_duration=500,
    )

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
