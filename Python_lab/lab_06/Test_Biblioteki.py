from lab06_zad2 import Bibltioteka;



#liczba_wprowadzanych_krotek = int(input())

#krotki dodaj
dodaj=[];
dodaj.append((" dodaj ", "Pan Tadeusz ", " Adam Mickiewicz ", 2000) );
dodaj.append((" dodaj ", "Quo Vadis ", " Henryk Sienkiewicz ", 2010) );
dodaj.append((" dodaj ", " Chatka Puchatka ", " Alan Alexander Milne ", 1998));
dodaj.append((" dodaj ", "Pan Tadeusz ", " Adam Mickiewicz ", 2000) );
dodaj.append((" dodaj ", " Chatka Puchatka ", " Alan Alexander Milne ", 1998));
# tworzenie obiektów
biblioteka = Bibltioteka(3);

#Test metody bibliotek.dodaj_egzemplarz_ksiazki()
print("-------------------------------------------------");
print("Test metody biblioteka.dodaj_egzemplarz_ksiazki()");
print("-------------------------------------------------");
for krotki in dodaj:
    biblioteka.dodaj_egzemplarz_ksiazki(krotki[1], krotki[2], krotki[3]);

for egzemplarz in biblioteka.listaEgzemplarzy:
    print(egzemplarz.Ksiazka.tytul, egzemplarz.Ksiazka.autor, egzemplarz.rok_wydania, egzemplarz.wypozyczony);


print("-------------------------------------------------");
print("Test metody biblioteka.dostepne_egzemplarze(' Chatka Puchatka ')");
print("-------------------------------------------------");

dostepneEgzemplarze= biblioteka.dostepne_egz(" Chatka Puchatka ");

for egzemplarz in dostepneEgzemplarze:
    print(egzemplarz.Ksiazka.tytul, egzemplarz.Ksiazka.autor, egzemplarz.rok_wydania, egzemplarz.wypozyczony);

#wprowadzanie krotek wywołujących metode wypozycz
krotkiWyp=[];
krotkiWyp.append((" wypozycz ", " Bartek Perkowski ", "Pan Tadeusz "));
krotkiWyp.append((" wypozycz ", " Bartek Perkowski ", "Pan Tadeusz "));
krotkiWyp.append((" wypozycz ", " Jacek Malyszko ", "Quo Vadis "));
krotkiWyp.append((" wypozycz ", " Bartek Perkowski ", "Quo Vadis "));

print("-------------------------------------------------");
print("Test metody biblioteka.pobierzCzytelnika(self, nazwisko)");
print("-------------------------------------------------");

for krotkaWyp in krotkiWyp:
    biblioteka.pobierzCzytelnika(krotkaWyp[1]);
for czytelnik in biblioteka.czytelnicy:
    print(biblioteka.czytelnicy[czytelnik].nazwisko);




#'''
print("-------------------------------------------------");
print("Test metody biblioteka.wypozycz('Jakub Dzikowski', ' Chatka Puchatka ')");
print("-------------------------------------------------");

for krotkaWyp in krotkiWyp:
    print(biblioteka.wypozycz(krotkaWyp[1], krotkaWyp[2]));

#'''



print("-------------------------------------------------");
print("Test metody biblioteka.oddaj(' Jacek Malyszko ', 'Quo Vadis ')");
print("-------------------------------------------------");

krotkiOdd=[]
krotkiOdd.append((" oddaj ", " Jacek Malyszko ", "Quo Vadis "));
krotkiOdd.append((" oddaj ", " Bartek Perkowski ", "Pan Tadeusz "));
krotkiOdd.append((" oddaj ", " Bartek Perkowski ", "Pan Tadeusz "));



for krotkaOdd in krotkiOdd:

    #wywołanie metody oddaj
    print(biblioteka.oddaj(krotkaOdd[1], krotkaOdd[2]));
'''
    #wypisanie dostępnych egzemplarzy po oddaniu ksiazki
    dostepneEgzemplarze= biblioteka.dostepne_egz(krotkaOdd[2]);
    for egzemplarz in dostepneEgzemplarze:
        print(egzemplarz.Ksiazka.tytul, egzemplarz.Ksiazka.autor, egzemplarz.rok_wydania, egzemplarz.wypozyczony);
'''





'''
biblioteka = lab06_zad2.Bibltioteka(3);
for i in range(liczba_wprowadzanych_krotek):

    krotka = eval(input());
    # print(krotka[0]);
    # print(krotka);
    # biblioteka.dodaj_egzemplarz_ksiazki(krotka[0], krotka[1], krotka[2])

    # Wywolywanie odpowiednich funkcji
    if krotka[0] == ' dodaj ':
        print("dodaj");
        biblioteka.dodaj_egzemplarz_ksiazki(krotka[1], krotka[2], krotka[3])


    elif krotka[0] == ' wypozycz ':
        print("wypozycz");
        nazwisko = krotka[1];
        tytul = krotka[2];

        output = biblioteka.wypozycz(nazwisko, tytul);

        print(output);


    elif krotka[0] == ' oddaj ':
        print("oddaj");
# biblioteka.wypiszListeKsiazek()

# test Biblioteka.dostepne_egz
'''
'''
lista= biblioteka.dostepne_egz('Pan Tadeusz ');

for egz in lista:
    print(egz.Ksiazka.tytul, egz.Ksiazka.autor, egz.rok_wydania, egz.wypozyczony);
'''


