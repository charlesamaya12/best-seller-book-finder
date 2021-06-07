#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 01:07:18 2021

@author: chandy
"""
import urllib.parse as upr

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app, best_seller_history, genre_title_tree

from layouts import templates
from utils import helpers

topnav = templates.topnav

def book_card(title="", author=""):
    if(title==''):
        data = best_seller_history[best_seller_history['title']=="THEY BOTH DIE AT THE END"]
    else:
        data = best_seller_history[best_seller_history['title']==title]
    book = data.iloc[0, :]
    best_rank = data['rank'].min()
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
            #helpers.generate_book_card(book)
            html.Table([
                html.Tbody([
            html.Tr([
                html.Th('Title', scope='row'),
                html.Td(book['title'])
            ]),
            html.Tr([
                html.Th('Author', scope='row'),
                html.Td(book['author'])
            ]),
            html.Tr([
                html.Th('Best Rank', scope='row'),
                html.Td('#'+str(best_rank))
            ]),
        ])
    ])
            ],
            className='w3-container w3-center w3-padding'
        ),
        className='w3-card-4 w3-blue w3-cell'
    )
    return book_card

def history_chart(title='', author=""):
    if(title==''):
        data = best_seller_history[best_seller_history['title']=="THEY BOTH DIE AT THE END"]
    else:
        data = best_seller_history[best_seller_history['title']==title]
    fig = px.line(data, x="bestsellers_date", y="rank", color='title', template='plotly_white')
    fig.update_traces(mode='lines+markers', line_shape='spline')
    fig['layout']['yaxis']['autorange'] = "reversed"
    fig.update_layout(legend_title_text='Titles')
    return fig

all_options = genre_title_tree


def gen_page_layout(title=''): 
    return html.Div(
        [        
            dcc.Graph(
                id='best-seller-history',
                figure=history_chart(title)
            ),
            book_card(title)
        ],
        className='w3-cell-row'
    )

def gen_layout(search_query=''):
    title = ''
    if(len(search_query) > 0):
        if(search_query[0]=='?'):
            param_string = search_query[1:]
            parsed = upr.parse_qs(param_string)
            if('title' in list(parsed.keys())):
                title = parsed['title'][0]

    return html.Div([topnav, gen_page_layout(title)])

#layout = gen_layout()


#@app.callback(
#    Output('title-dropdown', 'options'),
#    Input('genre-dropdown', 'value'))
#def set_cities_options(selected_country):
#    return [{'label': i, 'value': i} for i in all_options[selected_country]]


#@app.callback(
#    Output('title-dropdown', 'value'),
#    Input('title-dropdown', 'options'))
#def set_cities_value(available_options):
#    return available_options[0]['value']






