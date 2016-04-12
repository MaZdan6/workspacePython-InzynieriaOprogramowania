


class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul;
        self.autor = autor;






class Egzemplarz:

    '''
    def __init__(self, Ksiazka, rok_wydania, wypozyczony):
        self.Ksiazka = Ksiazka;
        self.rok_wydania = rok_wydania;
        self.wypozyczony = wypozyczony;
    '''

    def __init__(self, Ksiazka, rok_wydania, wypozyczony, dataDodania):
        self.Ksiazka = Ksiazka;
        self.rok_wydania = rok_wydania;
        self.wypozyczony = wypozyczony;
        self.dataDodania= dataDodania;

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
    def __init__(self,):

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
    def dodaj_egzemplarz_ksiazki(self, tytul, autor, rok_wydania, dataDodania):
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
                    nowyEgzemplarz = Egzemplarz(ksiazka, rok_wydania, False, dataDodania);
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

    def wypiszListeKsiazek(self):
        krotki = []
        for e in self.listaEgzemplarzy:
            krotka= (e.Ksiazka.tytul, e.Ksiazka.autor, e.rok_wydania, e.wypozyczony, e.dataDodania);
            krotki.append(krotka);
        krotki = sorted(krotki, key=lambda x: x[0]);  # sortowanie po drugim elemencie
        for krotka in krotki:
            print(krotka)

    #zwraca listeKziązek z iloscią egzemplarzy na podstawie listy Egzemplarzy
    def zwrocListeKsiazekILiczebeEgzemplarzy(self, listaEgzemplarzy):
        krotki = []
        lista= listaEgzemplarzy
        for ksiazka in self.zwrocListeKsiazek(lista):

            liczbaEgzemplarzy = 0;
            for egzemplarz in lista:
                if ksiazka.tytul == egzemplarz.Ksiazka.tytul:
                    liczbaEgzemplarzy = liczbaEgzemplarzy + 1;
            krotka = (ksiazka.tytul, ksiazka.autor, liczbaEgzemplarzy);
            krotki.append(krotka)
        krotki = sorted(krotki, key=lambda x: x[0]);  # sortowanie po drugim elemencie

        return krotki;

    #zwraca liste tytulow na podstawie listy egzemplarzy
    def zwrocListeKsiazek(self, listaEgzemplarzy):

        ksiazki=[]
        for e in listaEgzemplarzy:

            dodacDoListy=True;
            for k in ksiazki:
                if  k.tytul== e.Ksiazka.tytul:
                    dodacDoListy=False;

            if(dodacDoListy):
                ksiazki.append(e.Ksiazka);
        return  ksiazki


    #Data w postaci krotki
    def ksiazkiDodanePo(self, Data):

        data= self.zamienKrotkeNaLiczbe(Data);


        #egzemplarze dodane po dacie
        egzPo=[];

        for egz in self.listaEgzemplarzy:
            dataDodania= self.zamienKrotkeNaLiczbe(egz.dataDodania)
            if dataDodania>data:
                egzPo.append(egz);

        listaKsiazek= self.zwrocListeKsiazekILiczebeEgzemplarzy(egzPo);

        for l in listaKsiazek:
            print(l)


        #zamiana krotki na liczbę

    def zamienKrotkeNaLiczbe(self,krotka):

        rok=str(krotka[0]);
        miesiąc=str(krotka[1]);
        dzien=str(krotka[2]);
        string= rok+miesiąc+dzien;
        return  string;


            # zad1 zwrocenie listy książek i dostępnch egzemplarzy


#'''
#test
liczba_wprowadzanych_krotek = int(input());
krotkiWprowadzane=[];
for i in range(0, liczba_wprowadzanych_krotek):
    krotkiWprowadzane.append(eval(input()));

data= eval(input());


biblioteka = Bibltioteka();
for krotka in krotkiWprowadzane:

    biblioteka.dodaj_egzemplarz_ksiazki(krotka[0], krotka[1], krotka[2], krotka[3])
biblioteka.ksiazkiDodanePo(data);


'''
#liczba ksiazek do dodania (n).
5
("Chatka Puchatka", "Alan A. Milne", 2014 , (2014 , 4, 10))
("Quo Vadis", "Henryk Sienkiewicz", 2010 , (2014 , 1, 15))
("Chatka Puchatka", "Alan A. Milne", 1998 , (2013 , 12, 31))
("Pan Tadeusz", "Adam Mickiewicz", 2003 , (2012 , 1, 1))
("Quo Vadis", "Henryk Sienkiewicz", 2010 , (2014 , 1, 15))
(2013 , 12, 31)
'''