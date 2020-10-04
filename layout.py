import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

navbar = dbc.NavbarSimple(id="navbar",
                          brand="m(Ai)nd",
                          brand_href="/",
                          color="#2f4649",
                          dark="True",
                          sticky="top",
                          brand_style={"font-size": 40}
                          )

input_box = dcc.Input(
    id="text_field",
    type="text",
    placeholder="Enter text here...",
    maxLength=280,
    size="60",
    style={
        "padding": 30
    }
)

mkdown = html.Div(
    dcc.Markdown(id='image_container')
)

generate_button = dbc.Button(id="submit-button", children="Generate", color="primary", block=True, style={"padding": 25, "font-size": 30})