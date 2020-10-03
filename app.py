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
         html.Br(),
         html.Br(),
         dbc.Row([
             dbc.Col(input_box, width=5),
             dbc.Col(width=4),
             dbc.Col(generate_button, width=3),
         ]),

         dbc.Row([
             dbc.Col(),
         ]),
         html.Br(),
         html.Hr(),
         html.Br(),
         dbc.Row([
             dbc.Col(width=3),
             dbc.Col(mkdown, width=6),
             dbc.Col(width=3)
         ]),
         html.Div(id="mydiv")

     ])
     ])


# @app.callback(Output("image_container", "children"),
#               [Input("submit-button", "n_clicks")],
#               [State("text_field", "value")]
#               )
# def image_cb(clicks, value):
#     try:
#         if clicks and value:
#             links = list()
#             rake = KeywordExtraction(value)
#             keywords = rake.return_keywords_with_score_more_than_threshold()
#             print(clicks, value)
#             for word in keywords:
#                 link = get_webdriver(word)
#                 links.append(link)
#             # return "TEXT"
#             print("Keywords: ", keywords)
#             print("Links: ", links)
#             images = ''.join([f"!['some text']({link})" for link in links])
#             # images = ''.join([f"<img src={link} width='200' height='200' /> \n" for link in links])
#
#             return images


@app.callback(Output("mydiv", "children"),
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
            images = [dcc.Markdown(f"!['some text']({link})")for link in links]

            return images

        # return f"!['some text']({links[0]})"
    except TypeError:
        pass


if __name__ == '__main__':
    app.run_server(debug=True)
