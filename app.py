#!/usr/bin/env python
import os

port = os.environ.get('SOCKS5_PORT', '8080')
user = os.environ.get('SOCKS5_USER', '')
password = os.environ.get('SOCKS5_PASSWORD', '')

if (not user) or (not password):
	startup = ("--port=%s" % port) 
else:
	startup = ("--port=%s  --auth=%s:%s" % (port, user, password))

os.system("python socks5.py start %s" % startup)
