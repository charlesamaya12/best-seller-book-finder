#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 01:07:18 2021

@author: chandy
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app, best_seller_history

from layouts import templates
from utils import helpers

topnav = templates.topnav

def book_card(title="", author=""):
    book = best_seller_history.iloc[0, :]
    book_card = html.Div(
        html.Div(
            [
            html.A(
                html.Img(
                    src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=0062457802&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bestsellerbookfinder-20",
                    className='w3-card'
                ),
                href="https://www.amazon.com/gp/product/0062457802/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0062457802&linkCode=as2&tag=bestsellerbookfinder-20&linkId=3a919631bc9cbe27d4b70c7a7a5156fc", 
                target='_blank',
            ),
            helpers.generate_book_card(book)
            ],
            className='w3-container w3-center w3-padding'
        ),
        className='w3-card-4 w3-blue w3-cell'
    )
    return book_card

def history_chart(title="", author=""):
    data = best_seller_history[best_seller_history['title']=="THEY BOTH DIE AT THE END"]
    fig = px.line(data, x="bestsellers_date", y="rank", color='title', template='plotly_white')
    fig.update_traces(mode='lines+markers', line_shape='spline')
    fig['layout']['yaxis']['autorange'] = "reversed"
    fig.update_layout(legend_title_text='Titles')
    return fig

all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}


page_layout = html.Div(
        [
            dcc.RadioItems(
                id='countries-radio',
                options=[{'label': k, 'value': k} for k in all_options.keys()],
                value='America'
            ),
        
            html.Hr(),
        
            dcc.Dropdown(id='cities-dropdown'),
        
            html.Hr(),
        
            html.Div(id='display-selected-values'),
            dcc.Graph(
                id='best-seller-history',
                figure=history_chart()
            ),
            book_card()
        ],
        className='w3-cell-row'
    )


layout = html.Div([topnav, page_layout])

#dcc.Location(id='url', refresh=False)


@app.callback(
    Output('cities-dropdown', 'options'),
    Input('countries-radio', 'value'))
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@app.callback(
    Output('cities-dropdown', 'value'),
    Input('cities-dropdown', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']


@app.callback(
    Output('display-selected-values', 'children'),
    Input('countries-radio', 'value'),
    Input('cities-dropdown', 'value'))
def set_display_children(selected_country, selected_city):
    return u'{} is a city in {}'.format(
        selected_city, selected_country,
    )




