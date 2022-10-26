import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go
import numpy as np
tabtitle = 'EduML'

########### Initiate the app
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__) #external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle
array = np.array([2, 3, 5, 7])
########### Set up the layout
app.layout = html.Div(children=[
    html.H1("Some Random Words")
    ]
)


if __name__ == '__main__':
    app.run_server()
