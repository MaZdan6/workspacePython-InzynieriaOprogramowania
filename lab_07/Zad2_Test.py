
from Zad2 import Drzewo;
from Zad2 import MiaraProsta;
from Zad2 import MiaraPotegowa;









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