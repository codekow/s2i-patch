import dash
from dash import dcc,html


#external_stylesheets = ['/assets/tpp.css'] #, dbc.themes.BOOTSTRAP
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)

application = app.server

with open('README.md', 'r') as myfile:
  docs = myfile.read()


app.layout = html.Div(
    children=[
        dcc.Markdown(docs)
    ]
)

    
if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0', port=8080)
