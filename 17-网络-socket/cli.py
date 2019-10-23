#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
HOST = 'localhost'
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = '123'
while data:
	s.sendall(data.encode('UTF-8'))
	data = s.recv(512)
	print(data)
	print("获取服务器信息：\n", data.decode())
	data = input("请输入信息：\n")
s.close()
