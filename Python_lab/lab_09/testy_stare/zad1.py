


class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul;
        self.autor = autor;


class Egzemplarz:
    def __init__(self, Ksiazka, rok_wydania, wypozyczony):
        self.Ksiazka = Ksiazka;
        self.rok_wydania = rok_wydania;
        self.wypozyczony = wypozyczony;


class Czytelnik:
    def __init__(self, nazwisko):

        self.nazwisko = nazwisko;
        self.slownikWypKsiazek = dict();

    def wypozycz(self, egzemplarz):

        try:
            # czy wypozyczono wiecej niz 3 ksiazki
            liczbaWypozyczonychKsiazek= len(self.slownikWypKsiazek);

            if liczbaWypozyczonychKsiazek < 3:
                tytulWypozyczanejKsiazki = egzemplarz.Ksiazka.tytul;

                # wypozyczono juz ksiazke o danym tytule
                if not tytulWypozyczanejKsiazki in self.slownikWypKsiazek:

                    # dodanie wypozyczonej ksiazki do listy
                    self.slownikWypKsiazek[egzemplarz.Ksiazka.tytul] = egzemplarz;
                    egzemplarz.wypozyczony = True;
                    #print("Udało się wypozyczyć ksiażke: ", egzemplarz.Ksiazka.tytul, egzemplarz.Ksiazka.autor, egzemplarz.rok_wydania, egzemplarz.wypozyczony);
                    return True;
                else:

                    # zak
                    #print("wypozyczono juz ksiazke o danym tytule: ", tytulWypozyczanejKsiazki);
                    return False;
            else:

                # zak
                #print("Wypozyczono za duzo egzemplarzy");
                #print("len(self.slownikWypKsiazek): ", len(self.slownikWypKsiazek));
                return False;
        except:
            return False;

    def oddaj(self, tytul):

        try:
            #print(self.nazwisko);
            #print("len(self.slownikWypKsiazek): ", len(self.slownikWypKsiazek));
            egzemplarzDoOddania= self.slownikWypKsiazek[tytul];
            egzemplarzDoOddania.wypozyczony= False;
            del self.slownikWypKsiazek[tytul];
            #print("len(self.slownikWypKsiazek): ", len(self.slownikWypKsiazek));

            return  True;
        except:
            return False;


class Bibltioteka:
    # słownik ksiązek
    def __init__(self, limit_wypozyczen):
        self.limit_wypozyczen = limit_wypozyczen;

        self.listaKsiazek = [];
        self.listaEgzemplarzy = [];
        self.czytelnicy = dict();

    # dostepne_egz
    def dostepne_egz(self, tytul):

        lista_dostepnych_Egzemplarzy = [];

        for egz in self.listaEgzemplarzy:

            tytulEgzemplarza = egz.Ksiazka.tytul;
            if egz.Ksiazka.tytul == tytul:
                if not egz.wypozyczony:
                    lista_dostepnych_Egzemplarzy.append(egz);

        return lista_dostepnych_Egzemplarzy;

    # wypozycz
    def wypozycz(self, nazwisko, tytul):

        # self._pobierzCzytelnika[nazwisko];
        czytelnik = self.pobierzCzytelnika(nazwisko);

        dostepneEgzemplarze = self.dostepne_egz(tytul);
        iloscEgzemplarza = len(dostepneEgzemplarze);

        # nie było juz dostepnych egzemplarzy ksiazki
        if len(dostepneEgzemplarze) > 0:
            return czytelnik.wypozycz(dostepneEgzemplarze[0]); # jesli sie uda, to zwraca true
        else:
            return False;

    def pobierzCzytelnika(self, nazwisko):

        if not nazwisko in self.czytelnicy:
            czytelnik = Czytelnik(nazwisko);
            self.czytelnicy[nazwisko] = czytelnik;

        return self.czytelnicy[nazwisko];

    # oddaj
    def oddaj(self, nazwisko, tytul):
        try:
            czytelnik= self.czytelnicy[nazwisko];

            if czytelnik.oddaj(tytul)== True:
                return True;
            else:
                return False;
        except:
            return False;

    # dodaj
    # zad1
    def dodaj_egzemplarz_ksiazki(self, tytul, autor, rok_wydania):
        try:
            # sprawdzenie czy w liscie ksiazek jest książka o wprowadzanym tytule i autorze
            nieMaKsiazkiNaLiscie = True;
            for ksiazka in self.listaKsiazek:

                if ksiazka.tytul == tytul and ksiazka.autor == autor:
                    nieMaKsiazkiNaLiscie = False;
                    # break;
            # jesli nie ma ksiazki o podanym tytule i autorze, to sie ja wprowadza do listy ksiazek

            if nieMaKsiazkiNaLiscie:
                nowaKsiazka = Ksiazka(tytul, autor);
                self.listaKsiazek.append(nowaKsiazka);

            # dodaje egzemplarz ksiazki do listy
            for ksiazka in self.listaKsiazek:
                if ksiazka.tytul == tytul and ksiazka.autor == autor:
                    nowyEgzemplarz = Egzemplarz(ksiazka, rok_wydania, False);
                    self.listaEgzemplarzy.append(nowyEgzemplarz);
                    return True;
                    break;

                    # print("len(self.listaKsiazek): ", len(self.listaKsiazek));
                    # print("len(self.listaEgzemplarzy): ", len(self.listaEgzemplarzy));
                    # self.wypiszListeKsiazek();
        except:
            False;


    def wypiszListeKsiazek(self):
        krotki = []
        for ksiazka in self.listaKsiazek:

            liczbaEgzemplarzy = 0;
            for egzemplarz in self.listaEgzemplarzy:
                if ksiazka.tytul == egzemplarz.Ksiazka.tytul:
                    liczbaEgzemplarzy = liczbaEgzemplarzy + 1;
            krotka = (ksiazka.tytul, ksiazka.autor, liczbaEgzemplarzy);
            krotki.append(krotka)
        krotki = sorted(krotki, key=lambda x: x[0]);  # sortowanie po drugim elemencie
        for krotka in krotki:
            print(krotka)

            # zad1 zwrocenie listy książek i dostępnch egzemplarzy


'''
#test
liczba_wprowadzanych_krotek = int(input());
krotkiWprowadzane=[];
for i in range(0, liczba_wprowadzanych_krotek):
    krotkiWprowadzane.append(eval(input()));




listaDanychWyjsciowych=[];

biblioteka = Bibltioteka(3);
for krotka in krotkiWprowadzane:

    # Wywolywanie odpowiednich funkcji
    if krotka[0] == 'dodaj':
        #print("dodaj");
        output =biblioteka.dodaj_egzemplarz_ksiazki(krotka[1], krotka[2], krotka[3])

        listaDanychWyjsciowych.append(output);

    elif krotka[0] == 'wypozycz':
        #print("wypozycz");
        nazwisko = krotka[1];
        tytul = krotka[2];

        output = biblioteka.wypozycz(nazwisko, tytul);
        listaDanychWyjsciowych.append(output);
        #print(output);


    elif krotka[0] == 'oddaj':

        nazwisko = krotka[1];
        tytul = krotka[2];
        output = biblioteka.oddaj(nazwisko, tytul);
        listaDanychWyjsciowych.append(output);
        #print("oddaj");

for output in listaDanychWyjsciowych:
    print(output);

'''