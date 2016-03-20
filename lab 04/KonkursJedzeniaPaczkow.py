import operator


#wprowadzenie imion
names = input()
n=names.split(" ")

#print(n)

#wprowadzenie imion w kolejnosci jedzenia poczkow
donuts = input()
d=donuts.split(" ")

#print(d)
#stworzenie slownika klucz,wartosc -> imie,liczbawystapienia imienia

records= dict({});

for name in n:
    records[name]=0
#print(records)

#sumowanie wystapien imion

for donutEater in d:
    for name in n:
        if donutEater==name:
            records[name]= records[name]+1

# output -> lista krotek (imie uczestnika, liczba zjedzonych paczków) [( ’pawel ’, 4)


output=sorted(records.items(), key=operator.itemgetter(1), reverse=True )
print(output)

