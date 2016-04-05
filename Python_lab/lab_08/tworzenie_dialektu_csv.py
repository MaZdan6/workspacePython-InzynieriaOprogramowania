import csv


csv.register_dialect ('mojDialekt ', delimiter =',', quoting =csv.QUOTE_ALL);

plik_csv = open ('output .csv ', 'w')
zapisz = csv . writer(plik_csv, dialect= 'mojDialekt ');

dane = [
('Imie ','Nazwisko ','Firma ','Stanowisko '),
('Bartek ','Perkowski ','UEP ','Informatyk ')
]

for element in dane:
    zapisz . writerow(element);

plik_csv . close();