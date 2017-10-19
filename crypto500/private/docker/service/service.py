#!/usr/bin/env python3

import sys
from SecureShellServer import SecureShellServer

if __name__ == '__main__':
	if not len(sys.argv) == 3:
		print("Invalid number of arguments")
		exit(-1)
	
	print("Starting server...")
	try:
		SecureShellServer(sys.argv[1], int(sys.argv[2])).listen()
	except Exception as e:
		print("Server error")
		print(str(e))
		exit(-2)