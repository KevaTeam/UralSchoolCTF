from random import randint
import re


flag = "uralctf{iI's_s00_eASy_manN!Cookie#^}"


def gen():
    f = open('num.txt', 'w')
    num = []
    summ = [0]*len(flag)
    for y in range(999):
        t = []
        for x in range(len(flag)):
            c = randint(-1000,1000)
            t.append(c)
            summ[x] += c
        num.append(t)

    t = []
    for x in range(len(flag)):
        c = ord(flag[x]) - summ[x] % 256
        t.append(c)

    num.append(t)

    for y in num:
        f.write((" ".join(map(str,y)))+"\n")

    f.close()

        
def solve():
    f = open('num.txt')
    summ = [0]*len(flag)
    for line in f:
        t = re.findall(r"\-?\d+", line)
        if t:
            for x in range(len(flag)):
                summ[x] += int(t[x])

    print("".join(map(chr, map(lambda x: x%256,summ))))


gen()
solve()
