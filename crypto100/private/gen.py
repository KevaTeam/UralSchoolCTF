#!/usr/bin/env python3

def foo(data):
	return '|'.join([str(ord(i.lower()) - ord('a') + 1) for i in data])

payload = foo("whatdoyouknowaboutabc")

flag = "uralctf{" +payload + "}"
print(flag)