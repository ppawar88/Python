import threading as th

lock = th.Lock()

def add(a,b):
    print(a+b)

def add(a,b,c):
    print(a+b+c)

add(5,5,5)
add(5,5,5)

