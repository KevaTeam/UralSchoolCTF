import socket
from random import *
from threading import Thread
import time


PORT = 8050

flag = "uralctf{Ave_%username%_4v3_%us3rn4m3%!}"

emp = '.'
cat = '@'
mou = '&'

# Не использовать карту размером меньше 30 X 30!
X, Y = 80, 38

SecLimit = 10


def game(conn):
    try:      
        t = time.time()
            
        # Размер игровой карты по x и y
        cX, cY = randint(0,3), randint(0,3)
        mX, mY = randint(X-4,X-1)-10, randint(Y-4,Y-1)-10

        # Генерация пустой карты
        gamemap = list(list(emp for x in range(X)) for y in range(Y))
        gamemap[cY][cX] = cat
        gamemap[mY][mX] = mou
        
        for i in range(100):
            if abs(time.time() - t) > SecLimit:
                conn.send(('Time is up!\n').encode("utf-8"))
                conn.close()
                return()

            conn.send(make(gamemap).encode('utf-8'))
            conn.send(b"\n> ")
            data = conn.recv(256).decode('utf-8')
            er, gamemap, cX, cY = stepcat(data, gamemap, cX, cY, mX, mY)
            if (cX, cY) == (mX, mY):
                conn.send(('Flag: %s\n' %flag).encode("utf-8"))
                conn.close()
                return()
            if not er:
                conn.close()
                return()
            gamemap, mX, mY = stepmouse(gamemap, cX, cY, mX, mY)
    except:
        conn.close()
        return()
    

def make(m):
    res = ''
    for y in range(Y):
        for x in range(X):
            res += m[y][x]
            if x==X-1 and y!=Y-1:
                res += '\n'
    return(res)


def stepcat(step, gamemap, cX, cY, mX, mY):
    h = step.split(',')
    h[0], h[1] = int(h[0]), int(h[1])
    cH = list((cX + x, cY + y) for x in range(-2, 3)
          for y in range(-2, 3) if (cX + x in range(0, X) and cY + y in range(0, Y)) and (abs(x) + abs(y) != 3))

    if (h[0]+cX, h[1]+cY) not in cH:
        return(False, None, None, None)
    
    gamemap[cY][cX] = emp
    cX = cX + h[0]
    cY = cY + h[1]
    gamemap[cY][cX] = cat

    return(True, gamemap, cX, cY)
    
    

def stepmouse(gamemap, cX, cY, mX, mY):
    mH = list((x, y) for x in range(mX - 1, mX + 2)
          for y in range(mY - 1, mY + 2) if x in range(0, X) and y in range(0, Y) and (x,y)!=(cX,cY))

    cH = list((cX + x, cY + y) for x in range(-2, 3)
              for y in range(-2, 3) if (cX + x in range(0, X) and cY + y in range(0, Y)) and (abs(x) + abs(y) != 3))

    safe_mH = list(x for x in mH if x not in cH)

    if len(safe_mH) > 0:
        h = choice(safe_mH)
    else:
        h = choice(mH)

    gamemap[mY][mX] = emp
    mX = h[0]
    mY = h[1]
    gamemap[mY][mX] = mou  

    return(gamemap, mX, mY)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', PORT))
sock.listen(1)


try:
    while True:
        conn, addr = sock.accept()
        print('connected:', addr)    

        thr = Thread(target=game, args=(conn,))
        thr.start()
except:
    conn.close()    

