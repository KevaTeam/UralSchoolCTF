#!/usr/bin/env python3

import string
from collections import OrderedDict

keySlogan = "CTF IS SO SIMPLE"

def keygen(slogan):
	abc = string.ascii_lowercase
	buf = ''.join(OrderedDict.fromkeys(slogan.lower().replace(' ', '')))
	for i in abc:
		if not i in buf: buf += i
	key = dict()
	for i, j in zip(abc, buf):
		key[i] = j
	
	return key

k = keygen(keySlogan)

flag = "uralctf{Time to rock it from the Delta to the DMZ}".lower().replace(' ', '')
with open("falg.txt", "w") as f:
	f.write(flag)

crypt = ""
for i in flag:
	if i in k:
		crypt += k[i]
	else:
		crypt += i

with open("../public/data", "w") as f:
	f.write(crypt)