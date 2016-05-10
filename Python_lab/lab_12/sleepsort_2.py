from concurrent . futures import ThreadPoolExecutor
import time

def wyswietl (x):
    time . sleep (x)
    print (x)

liczby = [ int (x) for x in input (). split ()]

with ThreadPoolExecutor ( max_workers = len ( liczby )) as e:
    for x in liczby :
        e. submit ( wyswietl , x)