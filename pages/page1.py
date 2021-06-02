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

topnav = html.Div(
    className='w3-bar w3-border w3-light-grey',
    children=[
        dcc.Link('HOME', href='/', 
                 className='w3-bar-item w3-button w3-mobile'),
        dcc.Link('PAGE1', href='/pages/page-1', 
                 className='w3-bar-item w3-button w3-mobile w3-right w3-light-blue'),
        dcc.Link('PAGE2', href='/pages/page-2', 
                 className='w3-bar-item w3-button w3-mobile w3-right'),
    ])

fig1 = px.line(best_seller_history, x="bestsellers_date", y="rank", color='title', template='plotly_white')
fig1.update_traces(mode='lines+markers', line_shape='spline')
fig1['layout']['yaxis']['autorange'] = "reversed"
fig1.update_layout(legend_title_text='Titles')

chart_layout = html.Div([
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

layout = html.Div([topnav, chart_layout])


@app.callback(
    Output('page-1-display-value', 'children'),
    Input('page-1-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)