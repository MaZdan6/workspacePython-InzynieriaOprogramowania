import threading
import time

def wyswietl (x):
    time.sleep (x)
    print(x)

liczby = [int(x) for x in input(). split ()]

for x in liczby :
    t = threading . Thread(target=wyswietl, args=[x])
    t. start()

#input- 3 2 6 4 1 8