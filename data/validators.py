# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python 3 imports
from __future__ import absolute_import, unicode_literals

# imports
from peewee_validates import validate_regexp, StringField, Validator


class UserValidator(Validator):
    username = StringField()

    def clean(self, data):
        validator = validate_regexp('^[A-Z0-9]{10}$', flags=0)
        validator(self.username, data)
        return data
