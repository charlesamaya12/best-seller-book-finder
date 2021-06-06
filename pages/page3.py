#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 01:07:18 2021

@author: chandy
"""

import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from app import best_seller_history

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
        className='w3-card-4 w3-blue w3-cell width:50%'
    )
    return book_card

def history_chart(title="", author=""):
    data = best_seller_history[best_seller_history['title']=="THEY BOTH DIE AT THE END"]
    fig = px.line(data, x="bestsellers_date", y="rank", color='title', template='plotly_white')
    fig.update_traces(mode='lines+markers', line_shape='spline')
    fig['layout']['yaxis']['autorange'] = "reversed"
    fig.update_layout(legend_title_text='Titles')
    return fig


page_layout = html.Div(
        [
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




