class Konto:

    def __init__(self, numer, roczna_stopa): # kwota ma już przypisaną wartosc dlatego jej nie definiujemy, roczna stopa jest wiadoma
        self.numer = numer
        self.kwota = 0.0
        self.roczna_stopa = roczna_stopa

    def nastepny_miesiac(self):
        pass

    def wplac(self, kwota):
        if((kwota < 0.0) and (self.kwota < - kwota)):
            raise ValueError('Niewystarczajace saldo na koncie')
        self.kwota = round(self.kwota + kwota, 2)




class KontoKapDzienna(Konto):

    def __init__(self):
        pass

    def nastepny_miesiac(self): # 30 razy dokonujemy kapitalizacji dziennej
        for i in range(30):
            self.kwota = round(self.kwota * ( 1 + self.roczna_stopa / 360.0), 2)




class KontoKapMiesieczna(Konto):

    def __init__(self):
        pass

    def nastepny_miesiac(self):
        self.kwota = round(self.kwota * ( 1 + self.roczna_stopa / 12.0), 2) #rouynd zaokrągla do 2 miejsc po przecinku

class Bank():
    __numer = 1

    def __init__(self):
        self.konta = dict()

    def __pobierz_konto(self, nr_konta):
        return self.konta[nr_konta]

    def zaloz_konto(self, roczna_stopa = 0.036, kapitalizacja = 'miesieczna'):
        numer = Bank.__numer
        Bank.__numer += 1 # numeracja zwiększona o 1 w momencie zakładania kolejnego konta
        if(kapitalizacja == 'miesieczna'):
            self.konta[numer] = KontoKapMiesieczna(numer, roczna_stopa)
        else:
            self.konta[numer] = KontoKapDzienna(numer, roczna_stopa)
        return numer

    def wplac(self, nr_konta, kwota):
        try:
            self.__pobierz_konto(nr_konta).wplac(kwota)
        except e as ValueError:
            print(e)

    def nastepny_miesiac(self):
        for konto in self.konta:
            konto.nastepny_miesiac

    def przelej(self, nr_konta_nad, nr_konta_odb, kwota):
        try:
            __pobierz_konto(nr_konta.nad).wplac(-kwota)
            __pobierz_konto(nr_konta.odb).wplac(kwota)
        except e as ValueError:
            print(e)