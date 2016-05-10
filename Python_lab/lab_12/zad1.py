from concurrent.futures import ThreadPoolExecutor
from urllib.request import  urlopen
import time



def pobierz(url):
    with urlopen(url, timeout=1.5) as strumien:
        strumien.read()
    print(url)

#liczba linijek
ile = int(input())
urle = []
for i in range(ile):
    urle.append(input())

with ThreadPoolExecutor(max_workers=ile) as e:
    for adres in urle:
        e.submit(pobierz, adres)


'''
8
http://150.254.36.78/inzynieria/a
http://150.254.36.78/inzynieria/b
http://150.254.36.78/inzynieria/c
http://150.254.36.78/inzynieria/d
http://150.254.36.78/inzynieria/e
http://150.254.36.78/inzynieria/f
http://150.254.36.78/inzynieria/g
http://150.254.36.78/inzynieria/h
'''