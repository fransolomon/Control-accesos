# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# imports
import os

from peewee import SqliteDatabase

CURRENT_PATH = os.getcwd()
DATABASE_PATH = os.path.join(CURRENT_PATH, 'server', 'data', 'registry.db')
DB = SqliteDatabase(DATABASE_PATH)
