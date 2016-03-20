class Drzewo:
    """Klasa reprezentująca drzewo, po którym będziemy wyszukiwać odległości pomiędzy wierzchołkami. W konstruktorze przyjmuje listę krotek reprezentujących połączenia.
    """
    def __init__(self, lista_krotek: "tutaj chcemy mieć listę krotek, reprezentujących połączenia pomiędzy wierzchołkami"):
        """Konstruktor powinien zapisywać nadesłaną listę krotek jako atrybut obiektu i dodatkowo instancjonowac i przechowywac dwa obiekty odpowiedzialne za różne podejscia do obliczania odległosci (klasy MiaraProsta, MiaraPotegowa)

        """
        self.lista_krotek = lista_krotek
        self.miaraProsta= MiaraProsta();
        self.miaraPotegowa= MiaraPotegowa();


    #zwraca listę wezlow od wiechrzcholka do korzenia
    def pobierz_nadkoncepty(self, wierzcholek: str) -> list:
        lista_wyn = []
        lista_wyn.append(wierzcholek)
        szukamy_dla = wierzcholek
        while True:
            czy_znalazlem = False
            for i in self.lista_krotek:
                if i[1] == szukamy_dla:
                    lista_wyn.append(i[0])
                    szukamy_dla = i[0]
                    czy_znalazlem=True
                    break
            if czy_znalazlem==False:
                break
        return lista_wyn





    def oblicz_odleglosc(self, wierzcholek1:str, wierzcholek2:str, miara:str) -> int:
        """
        Oblicza odległość pomiędzy wierzchołkami zgodnie z zadaną miarą. Jeśli miara ma wartość "prosta", odległość ma być liczona z wykorzystaniem obiektu klasy MiaraProsta, jesli "potegowa" to za pomocą obiektu klasy MiaraPotegowa
        """



        wezel1= wierzcholek1
        wezel2= wierzcholek2;

        if miara == "prosta ":
                # print(miara,wezel1,wezel2);
                nadwezly11= self.pobierz_nadkoncepty(wezel1);
                nadwezly22= self.pobierz_nadkoncepty(wezel2);

                odleglosc= self.miaraProsta.licz_odleglosc(nadwezly11, nadwezly2= nadwezly22);
                return  odleglosc;

        elif miara== "potegowa ":
            #print(miara, wezel1, wezel2);

            nadwezly1= self.pobierz_nadkoncepty(wezel1);
            nadwezly2= self.pobierz_nadkoncepty(wezel2);

            odleglosc= self.miaraPotegowa.licz_odleglosc(nadwezly1, nadwezly2);
            return  odleglosc;














class MiaraProsta:
    def licz_odleglosc(self, nadwezly1:list, nadwezly2:list) -> int:
        """Funkcja zwraca odległość pomiędzy węzłami liczoną jako ilość przeskoków pomiedzy nimi. Otrzymuje jako wejście dwie listy, przechowujące nadwęzły obu analizowanych wierzchołków (wynik funkcji Drzewo.pobierz_nadkoncepty). W tych listach chcemy znaleźć najniższy wspólny nadwęzeł, a następnie określamy na której pozycji ten węzeł jest w obu listach. Przykładowo, w listach ['A', 'B', 'C', 'D'] ['E', 'F', 'G', 'C', 'D'] najniższy wspólny współwierzchołek to C i od pierwszego wierzchołka jest oddalony o 3 przeskoki, a od drugiego o 4 przeskoki. W takim przypadku odległość powinna wynosić 2 + 3 = 5. Przykład poniżej NIE ODPOWIADA przykładowi z prezentacji (jest to inne drzewo).

        """

        #znajdz najbliższy wspólny nadwęzeł z dwóch list
        nwn= 'nie znaleziono najbliższego wpolnego nadwezła';
        znaleziono_nwn= False;
        for nadwezel1 in nadwezly1:

            if znaleziono_nwn:
                break;

            for nadwezel2 in nadwezly2:
                if nadwezel1== nadwezel2:
                    nwn= nadwezel1;
                    znaleziono_nwn= True;
                    break;

        #zwroc liczbe wezlow od wezla do nwn dla wezla poczatkowego i koncowego
        l1= nadwezly1.index(nwn);
        l2= nadwezly2.index(nwn)

        return  l1+l2;

class MiaraPotegowa:
    def licz_odleglosc(self, nadwezly1:list, nadwezly2:list) -> int:
        """Funkcja zwraca odległość pomiędzy węzłami liczoną w taki sposób, że każdy kolejny przeskok w górę prowadzący do najbliższego wspólnego nadwierzchołka jest liczony jako kolejna potęga dwójki. Przykładowo, w listach ['T', 'A', 'B', 'C', 'D'] ['U', 'E', 'F', 'G', 'C', 'D'] najniższy wspólny współwierzchołek to C i od pierwszego wierzchołka jest oddalony o 3 przeskoki, a od drugiego o 4 przeskoki. W takim przypadku wynik wynosi (1 + 2 + 4) + (1 + 2 + 4 + 8) = 22. Przykład poniżej NIE ODPOWIADA przykładowi z prezentacji (jest to inne drzewo).

        """

        #znajdz najbliższy wspólny nadwęzeł z dwóch list
        nwn= 'nie znaleziono najbliższego wpolnego nadwezła';
        znaleziono_nwn= False;
        for nadwezel1 in nadwezly1:

            if znaleziono_nwn:
                break;

            for nadwezel2 in nadwezly2:
                if nadwezel1== nadwezel2:
                    nwn= nadwezel1;
                    znaleziono_nwn= True;
                    break;

        #zwroc liczbe wezlow od wezla do nwn dla wezla poczatkowego i koncowego
        l1= nadwezly1.index(nwn);
        l2= nadwezly2.index(nwn)

        #zwroc sumy poteg
        p1=0;
        p2=0;

        for i in range(0,l1):
            potega= 2**i
            p1=p1+potega;

        for i in range(0,l2):
            potega= 2**i
            p2=p2+potega;

        return p1+p2;










#wprowadzanie ręczne
drzewo_input= eval(input());


#drzewo_input = [( 'F', 'B'), ('B', 'A'), ('B', 'D'), ('D', 'C'), ('D', 'E'), ('F', 'G'), ('G', 'I'), ('I', 'H')];

drzewo = Drzewo(drzewo_input);


#wprowadzanie ręczne
zapytania = eval(input());


#zapytania = [( 'prosta ', 'C', 'G'), ('prosta ', 'G', 'C'), ('potegowa ', 'G', 'C')];
outputLista=[];

for zapytanie in zapytania:

    miara= zapytanie[0];
    wierzcholek1=  zapytanie[1];
    wierzcholek2= zapytanie[2];



    odleglosc= drzewo.oblicz_odleglosc(wierzcholek1, wierzcholek2, miara);
    outputLista.append(odleglosc);

print(outputLista);



'''
przykładowe wejscie dla zad 2
[( 'F', 'B'), ('B', 'A'), ('B', 'D'), ('D', 'C'), ('D', 'E'), ('F', 'G'), ('G', 'I'), ('I', 'H')]
[( 'prosta ', 'C', 'G'), ('prosta ', 'G', 'C'), ('potegowa ', 'G', 'C')]

wyjscie:
[4, 4, 8]
'''