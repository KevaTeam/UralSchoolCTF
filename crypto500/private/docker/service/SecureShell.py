#!/usr/bin/env python3

import subprocess
import base64

def decrypt(data):
	with open('private.key', 'r') as f:
		key = f.read()
	data = base64.b64decode(data)
	res = ""
	for i in data:
		res +=  chr(i ^ ord(key[0]))
		key = key[1:] + res[-1]
	return res

def run(cmd):
	process = subprocess.Popen(cmd.split(), stdout = subprocess.PIPE)
	cout, cerr = process.communicate()
	return (cerr if cerr else cout).decode('utf8')

commandWhiteList = 	['ls', 'cat']

def execute(data):
	try:
		cmd = decrypt(data)
		if not cmd.split(' ')[0] in commandWhiteList:
			raise Exception("Unknown comand\n")
		return run(cmd)

	except Exception as e:
		return str(e)