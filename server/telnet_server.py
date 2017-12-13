# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python 3 imports
from __future__ import absolute_import, unicode_literals

# imports
import signal
import socket

import sys

# constants
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 10  # Normally 1024, but we want fast response

send_data = [
    b'HOLA',
    # b'Control',
    b'1E02420759 Abre',
    b'1E02420759 Maestra',
    b'1E02420759 Negra',
    b'1E02420759 Cerrado'
]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()


def stophandler(signum, frame):
    print('Program closed')
    conn.close()
    sys.exit(0)


print("Connection address: {}".format(addr))
signal.signal(signal.SIGINT, stophandler)
while True:
    # data = conn.recv(BUFFER_SIZE)
    # if not data:
    #     break
    # print("received data:".format(data))
    for data in send_data:
        print(data)
        conn.send(data)  # echo
    break

conn.close()
