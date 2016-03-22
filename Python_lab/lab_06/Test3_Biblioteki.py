
from lab06_zad2 import Bibltioteka;



#liczba_wprowadzanych_krotek = int(input())

#test
liczba_wprowadzanych_krotek = input();
krotkiWprowadzane=[];
for i in range(0,12):
    krotkiWprowadzane.append(eval(input()));



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