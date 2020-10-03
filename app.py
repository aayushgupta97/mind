import flask
import dash
from layout import *
from scraper import *
from dash.dependencies import Output, Input, State
from rake import KeywordExtraction
server = flask.Flask(__name__)

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/memory/',
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)


@server.route('/')
def index():
    return "Home"


app.layout = html.Div(
    [navbar,
     dbc.Container([
         dbc.Row([
             dbc.Col(input_box),
             dbc.Col()
         ]),

         dbc.Row([
             dbc.Col(),
         ]),
         html.Br(),
         html.Hr(),
         html.Br(),
         dbc.Row(dbc.Col(dbc.Button(id="submit-button", children="Update", color="primary", block=True), width=4)),
         html.Br(),
         dbc.Row([
             # dbc.Col(width={"size": 12, "offset": 0}),
             dbc.Col(width=3),
             dbc.Col(mkdown, width=6),
             dbc.Col(width=3)
         ]),

     ])
     ])


@app.callback(Output("image_container", "children"),
              [Input("submit-button", "n_clicks")],
              [State("text_field", "value")]
              )
def image_cb(clicks, value):
    try:
        if clicks and value:
            links = list()
            rake = KeywordExtraction(value)
            keywords = rake.return_keywords_with_score_more_than_threshold()
            print(clicks, value)
            for word in keywords:
                link = get_webdriver(word)
                links.append(link)
            # return "TEXT"
            print("Keywords: ", keywords)
            print("Links: ", links)
            images = ''.join([f"!['some text']({link})" for link in links])
            return images
        # return f"!['some text']({links[0]})"
    except TypeError:
        pass


# @app.callback(Output("data_table_div", "children"),
# [Input("submit-button", "n_clicks"),
#  Input("text_field", "children")])
# def update_table(n_clicks):
#     return None


if __name__ == '__main__':
    app.run_server(debug=True)
