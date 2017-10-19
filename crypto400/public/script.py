#!/usr/bin/env python3

import string

abc = "{" + string.ascii_lowercase + "}"


def strToInt(s):
	return [abc.index(i) for i in s]

def intToStr(h):
	return ''.join([abc[i] for i in h])

def shift(s, n):
	return s[n:] + s[:n] 

def cesir(s, n = 4):
	key = {i: j for i, j in zip(abc, shift(abc, n))}
	return ''.join([key[i] for i in s])

def rot14(s):
	key = {i: j for i, j in zip(abc, shift(abc, 14))}
	return ''.join([key[i] for i in s])

def add(b, n):
	return [(i + n + 28) % 28 for i in b]

with open("flag.txt", "r") as f:
	flag = f.read()

with open("key", "r") as f:
	key = int(f.read())

with open("data", "w") as f:
	f.write(intToStr(shift(add(strToInt(cesir(rot14(shift(intToStr(add(strToInt(shift(flag, 12)), key)), 13)), key)), (len(string.ascii_lowercase) - len(abc))*key), 4)))