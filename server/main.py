# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python 3 imports
from __future__ import absolute_import, unicode_literals

# app imports
import signal
import telnetlib
from datetime import datetime

# constants
import sys

HOST = "10.10.0.159"
PORT = 80
TIMEOUT = 10


def stophandler(signum, frame):
    print('Program closed')
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, stophandler)
    try:
        print("Conectando con IP:{} Puerto:{}".format(HOST, PORT))
        t = telnetlib.Telnet()
        t.close()
        t.open(HOST, port=PORT)
        while True:
            telnetinput = t.read_until("HOLA", 1)
            start_time = datetime.now()
            # print "En espera ... "
            if "Control" in telnetinput:
                print("Control at {}".format(start_time.isoformat()))
            elif "Abre" in telnetinput:  # ex. C64BFCC4B5 Abre
                print("Open at {}".format(start_time.isoformat()))
                # TODO store data
            elif "Maestra" in telnetinput:  # ex. 1E02420759 Abre 1E02420759 Maestra
                print("Master at {}".format(start_time.isoformat()))
                # TODO store data
            elif "Negra" in telnetinput:  # ex. 3B4BFCD05C Negra
                print("Banned at {}".format(start_time.isoformat()))
                # TODO store data
            elif "Cerrado" in telnetinput:  # ex. 6A4BFCE439 Cerrado
                print("Not allowed at {}".format(start_time.isoformat()))
                # TODO store data
    except Exception:
        print("fail connection...")
        pass


if __name__ == '__main__':
    main()
