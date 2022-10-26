import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go

tabtitle = 'EduML'

########### Initiate the app
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__) #external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading)
    ]
)


if __name__ == '__main__':
    app.run_server()
