from dash import Dash

from official_tutorials.fundamentals.p1_layout.layout import layout

app = Dash(__name__)

app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)
