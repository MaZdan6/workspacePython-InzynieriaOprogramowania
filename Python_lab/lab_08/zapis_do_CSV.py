import csv

plik_csv = open ('output .csv ', 'w', encoding ='utf -8 ')
zapisz = csv.writer( plik_csv , dialect ='unix')

dane = [
('Imie ','Nazwisko ','Firma ','Stanowisko '), 
('Bartek ','Perkowski ','UEP ','Informatyk '),
('Jan ','Nowak ','ABC ','Sprzedawca '), 
('Jakub ','Dzikowski ','UEP ',' Administrator '), 
('Jacek ','Malyszko ','UEP ',' Administrator '), 
('Marek ','Kowalski ','ABC ','Informatyk ') 
]

for element in dane :
    zapisz.writerow ( element )

plik_csv . close ()