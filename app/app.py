#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:46:24 2023

@author: kevinrojer
"""

import dash
import dash_bootstrap_components as dbc
import config
from flask import Flask


# Set up Flask
server = Flask(__name__)

# Initialize the Dashly Application:
app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP, config.APP_STYLE],
                server=server,
                suppress_callback_exceptions=True)
app.title = config.APP_TITLE

# Configure Flask Server
server.config.update(SECRET_KEY=config.SECRET_KEY)