import  re
class Ksiazka:

    def __init__(self, tytul, autor):
        self.tytul =tytul
        self.autor= autor

class Egzemplarz:

    def __init__(self, Ksiazka, rok_wydania, wypozyczony):

        self.Ksiazka= Ksiazka
        self.rok_wydania= rok_wydania
        self.wypozyczony= wypozyczony


class Czytelnik:



    def __init__(self, nazwisko):

        self.nazwisko= nazwisko;

    def wypozycz(self, egzemplarz):

        return True;
    def oddaj(self, tytul):

        return True;

class Bibltioteka:


    #słownik ksiązek
    def __init__(self, limit_wypozyczen):
        self.limit_wypozyczen= limit_wypozyczen;

        self.listaKsiazek=[];
        self.listaEgzemplarzy=[];



    def dostepne_egz(self, tytul):

        pass

    def wypozycz(self, nazwisko, tytul):
        pass

    def oddaj(self, nazwisko, tytul):
        pass

    #zad1
    def dodaj_egzemplarz_ksiazki(self, tytul, autor, rok_wydania):

        #sprawdzenie czy w liscie ksiazek jest książka o wprowadzanym tytule i aoutorze
        nieMaKsiazkiNaLiscie= True;
        for ksiazka in self.listaKsiazek:

            if ksiazka.tytul== tytul and ksiazka.autor== autor:
                nieMaKsiazkiNaLiscie= False;
            #break;
        # jesli nie ma ksiazki o podanym tytule i autorze, to sie ja wprowadza do listy ksiazek

        if nieMaKsiazkiNaLiscie:

            nowaKsiazka= Ksiazka(tytul, autor);
            self.listaKsiazek.append(nowaKsiazka);

        #dodaje egzemplarz ksiazki do listy
        for ksiazka in self.listaKsiazek:
            if ksiazka.tytul== tytul and ksiazka.autor== autor:
                nowyEgzemplarz= Egzemplarz(ksiazka, rok_wydania, False);
                self.listaEgzemplarzy.append(nowyEgzemplarz);
                break;

        #print("len(self.listaKsiazek): ", len(self.listaKsiazek));
        #print("len(self.listaEgzemplarzy): ", len(self.listaEgzemplarzy));
        #self.wypiszListeKsiazek();


    def wypiszListeKsiazek(self):
        krotki=[]
        for ksiazka in self.listaKsiazek:

            liczbaEgzemplarzy=0;
            for egzemplarz in self.listaEgzemplarzy:
                if ksiazka.tytul==egzemplarz.Ksiazka.tytul:
                    liczbaEgzemplarzy= liczbaEgzemplarzy+1;
            krotka=(ksiazka.tytul, ksiazka.autor, liczbaEgzemplarzy);
            krotki.append(krotka)
        krotki= sorted(krotki, key=lambda x: x[0]); #sortowanie po drugim elemencie
        for krotka in krotki:
            print(krotka)

    #zad1 zwrocenie listy książek i dostępnch egzemplarzy


liczba_wprowadzanych_krotek= int(input())
biblioteka = Bibltioteka(4);
for i in range(liczba_wprowadzanych_krotek):

    krotka= eval(input());
    #print(krotka);
    biblioteka.dodaj_egzemplarz_ksiazki(krotka[0], krotka[1], krotka[2])

biblioteka.wypiszListeKsiazek()

