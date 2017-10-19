Авторское решение:

Данная программа сначала отбирает все возможные ходы, потом выбирает, который из них будет ближайшим к мыши. Как только кошка подойдет на достаточное расстояние, она сбавляет скорость (теперь будет ходить как мышка), чтобы оттеснить жертву в угол. Программа укладывается в 100 ходов и 10 секунд при карте 80 X 32.


Необходимо поменять параметры в строке
> sock.connect(('localhost', 8050))


```
import socket
import time


def lenght(cX, cY, mX, mY):
    return(((mX-cX)**2 + (mY-cY)**2)**0.5)

X, Y = 80, 38

sec = list()

for i in range(1):
    t = time.time()

    sock = socket.socket()
    sock.connect(('localhost', 8050))

    for i in range(100):
        time.sleep(0.1)
        data = sock.recv(1024*8).decode('utf-8')

        if 'Flag' in data:
            print(data)
            break
        
        CatN = data.find('@')
        MouseN = data.find('&')
        cX, cY = CatN % (X+1), int(CatN/(X+1))
        mX, mY = MouseN % (X+1), int(MouseN/(X+1))

        if abs(cX - mX) < 3 and abs(cY - mY) < 3:
            cH = list((cX + x, cY + y) for x in range(-2, 3)
                      for y in range(-2, 3) if (cX + x in range(0, X) and cY + y in range(0, Y)) and (abs(x) + abs(y) != 3))

        else:
            cH = list((cX + x, cY + y) for x in range(-1, 2)
                      for y in range(-1, 2) if (cX + x in range(0, X) and cY + y in range(0, Y)))

        c = lenght(cX, cY, mX, mY)
        choice = (0, 0)

        for j in cH:
            temp = lenght(*j, mX, mY)
            if temp < c:
                c = temp
                choice = (j[0]-cX, j[1]-cY)

        sock.send(('%d,%d\n' %choice).encode('utf-8'))

    q = (time.time()-t)
    sec.append(q)

print("Sec: %f" % sec[0])
```