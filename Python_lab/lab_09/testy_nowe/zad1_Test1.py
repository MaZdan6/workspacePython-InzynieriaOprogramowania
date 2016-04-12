


from lab_09.zad1 import Bibltioteka;













#liczba_wprowadzanych_krotek = int(input())

#test
#liczba ksiazek do dodania (n).
liczba_wprowadzanych_krotek = 5;

#W kolejnych n linijkach podane egzemplarze ksiazki.
krotkiWprowadzane=[];
krotkiWprowadzane.append(("Chatka Puchatka", "Alan A. Milne", 2014 , (2014 , 4, 10)));
krotkiWprowadzane.append(("Quo Vadis", "Henryk Sienkiewicz", 2010 , (2014 , 1, 15)));
krotkiWprowadzane.append(("Chatka Puchatka", "Alan A. Milne", 1998 , (2013 , 12, 31)));
krotkiWprowadzane.append(("Pan Tadeusz", "Adam Mickiewicz", 2003 , (2012 , 1, 1)));
krotkiWprowadzane.append(("Quo Vadis", "Henryk Sienkiewicz", 2010 , (2014 , 1, 15)));
#data (jako krotka).
data=(2013 , 12, 31);

listaDanychWyjsciowych=[];

biblioteka = Bibltioteka();


# Test dodawania książek
for krotka in krotkiWprowadzane:
    biblioteka.dodaj_egzemplarz_ksiazki(krotka[0], krotka[1], krotka[2], krotka[3])

#biblioteka.wypiszListeKsiazek()
#biblioteka.wypiszListeEgzemplarzy();

biblioteka.ksiazkiDodanePo(data);







