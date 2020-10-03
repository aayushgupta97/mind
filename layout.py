import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

navbar = dbc.NavbarSimple(id="navbar",
                          brand="Maind",
                          brand_href="/",
                          color="warning",
                          dark="True",
                          sticky="top"
                          )

input_box = dcc.Input(
    id="text_field",
    type="text",
    placeholder="Enter text here...",
    maxLength=140,
    size="60",
    style={
        "padding": 7
    }
)

mkdown = html.Div(
    dcc.Markdown(id='image_container')
)

generate_button = dbc.Button(id="submit-button", children="Generate", color="primary", block=True)