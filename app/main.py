#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:14:19 2023

@author: kevinrojer
"""


import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from app import app
import auth
import config


app.layout = dbc.Container([
    # Nav bar
    html.Nav(
        children=[
            html.Div([
                html.A('Home', href='/'),
                html.A('About', href='/about'),
                html.A('Contact', href='/contact')
            ], className='nav-links'),
        ],
        id="nav-bar",
        className='navbar'
    ),
    
    # Dynamic Page content
    dcc.Location(id='url', refresh=True),
    html.Div(id="page-content"),
    
    # Footer
    html.Div([], id="footer-content"),
    ])

@app.callback(Output('page-content', 'children'),
          [Input('url', 'pathname')])

def display_page(pathname):
    # Redirect to login page if not logged in
    if pathname == '/login' or pathname == '/':
        return auth.login_layout
    else:
        # Logic to display other pages after successful login
        # This can be your home page or other content pages
        # e.g., return home_layout if pathname == '/home'
        pass
    
if __name__ == '__main__':
    app.run_server(debug=True)