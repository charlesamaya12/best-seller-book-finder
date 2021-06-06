#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:44:47 2021

@author: chandy
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import best_seller_history

from layouts import templates
from utils import helpers

topnav = templates.topnav


markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

showcols = ['rank', 'title', 'author', 'publisher', 'bestsellers_date', 'display_name']

table_layout = html.Div([
    html.H2('Page 2'),
    dcc.Dropdown(
        id='page-2-dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='page-2-display-value'),
    html.Br(),
    dcc.Link('Navigate to Home', href='/'),
    html.Br(),
    dcc.Link('Navigate to Page 1', href='/pages/page-1'),
    html.Br(),
    dcc.Markdown(children=markdown_text),
    helpers.generate_table(best_seller_history[showcols])
])

layout = html.Div(
    [
     topnav,
     table_layout
    ])

@app.callback(
    Output('page-2-display-value', 'children'),
    Input('page-2-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)