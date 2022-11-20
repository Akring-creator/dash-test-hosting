from dash import Dash, Input, Output, dcc, html, State
from qgen import quGen
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import datetime

tabtitle = 'EduML'

########### Initiate the app
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
            meta_tags=[{'name' : 'viewport', 'content' : 'width=device-width, initial-scale=1.0'}]
            )
server = app.server
app.title=tabtitle
app.layout = html.Div(style = {'background-image':'url(https://i.ibb.co/N3qcv28/Frame-8.png)', 
                            'background-repeat': 'no-repeat'},
children=[dbc.Container([
    dbc.Row([
        dbc.Col([dbc.Card([
                dbc.CardImg(
                    src='https://i.ibb.co/883NDJK/Group-1.png', 
                    bottom=True
                ),
            ], style={'width': '5rem'},
            className='card mb-4 mt-4 border-0')]),
        dbc.Col([dbc.Card([
                dbc.CardImg(
                    src='https://i.ibb.co/x1Sj9LB/Frame-2.png', 
                    bottom=True
                ),
            ], style={'width': '5rem'},
            className='card mb-4 mt-4 border-0')], width={'size' : 1, 'offset' : 4})
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('Learning With', className='font-weight-bold'),
            html.H1('AI Power',className='font-weight-bold'),
            html.H5('Edu ML is a short answer question maker application that use a Machine Learning approach to generate questions quickly and precisely'),
            html.Button('Make Question', className='btn-primary')
        ], width={'size': 4}),
        dbc.Col([
            dbc.Card([
                dbc.CardImg(
                    src='https://i.ibb.co/grSmPTm/gambar.png',
                    bottom=True
                )
            ], className='card border-0')
        ], width={'size': 5, 'offset':2})
    ], className='mb-4'),
    dbc.Row([
        dbc.Col([
            dcc.Textarea(id = 'texts', 
                style={'width': 500, 
                'height': 300, 
                'background-color': '#f8f8f8', 
                'border': '2px solid #ccc',
                'border-radius': '4px',
                'resize' : 'none'},
                placeholder='Masukkan Artikel....'),
            dcc.Input(
                id = 'questionAmount', 
                type= 'number', 
                style={'background-color': '#f8f8f8', 
                'border': '2px solid #ccc',
                'border-radius': '4px'},
                placeholder="Berapa Soal?")
        ], style = {'background-image':'url(https://i.ibb.co/ZN8Z2ZV/Ellipse-5.png)', 'background-size': '300px', 'background-repeat': 'no-repeat'}),
        dbc.Col([
            html.H1("Just watch."),
            html.H1("Let AI do the rest."),
            html.P("Here we use the Spacy python library to analyze and process words so that we can make questions from the given articles"),
            html.Button('Submit', className='btn-primary', id = 'submitButton'),
            html.P(''),
            html.Button('Download Excel', className='btn-primary', id = 'downloadFile'),
            html.Div(id = 'outputQugen'),
            dcc.Download(id = 'downloadExcelFile')
        ], style = {'background-image':'url(https://i.ibb.co/BgyXtvf/Frame-8.png)', 'background-repeat': 'no-repeat'})
    ])
])])
@app.callback(
    Output(component_id='outputQugen', component_property='children'),
    # Input(component_id= 'dropdownList', component_property='value'),
    Input(component_id = 'submitButton', component_property = 'n_clicks'),
    [State(component_id='texts', component_property='value'),
    State(component_id = 'questionAmount', component_property = 'value')],
    prevent_initial_call=False
)
def output_function(n,  text, questionAmount):
    global df
    print('In Process')
    data = quGen(text, questionAmount)
    print('Extracting to Excel')
    df = pd.DataFrame.from_dict(data)
    df = df.drop(['prob', 'distractors'], axis=1)
    print('success')

@app.callback(
    Output('downloadExcelFile', 'data'),
    Input('downloadFile', 'n_clicks'),
    prevent_initial_call = True
)
def download_excel_function(n):
    return dcc.send_data_frame(df.to_excel, "Question-Answer-pairs.xlsx", sheet_name="question_list")


if __name__ == '__main__':
    app.run_server()
