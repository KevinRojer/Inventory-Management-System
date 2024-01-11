#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 23:57:46 2024

@author: kevinrojer
"""


from dash import html
import dash_bootstrap_components as dbc


footer = dbc.Container([
    dbc.Row([
        html.Footer(
            html.P("2024 Click Genics & Partners. All rights reserved",
                   className="footer-text"),
            )
        ], className="footer-bar")
    ])