#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 23:40:44 2024

@author: kevinrojer
"""


from dash import html
import dash_bootstrap_components as dbc
import config

headerbar = dbc.Navbar([
    dbc.NavbarBrand([
        html.Img(src=config.LOGO_SVG)
        ], id="logo-img", href="/"),
    ], id="header-nav-bar")


navbar = dbc.Tabs([
    dbc.Tab(label="Dashboard", tab_id="dashboard-tab"),
    dbc.Tab(label="Inventory", tab_id="inevtory-tab"),
    dbc.Tab(label="Suppliers", tab_id="suppliers-tab")
    ], id="tabs-nav-bar", active_tab="dashboard-tab")