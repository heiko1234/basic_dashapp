

from pydoc import classname
from dash import html, dcc


def home_card(
        id,
        header_text,
        text,
        href
):
    output = html.Div(
        className="gnc",
        id=id,
        children=[
            html.Div(
                className="gnc-body",
                children=[
                    html.A(
                        className="gnc-card-container",
                        id=f"{id}_container",
                        href=href,
                        children=[
                            html.Div(
                                className="gnc-topbar",
                                children=[
                                    html.Div(id=f"{id}_topbar")
                                ]
                            ),
                            html.H2(
                                className="gnc-header_text",
                                children=header_text
                            ),
                            html.P(
                                className="gnc-description",
                                children=text
                            )
                        ]
                    )
                ]
            )
        ]
    )
    return output



