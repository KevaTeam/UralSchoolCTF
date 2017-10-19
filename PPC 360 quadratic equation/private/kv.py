from random import randint
from re import findall
import socket
from threading import Thread
import time


PORT = 8060
flag = "uralctf{Yeahh_It's Aw3s0mE!Grac}"

SecLimit = 30


def gen_x(len_x, R2):
    if len_x == 2:
        if R2<2:
            return 0, randint(-999,999)
        elif R2<4:
            x = randint(-999,999)
            return -x, x
        else:
            return randint(-999,999), randint(-999,999)
    elif len_x == 1:
        if R2 == 0:
            return 0, 0
        x = randint(-999,999)
        return x, x
    else:
        return "None"


def gen_abc(x):
    a = randint(-10,10)
    while a == 0:
        a = randint(-10,10)
    if len(x) == 2:
        b = -a*(x[0]+x[1])
        c = a*x[0]*x[1]
    elif x == "None":
        c = randint(-9999,9999)
        b = randint(-99,99)
        while b**2 >= 4*a*c:
            c = randint(-9999,9999)
            b = randint(-99,99)
    else:
        b = 2*a*x[0]
        c = a*x[0]**2
        
    return a,b,c        
    

def compl_ur(a, b, c):
    us = "%dX^2" % a
    if b>0:
        us += "+"
        us += "%dX" % b
    elif b<0:
        us += "%dX" % b
    if c>0:
        us += "+"
        us += "%d" % c
    elif c<0:
        us += "%d" % c
    us += "=0"
    return us


def l(R1):
    if R1<1:
        len_x = 0
    elif R1<4:
        len_x = 1
    else:
        len_x = 2
    return len_x


def kv(conn):
    R1, R2 = randint(0,9), randint(0,9)
    len_x = l(R1)
    x = gen_x(len_x,R2)
    print(x)
    a,b,c = gen_abc(x)
    us = compl_ur(a, b, c)
    conn.send((us+"\n> ").encode("utf-8"))
    res = conn.recv(128).decode('utf-8')
    if res[:4] == "None":
        if len_x == 0:
            return True
        else:
            return False
    input_x = findall(r"(\-?\d+) (\-?\d+)", res)
    if input_x[0] == (str(min(x)), str(max(x))):
        return True
    else:
        return False


def task(conn):
    try:      
        t = time.time()
        conn.send(('Hi! You have 30 sec!\n').encode("utf-8"))
                    
        for i in range(100):
            if abs(time.time() - t) > SecLimit:
                conn.send(('Time is up!\n').encode("utf-8"))
                conn.close()
                return

            if not kv(conn):
                conn.send(('Answer incorrect!\n').encode("utf-8"))
                conn.close()
                return

        conn.send(('Flag: %s\n' %flag).encode("utf-8"))
        conn.close()
        return
    
    except:
        conn.close()
        return


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', PORT))
sock.listen(1)

try:
    while True:
        conn, addr = sock.accept()  

        thr = Thread(target=task, args=(conn,))
        thr.start()
except:
    conn.close()

