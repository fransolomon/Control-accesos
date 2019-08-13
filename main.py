# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python 3 imports
from __future__ import absolute_import, unicode_literals

# imports

# app imports
from server.controller import Server

# constants
HOST = "127.0.0.1"
PORT = 5005
TIMEOUT = 10

if __name__ == '__main__':
    server = Server(HOST, PORT, TIMEOUT)
    server.main()
