#!/usr/bin/env python

import socket

class eth_class:
 def __init__(self, ip, port):
  print('IP: ', ip, ' port=%d'%(port))

TCP_IP = ''
TCP_PORT = 5560
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
x = eth_class('192.168.2.55',TCP_PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)
while 1:
 data = conn.recv(BUFFER_SIZE)
 if not data: break
 print("received data:", data)
 conn.send(data)  # echo
conn.close()
