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


def decrypt1000(text, file_name):
    f = open(file_name)
    keys = f.read().split("\n")
    for key in keys[-2::-1]:
        text = decrypt(text, key)
    return text


cipher = "Olussa!dev akdby{_sferutfnmceofs1iwnmI_0skmtw_fd}jasoeijnl_,ftme"
file_name = "keys.txt"

print(decrypt1000(cipher, file_name))
