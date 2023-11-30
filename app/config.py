#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:32:55 2023

@author: kevinrojer
"""


# Dashly application configuration settings

# App title and description
APP_TITLE = "Inventory Management System"
APP_DESCRIPTION = "Manage staff, reviews, and analytics."

# # Dashly app layout
# APP_LAYOUT = {
#     "title": APP_TITLE,
#     "meta_tags": [{"name": "description", "content": APP_DESCRIPTION}],
# }

# Stylesheets
APP_STYLE = "/assets/style.css"
FA_STYLE = "https://use.fontawesome.com/releases/v6.4.2/css/all.css"

# Server configuration
DEBUG = True  # Set to False in production
HOST = "0.0.0.0"
PORT = 8050  # Choose an appropriate port

# Database configuration
DATABASE_URI = "mysql://username:password@localhost:5432/staff_db"

# Secret key for session management (change in production)
SECRET_KEY = "your-secret-key"

# User roles
ROLES = {"admin", "manager", "employee"}

# External APIs and services
SUPPLIER_API_KEY = "your-supplier-api-key"

# Logging configuration
LOG_LEVEL = "INFO"

# Email configuration for notifications and password resets
SMTP_HOST = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your-email@example.com"
SMTP_PASSWORD = "your-email-password"

# Analytics and reporting settings
ANALYTICS_ENABLED = True

# Other application-specific configuration parameters
# ...

# Flask-Security settings (if applicable)
SECURITY_PASSWORD_SALT = "your-password-salt"

# Additional settings for extensions and libraries
# ...

# Environment-specific configuration (e.g., development, production)
# ...

# Asset specific configuration
PP_LOGO_SVG = r"\assets\pp_logo_svg.svg"

# You can define functions or classes to read configuration from environment variables or files
