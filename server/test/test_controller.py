# -*- coding: utf-8 -*-
"""
License boilerplate should be used here.
"""

# python 3 imports
from __future__ import absolute_import, unicode_literals

# imports
import unittest
from unittest.mock import patch, MagicMock

# app imports
from server.controller import Server


class TestServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.telnet_patcher = patch('telnetlib.Telnet')
        cls.telnet_mock = cls.telnet_patcher.start()

        super(TestServer, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.telnet_patcher.stop()
        super(TestServer, cls).tearDownClass()

    def setUp(self):
        self.server = Server()
        # until = MagicMock()
        # until.side_effect = [
        #     True,
        #     b'HOLA',
        #     b'Control',
        #     b'1E02420759 Abre',
        #     b'1E02420759 Maestra',
        #     b'1E02420759 Negra',
        #     b'1E02420759 Cerrado'
        # ]
        # self.telnet_mock.read_until = until
        self.telnet_mock.open = MagicMock(return_value=True)

    def test_connect(self):
        self.server.connect()
        self.telnet_mock.assert_called_once()

    def test_operate_invalid_username(self):
        message = self.server.operate('1E0242075 Abre')
        self.assertEqual(message, 'Invalid username at {}')

    def test_operate_open(self):
        message = self.server.operate('1E02420759 Abre')
        self.assertEqual(message, 'Open at {}')

    def test_operate_master(self):
        message = self.server.operate('1E02420759 Maestra')
        self.assertEqual(message, 'Master at {}')

    def test_operate_banned(self):
        message = self.server.operate('1E02420759 Negra')
        self.assertEqual(message, 'Banned at {}')

    def test_operate_close(self):
        message = self.server.operate('1E02420759 Cerrado')
        self.assertEqual(message, 'Not Allowed at {}')


if __name__ == '__main__':
    unittest.main()
