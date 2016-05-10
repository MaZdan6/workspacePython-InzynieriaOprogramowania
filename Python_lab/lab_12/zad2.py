
from urllib.request import  urlopen
import time
from concurrent.futures import ThreadPoolExecutor


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

numbers = []
def pobierz(url):
    with urlopen(url, timeout=1.5) as strumien:

        #wczytanie stringa z url'a
        s = str(strumien.read())
        #zamiana stringa na listy
        number= int(s[2:len(s)-1])

        #dodanie wczytanej liczby do listy
        numbers.append(number);


#liczba linijek
ile = int(input())
urle=[]
for i in range(ile):
    urle.append(input())

with ThreadPoolExecutor(max_workers=ile) as e:
    for adres in urle:
        e.submit(pobierz, adres)

print(sum(numbers))

