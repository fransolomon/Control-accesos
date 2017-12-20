# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python 3 imports
from __future__ import absolute_import, unicode_literals

# imports
from peewee import *
from config import DB


class Entry(Model):
    operation = CharField()
    date = DateTimeField()
    useridentifier = CharField()
    username = CharField()
    extra = TextField()

    class Meta:
        database = DB  # This model uses the "registry.db" database.


class User(Model):
    useridentifier = CharField(unique=True)
    username = CharField(default='NO EN LISTA')

    class Meta:
        database = DB  # This model uses the "registry.db" database.
