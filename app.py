from dash import dcc,  Input, Output, dcc, html, State
import dash
import plotly.graph_objs as go
import numpy as np
tabtitle = 'EduML'

########### Initiate the app
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__) #external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle
p = 'panjang : '
l = 'Lebar : '
t = 'Tinggi : '
array1 = np.array([2, 3, 5, 7])
########### Set up the layout
app.layout = html.Div(children=[
    html.H1("Block Similiarity"),
    html.Br(),
    html.H2(p),
    dcc.Input( id = 'p1', type = 'number'),
    html.H2(l),
    dcc.Input( id = 'l1', type = 'number'),
    html.H2(t),
    dcc.Input( id = 't1', type = 'number'),
    html.Button(id = 'SubmitButton')
    ]
)


if __name__ == '__main__':
    app.run_server()
