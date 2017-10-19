import socket
import time
import re


for i in range(1):
    t = time.time()

    sock = socket.socket()
    sock.connect(('localhost', 8060))
    for i in range(101):
        time.sleep(0.1)
        data = sock.recv(256).decode('utf-8')
        
        if 'Flag' in data:
            print(data, end="")
            break

        print(data, end="")
        
        a = re.findall(r"(-?\d+)X\^2", data)
        a = int(a[0])
        b = re.findall(r"(-?\d+)X[^\^]", data)
        if len(b)!=0:
            b = int(b[0])
        else:
            b = 0
        c = re.findall(r"[^\^](-?\d+)=0", data)
        if len(c)!=0:
            c = int(c[0])
        else:
            c = 0

        d = b**2-4*a*c

        if d>=0:
            x1,x2 = int((-b+d**(1/2))/2/a), int((-b-d**(1/2))/2/a)
            sock.send(('%d %d\n' %(min(x1, x2),max(x1,x2))).encode('utf-8'))
            print('%d %d\n' %(min(x1, x2),max(x1,x2)))
        else:
            sock.send(('None\n').encode('utf-8'))
            print('None\n')
        

    q = (time.time()-t)

print("Sec: %f" %q)
