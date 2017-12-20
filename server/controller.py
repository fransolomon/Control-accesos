# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python 3 imports
from __future__ import absolute_import, unicode_literals

import signal
import sys
import telnetlib
# imports
from datetime import datetime

from data.models import Entry, User

from data.validators import UserValidator


# app imports


def stophandler(signum, frame):
    print('Program closed')
    sys.exit(0)


class Server:
    def __init__(self, host='127.0.0.1', port=5005, timeout=10):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.start_time = datetime.now()
        self.active = True

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

    def connect(self):
        print("Connect to IP:{} Port:{} at {}".format(
            self.host, self.port, self.start_time
        ))
        t = telnetlib.Telnet()
        # t.close()
        t.open(self.host, port=self.port)
        return t

    def main(self):
        signal.signal(signal.SIGINT, stophandler)
        try:
            t = self.connect()
            while self.active:
                telnetinput = t.read_until(b"HOLA", 1)
                telnetinput = str(telnetinput, 'utf-8')

                start_time = datetime.now()
                self.start_time = start_time

                if "Control" in telnetinput:
                    message = "Control at {}"
                else:
                    message = self.operate(telnetinput)

                print(message.format(start_time.isoformat()))

        except Exception as e:
            print(e)
            print("fail connection...")

    def operate(self, telnetinput):
        message = '{}'
        useridentifier = telnetinput[0:11]
        useridentifier = useridentifier.strip()

        validator = UserValidator()

        valid = validator.validate({'username': useridentifier})
        if not valid:
            message = 'Invalid username at {}'
            return message

        user, created = User.get_or_create(
            useridentifier=useridentifier)
        entry = Entry(
            date=self.start_time,
            useridentifier=useridentifier,
            username=user.username,
            extra=telnetinput
        )

        if "Abre" in telnetinput:  # ex. C64BFCC4B5 Abre
            message = "Open at {}"
            entry.operation = 'Abre'
            entry.save()
        elif "Maestra" in telnetinput:  # ex. 1E02420759 Abre 1E02420759 Maestra
            message = "Master at {}"
            entry.operation = 'Maestra'
            entry.save()
        elif "Negra" in telnetinput:  # ex. 3B4BFCD05C Negra
            message = "Banned at {}"
            entry.operation = 'Negra'
            entry.save()
        elif "Cerrado" in telnetinput:  # ex. 6A4BFCE439 Cerrado
            message = "Not Allowed at {}"
            entry.operation = 'Cerrado'
            entry.save()

        return message
