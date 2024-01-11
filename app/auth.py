#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:23:50 2023

@author: kevinrojer
"""


from app import app
from flask_login import LoginManager, UserMixin
import config


# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app.server)
login_manager.login_view = "/loign"


# User Class
class User(UserMixin):
    
    def __init__(self, username):
        self.id = username
        
        
@login_manager.user_loader
def user_loader(user_id):
    return User(user_id)


def validate_user(username, password):
    if (username in config.users) and (password == config.users[password]):
        return True
    return False