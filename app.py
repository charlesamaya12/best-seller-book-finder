#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:37:10 2021

@author: chandy
"""

import dash
import pandas as pd

external_stylesheets = ['https://www.w3schools.com/w3css/4/w3.css']

app = dash.Dash(__name__, suppress_callback_exceptions=False, 
                external_stylesheets=external_stylesheets,
                title='BestSellerBookFinder')
server = app.server

best_seller_history = pd.read_csv('nyt-best-sellers-best_seller_history.csv')

genre_title_tree = []
for genre in best_seller_history['display_name'].unique():
    titles = best_seller_history[best_seller_history['display_name']==genre]['title'].unique()
    genre_title_tree.append((genre, titles))

genre_title_tree = dict(genre_title_tree)
genre_title_tree['ALL'] = list(genre_title_tree.values())[0]