#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 12:41:36 2021

@author: chandy
"""

import dash_core_components as dcc
import dash_html_components as html

def generate_table(dataframe, max_rows=100):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

def generate_book_card(s):
    return html.Table([
        html.Tbody([
            html.Tr([
                html.Th('Title', scope='row'),
                html.Td(s['title'])
            ]),
            html.Tr([
                html.Th('Author', scope='row'),
                html.Td(s['author'])
            ]),
            html.Tr([
                html.Th('Publisher', scope='row'),
                html.Td(s['publisher'])
            ]),
        ])
    ])