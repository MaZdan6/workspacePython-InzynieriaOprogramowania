from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import time

def wyswietl(x):
    time . sleep(x)
    return x

liczby = [int(x) for x in input(). split()]

with ThreadPoolExecutor(max_workers=len(liczby)) as e:
    futures = {e. submit(wyswietl, x) for x in liczby}
    suma= 0
for f in as_completed(futures):
    print(f. result())
    suma += f. result()
    print(suma)

#3 2 6 4 1 8