#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:44:10 2021

@author: chandy
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app
from app import best_seller_history


fig1 = px.line(best_seller_history, x="published_date", y="rank", color='title')
fig1.update_traces(mode='lines+markers')
fig1['layout']['yaxis']['autorange'] = "reversed"
fig1.update_layout(transition_duration=500)

layout = html.Div([
    html.H3('Page 1'),
    dcc.Dropdown(
        id='page-1-dropdown',
        options=[
            {'label': 'Page 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='page-1-display-value'),
    dcc.Link('Go to Page 2', href='/pages/page-2'),
    html.Br(),
    dcc.Link('Navigate to Home', href='/'),
    html.Br(),
    html.H4(children='Best Seller History'),
    dcc.Graph(
        id='best-seller-history',
        figure=fig1
    ),
])


@app.callback(
    Output('page-1-display-value', 'children'),
    Input('page-1-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)