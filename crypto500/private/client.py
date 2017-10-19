#!/usr/bin/env python3

import socket
import base64

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

client.connect(('localhost', 9999))


def encrypt(data):
	key = "ftclaru"
	res = ""
	for i in data:
		key += i
		res += chr(ord(i) ^ ord(key[0]))
		key = key[1:]
	return base64.b64encode(bytes(res, "utf8"))

while True:
	cmd = input("input command: ")
	print(cmd)
	data = encrypt(cmd)
	print(data)
	with open('../public/' + cmd + '.cmd', 'w') as f:
		f.write(data.decode("utf8"))
	client.send(data)
	print("result:\n{}".format(client.recv(10000).decode('utf8')))

client.close()