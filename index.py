#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:52:19 2021

@author: chandy
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from pages import page1, page2

url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

layout_index = html.Div([
    dcc.Link('Navigate to "/page-1"', href='/pages/page-1'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/pages/page-2'),
])

# index layout
app.layout = url_bar_and_content_div

# "complete" layout
app.validation_layout = html.Div([
    url_bar_and_content_div,
    layout_index,
    page1.layout,
    page2.layout,
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return layout_index
    elif pathname == '/pages/page-1':
        return page1.layout
    elif pathname == '/pages/page-2':
        return page2.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)