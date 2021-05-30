#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:37:10 2021

@author: chandy
"""

import dash
import pandas as pd

app = dash.Dash(__name__, suppress_callback_exceptions=False)
server = app.server

best_seller_history = pd.read_csv('nyt-best-sellers-best_seller_history.csv')
