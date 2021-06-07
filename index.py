#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:52:19 2021

@author: chandy
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import os

from app import app, server #need server for gunicorn index:server
from pages import page1, page2, page3
from layouts import templates

topnav = templates.topnav

layout_index = html.Div(
    [
     topnav,
     html.Header("Home Page", className='w3-center w3-padding')
    ])

url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
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
              Input('url', 'pathname'),
              Input('url', 'search'))
def display_page(pathname, search):
    if pathname == '/':
        return layout_index
    elif pathname == '/pages/page-1':
        return page1.layout
    elif pathname == '/pages/page-2':
        return page2.layout
    elif pathname == '/pages/page-3':
        return page3.gen_layout(search)
    else:
        return '404'

if __name__ == '__main__':
    if(os.environ['SERVERENV']=='DEBUG'):
        app.run_server(debug=True)
    else:
        app.run_server()