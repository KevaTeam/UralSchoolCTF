#!/usr/bin/env python3

import socket
import threading
from SecureShell import execute

class SecureShellServer(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind((self.host, self.port))

	def listen(self):
		self.sock.listen(100)
		while True:
			client, addr = self.sock.accept()
			client.settimeout(30)
			threading.Thread(target = self.shell, args = (client, addr)).start()

	def shell(self, client, addr):
		size = 100
		print("Have a new connection with address: {}".format(addr))
		while True:
			try:
				data = client.recv(size)
				if data:
					res = (execute(data) + '\n').encode('utf8')
					client.send(res)
				else:
					raise Exception('Client disconnected')
			except Exception as e:
				client.send(bytes(str(e), 'utf8'))
				client.close()
				print(str(e))
				return

if __name__ == '__main__':
	SecureShellServer('', 9999).listen()