import re


def solve():
    f = open('num.txt')
    summ = [0]*36
    for line in f:
        t = re.findall(r"\-?\d+", line)
        if t:
            for x in range(36):
                summ[x] += int(t[x])

    print("".join(map(chr, map(lambda x: x%256,summ))))


solve()
