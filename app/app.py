#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:46:24 2023

@author: kevinrojer
"""

import dash
import dash_bootstrap_components as dbc
import config


# Initialize the Dashly Application:
app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP, config.APP_STYLE])
app.title = config.APP_TITLE