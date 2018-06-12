"""
spamc: eventlet backend
"""
# pylint: disable=unused-import,invalid-name,no-member
# from eventlet.green import select
from eventlet import sleep
from eventlet.green.socket import socket

Socket = socket
# Select = select.select
assert sleep
