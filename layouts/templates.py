#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 22:49:48 2021

@author: chandy
"""

import dash_core_components as dcc
import dash_html_components as html


topnav = html.Div(
    className='w3-bar w3-border w3-light-green w3-row',
    children=[
        dcc.Link(
            html.Img(src='/assets/logo-big.png', alt='HOME'), 
            href='/', className='w3-bar-item'),
        dcc.Link('PAGE1', href='/pages/page-1', 
                 className='w3-bar-item w3-button w3-right'),
        dcc.Link('PAGE2', href='/pages/page-2', 
                 className='w3-bar-item w3-button w3-right'),
        dcc.Link('PAGE3', href='/pages/page-3', 
                 className='w3-bar-item w3-button w3-right'),
    ])