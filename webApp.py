# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python 3 imports
from __future__ import absolute_import, unicode_literals

# imports
from flask import Flask, render_template

# from data.models import Entry
from data.models import Entry, User

app = Flask(__name__)


@app.route("/")
def index():
    entries = Entry.select()
    return render_template('index.html', entries=entries)


@app.route("/users")
def users():
    users = User.select()
    return render_template('users.html', users=users)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5556)
