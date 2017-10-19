#!/usr/bin/env python3

block_length = 10

key = [2, 7, 8, 3, 9, 1, 5, 6, 0, 4]

def foo(flag):
	l = len(flag)%block_length
	if l:
		flag += ' '*(block_length - l)
	flag = list(flag)
	l = len(flag)//block_length
	for i in range(0, len(flag), block_length):
		buf = flag[i:(i+block_length)]
		for j in range(block_length):
			flag[i+key[j]] = buf[j]
		print(buf)
	return(''.join(flag))

payload = "Every day I'm shuffling Shuffling shuffling".replace(' ', '').lower()
flag = "uralctf{" + payload + "}"
with open("flag.txt", "w") as f:
	f.write(flag)

crypt = foo(flag)
print(flag)
print(crypt)

with open("../public/data", "w") as f:
	f.write(crypt)