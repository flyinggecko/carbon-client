#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: Andreas Rütten <andreas@smaato.com>
Copyright: Smaato Inc. 2013

Implements a carbon client which is able to send:
    - the plaintext protocol
    - the pickle protocol
'''

import socket
import struct
import cPickle
import sys

__version__ = '0.1'
__author__ = 'Andreas Rütten'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2014 Andreas Rütten'

class CarbonClient():


    def __init__(self, host, port):
        '''
        Constructor to create the carbon client
        '''
        self._host = str(host)
        self._port = int(port)

    def send_plaintext(self, name, value, timestamp):
        '''
        Send a value to carbon using the plaintext protocol
        '''
        try:
            sock = socket.socket()
            sock.connect((self._host, self._port))
        except socket.error as msg:
            print msg
            print 'Could not open socket: ' + self._host + ':' + str(self._port)
            sys.exit(1)

        sock.send("%s %f %d\n" % (name, value, timestamp))
        sock.close()

    def send_pickle(self, pickle_data):
        '''
        Send a value(s) to carbon using the pickle protocol

        The general idea is that the pickled data forms a list of multi-level tuples:

            [(path, (timestamp, value)), ...]
        '''
        payload = cPickle.dumps(pickle_data)
        header = struct.pack("!L", len(payload))
        message = header + payload

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self._host, self._port))

        except socket.error as msg:
            print msg
            print 'Could not open socket: ' + self._host + ':' + str(self._port)
            sys.exit(1)

        sock.send(message)
        sock.close()