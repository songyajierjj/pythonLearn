#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
HOST = ''
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
	conn, addr = s.accept()
	print('客户端地址', addr)
	data = conn.recv(1024)
	print("获取信息：", data.decode("UTF-8"))
	if not data:
		break
	conn.sendall(data)
conn.close()
