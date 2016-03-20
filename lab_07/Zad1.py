class Drzewo:
    """Klasa reprezentująca drzewo, po którym będziemy wyszukiwać odległości pomiędzy wierzchołkami. W konstruktorze przyjmuje listę krotek reprezentujących połączenia.
    """
    def __init__(self, lista_krotek: "tutaj chcemy mieć listę krotek, reprezentujących połączenia pomiędzy wierzchołkami"):
        """Konstruktor powinien zapisywać nadesłaną listę krotek jako atrybut obiektu i dodatkowo instancjonowac i przechowywac dwa obiekty odpowiedzialne za różne podejscia do obliczania odległosci (klasy MiaraProsta, MiaraPotegowa)

        """
        self.lista_krotek = lista_krotek


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
        pass

class MiaraProsta:
    def licz_odleglosc(self, nadwezly1:list, nadwezly2:list) -> int:
        """Funkcja zwraca odległość pomiędzy węzłami liczoną jako ilość przeskoków pomiedzy nimi. Otrzymuje jako wejście dwie listy, przechowujące nadwęzły obu analizowanych wierzchołków (wynik funkcji Drzewo.pobierz_nadkoncepty). W tych listach chcemy znaleźć najniższy wspólny nadwęzeł, a następnie określamy na której pozycji ten węzeł jest w obu listach. Przykładowo, w listach ['A', 'B', 'C', 'D'] ['E', 'F', 'G', 'C', 'D'] najniższy wspólny współwierzchołek to C i od pierwszego wierzchołka jest oddalony o 3 przeskoki, a od drugiego o 4 przeskoki. W takim przypadku odległość powinna wynosić 2 + 3 = 5. Przykład poniżej NIE ODPOWIADA przykładowi z prezentacji (jest to inne drzewo).

        nadwezly1, nadwezly2 - listy, w których przechowywane są nadwęzły wierzchołków, dla których chcemy ustalić odległość
        >>> miara = MiaraProsta()
        >>> miara.licz_odleglosc(['A', 'B', 'C'], ['D', 'E', 'B', 'C'])
        3
        """
        pass

class MiaraPotegowa:
    def licz_odleglosc(self, nadwezly1:list, nadwezly2:list) -> int:
        """Funkcja zwraca odległość pomiędzy węzłami liczoną w taki sposób, że każdy kolejny przeskok w górę prowadzący do najbliższego wspólnego nadwierzchołka jest liczony jako kolejna potęga dwójki. Przykładowo, w listach ['T', 'A', 'B', 'C', 'D'] ['U', 'E', 'F', 'G', 'C', 'D'] najniższy wspólny współwierzchołek to C i od pierwszego wierzchołka jest oddalony o 3 przeskoki, a od drugiego o 4 przeskoki. W takim przypadku wynik wynosi (1 + 2 + 4) + (1 + 2 + 4 + 8) = 22. Przykład poniżej NIE ODPOWIADA przykładowi z prezentacji (jest to inne drzewo).

        nadwezly1, nadwezly2 - listy, w których przechowywane są nadwęzły wierzchołków, dla których chcemy ustalić odległość
        >>> miara = MiaraPotegowa()
        >>> miara.licz_odleglosc(['L', 'A', 'B', 'C'], ['M', 'D', 'E', 'B', 'C'])
        10
        """
        pass




drzewo_input = eval(input());
drzewo = Drzewo(drzewo_input);
zapytania = eval(input());
for z in zapytania:
    print(drzewo.pobierz_nadkoncepty(z));

'''
przykładowe wjejscie dla zad 1
[( 'F', 'B'), ('B', 'A'), ('B', 'D'), ('D', 'C'), ('D', 'E'), ('F', 'G'), ('G', 'I'), ('I', 'H')]
['B', 'F', 'C']

wyjscie:
[’C’, ’D’, ’B’, ’F’]
'''

