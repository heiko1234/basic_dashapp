import dash
from dash import html, dcc
from dash import callback_context


from app.utilities.cards import (
    home_card
)


dash.register_page(__name__,path="/")

# dash.register_page(
#     __name__,
#     path='/second',
#     title='Home Dashboard',
#     name='Home Dashboard'
# )


layout = html.Div(
    children=[
        home_card(
            id="landingcard",
            header_text="Landing page",
            text="this is the landing page",
            href="landing"
        ),
        home_card(
            id="datacard",
            header_text="Data",
            text="this is the data page",
            href="data"
        ),
    ],
)

