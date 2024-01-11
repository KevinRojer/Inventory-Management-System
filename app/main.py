#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:14:19 2023

@author: kevinrojer
"""

from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app
import config
from flask_login import current_user, login_user
from components.navbar import headerbar
from components.footer import footer


app.layout = dbc.Container([
    # Handle URL
    dcc.Location(id="url", refresh=False),
    #Header
    headerbar,
    # Dynamic page content
    html.Div(id="page-content"),
    #footer
    footer,
    ])
    


if __name__ == "__main__":
    app.run_server(debug=config.DEBUG, dev_tools_props_check=config.DEBUG)