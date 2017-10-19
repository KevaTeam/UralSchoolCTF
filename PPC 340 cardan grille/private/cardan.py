import pprint
from random import choice
from math import trunc


flag = "uralctf{1ts_muffIn_time,s0mebody_sOlve_me!}"
text = flag + " sfkjenskfnjsaiowdadw"
file_name = "/home/fascinsun/Documents/ppc ugra/ppc 100/keys.txt"
cipher = "Oaussr!dev akdby{_sfegutfnmceofs1iwnmI_0skmtw_fd}jasoeijnl_,ftme"


def set_xy(N, a):
    func = {
        0: lambda N: [N%4, trunc(N/4)],
        1: lambda N: [7-trunc(N/4), N%4],
        2: lambda N: [trunc(N/4), 7-(N%4)],
        3: lambda N: [7-(N%4), 7-trunc(N/4)]}
    return func[a](N)


def genmap():
    key = [int(choice("0123")) for _ in range(16)]
    kmap = [[0 for _ in range(8)] for _ in range(8)]
    for i, val in enumerate(key):
        x, y = set_xy(i, val)
        kmap[y][x] = 1
    return kmap


def map_to_hex(kmap):
    key = ""
    for i in kmap:
        h = hex(int(''.join(list(map(str, i))),2))[2:]
        while len(h) < 2:
            h = '0' + h
        key += h
    return key


def hex_to_map(key):
    kmap = []
    for i in range(0,16,2):
        b = bin(int(key[i:i+2], 16))[2:]
        while len(b) < 8:
            b = '0' + b
        kmap.append([int(j) for j in b])
    return kmap


def rotation(kmap):
    new_kmap = [[0 for _ in range(8)] for _ in range(8)]
    for x in range(8):
        for y in range(8):
            new_kmap[y][x] = kmap[7-x][y]
    return new_kmap


def encrypt(text, key):
    kmap = hex_to_map(key)
    cipher = [['0' for _ in range(8)] for _ in range(8)]
    k, r = 0, 0

    while r < 4:
        for y in range(8):
            for x in range(8):
                if kmap[y][x]:
                    cipher[y][x] = text[k]
                    k += 1
        kmap = rotation(kmap)
        r += 1
        
    c = ''.join(cipher[y][x] for y in range(8) for x in range(8))
    return c


def decrypt(cipher, key):
    kmap = hex_to_map(key)
    c = [[j for j in cipher[i:i+8]] for i in range(0,64,8)]
    text = ""
    k, r = 0, 0

    while r < 4:
        for y in range(8):
            for x in range(8):
                if kmap[y][x]:
                    text += c[y][x]
                    k += 1
        kmap = rotation(kmap)
        r += 1
        
    return text


def encrypt100(text, file_name):
    f = open(file_name)
    for line in f:
        key = line[:16]
        text = encrypt(text, key)
    return text


def decrypt100(text, file_name):
    f = open(file_name)
    keys = f.read().split("\n")
    for key in keys[-2::-1]:
        text = decrypt(text, key)
    return text


cipher = encrypt100(text, file_name)
print(cipher)
print(decrypt100(cipher, file_name))
