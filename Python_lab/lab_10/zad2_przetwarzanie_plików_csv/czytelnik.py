import operator
delimeter=input()
wejscie=input()
plik = open(wejscie, 'r')
def csv(plik,delimeter):
    for i in plik:
        wiersz = i.split(delimeter)[3]
        yield wiersz

wynik=[]
suma=0
zadanie=csv(plik,delimeter)
for j in zadanie:
    wynik.append(j)
for k in(wynik[1:]):
    suma+=int(k)
print(suma)



'''
,
phoneCalls.csv

'''