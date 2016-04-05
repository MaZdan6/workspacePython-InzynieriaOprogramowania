import csv



#tworzenie dialectu
csv.register_dialect('mojDialekt', delimiter =',', quoting =csv.QUOTE_ALL);

#plik
plik_csv = open('sample.csv', 'r');
czytaj = csv.reader(plik_csv, dialect='mojDialekt');

for i, rekord in enumerate(czytaj):
    if i == 0:
        naglowek = rekord;
    else:
        for j, pole in enumerate( rekord ):
            print(naglowek[j],':',pole );
    print('')

plik_csv.close();