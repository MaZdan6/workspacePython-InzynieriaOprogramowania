
from lab06_zad2 import Bibltioteka;



#liczba_wprowadzanych_krotek = int(input())

#test
liczba_wprowadzanych_krotek = 12;
krotkiWprowadzane=[];
krotkiWprowadzane.append((" dodaj ", "Pan Tadeusz ", " Adam Mickiewicz ", 2000) );
krotkiWprowadzane.append((" dodaj ", "Quo Vadis ", " Henryk Sienkiewicz ", 2010));
krotkiWprowadzane.append((" dodaj ", " Chatka Puchatka ", " Alan Alexander Milne ", 1998));
krotkiWprowadzane.append((" dodaj ", "Pan Tadeusz ", " Adam Mickiewicz ", 2000) );
krotkiWprowadzane.append((" dodaj ", " Chatka Puchatka ", " Alan Alexander Milne ", 2014));
krotkiWprowadzane.append((" wypozycz ", " Bartek Perkowski ", "Pan Tadeusz "));
krotkiWprowadzane.append((" wypozycz ", " Bartek Perkowski ", "Pan Tadeusz "));
krotkiWprowadzane.append((" wypozycz ", " Jacek Malyszko ", "Quo Vadis "));
krotkiWprowadzane.append((" wypozycz ", " Bartek Perkowski ", "Quo Vadis "));
krotkiWprowadzane.append((" oddaj ", " Jacek Malyszko ", "Quo Vadis "));
krotkiWprowadzane.append((" wypozycz ", " Bartek Perkowski ", "Quo Vadis "));
krotkiWprowadzane.append((" oddaj ", " Jacek Malyszko ", "Quo Vadis "));

listaDanychWyjsciowych=[];

biblioteka = Bibltioteka(3);
for krotka in krotkiWprowadzane:

    # Wywolywanie odpowiednich funkcji
    if krotka[0] == ' dodaj ':
        #print("dodaj");
        output =biblioteka.dodaj_egzemplarz_ksiazki(krotka[1], krotka[2], krotka[3])

        listaDanychWyjsciowych.append(output);

    elif krotka[0] == ' wypozycz ':
        #print("wypozycz");
        nazwisko = krotka[1];
        tytul = krotka[2];

        output = biblioteka.wypozycz(nazwisko, tytul);
        listaDanychWyjsciowych.append(output);
        #print(output);


    elif krotka[0] == ' oddaj ':

        nazwisko = krotka[1];
        tytul = krotka[2];
        output = biblioteka.oddaj(nazwisko, tytul);
        listaDanychWyjsciowych.append(output);
        #print("oddaj");

for output in listaDanychWyjsciowych:
    print(output);