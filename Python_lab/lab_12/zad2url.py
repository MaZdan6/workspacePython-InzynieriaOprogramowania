from urllib.request import urlopen
from concurrent . futures import ThreadPoolExecutor
import time

suma = []

def pobierz(url):
    with urlopen(url, timeout=1.5) as strumien:
        s = str(strumien.read())
        suma.append(int(s[2:len(s)-1]))

ile = int(input())
urle = []
for i in range(ile):
    urle.append(input())



with ThreadPoolExecutor (max_workers = ile ) as e:
    for adres in urle :
        e. submit(pobierz,adres)

print(sum(suma))