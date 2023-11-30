#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:28:06 2023

@author: kevinrojer
"""


import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from app import app
import config


layout = dbc.Container([
    # Email input
    dbc.Row([
        dbc.Label("Email"),
        dbc.Input(""),
        ])
    ])