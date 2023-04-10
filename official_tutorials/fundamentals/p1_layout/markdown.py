from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](https://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](https://commonmark.org/help/)
if this is your first introduction to Markdown!
'''
app = Dash(__name__)
app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])

if __name__ == '__main__':
    app.run_server(debug=True)
