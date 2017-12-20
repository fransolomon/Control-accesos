# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python 3 imports
from __future__ import absolute_import, unicode_literals

# imports
from flask import Flask, render_template

from ..data.models import Entry

app = Flask(__name__)


@app.route("/")
def index():
    entries = Entry.filter()
    return render_template('index.html', entries=entries)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5556)
