
from Python_lab.lab_09.zad1 import Bibltioteka

''''
#input
numberOfBooks=5;
listOfBooks=[];
tuple0=("Chatka Puchatka" , "Alan A . Milne" , 2014 , (2014 , 4, 10));
tuple1=("Quo Vadis" , "Henryk Sienkiewicz" , 2010 , (2014 , 1 , 15));
tuple2=("Chatka Puchatka" , "Alan A . Milne" , 1998 , (2013 , 12 , 31));
tuple3=("Pan Tadeusz" , "Adam Mickiewicz" , 2003 , (2012 , 1, 1));
tuple4=("Quo Vadis" , "Henryk Sienkiewicz" , 2010 , (2014 , 1 , 15));

listOfBooks.append(tuple0);
listOfBooks.append(tuple1);
listOfBooks.append(tuple2);
listOfBooks.append(tuple3);
listOfBooks.append(tuple4);
dateTuple=(2013 , 12 , 31);



biblioteka = Bibltioteka(3);
listaDanychWyjsciowych=[];
for krotka in listOfBooks:

    # Wywolywanie odpowiednich funkcji

    output =biblioteka.dodaj_egzemplarz_ksiazki(krotka[0], krotka[1], krotka[2],krotka[3])
    listaDanychWyjsciowych.append(output);



for output in listaDanychWyjsciowych:
    print(output);
'''

'''
#Wypisanie danych wejściowych do konsoli
print("numberOfBooks: ", numberOfBooks);
#print(book);

for book in  listOfBooks:
    print(book);

print("dateTuple: ", dateTuple)
'''



#Test