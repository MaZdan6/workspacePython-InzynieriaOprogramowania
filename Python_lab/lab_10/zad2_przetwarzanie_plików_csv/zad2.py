import operator

#wprowadzanie danych
'''
delimeter = "," ;
fileName = "phoneCalls.csv";
'''

#'''
delimeter = input() ;
fileName = input();
#'''

#czytanie pliku
file = open(fileName, 'r');

#pobieranie sekund z każdego wiersza
def getSeconds( file, delimeter):
    for row in file :



        seconds = row.split(delimeter)[3];

        #pominięcie pierwszego wiersza z nazwą kolumny
        if seconds == 'Duration(seconds)':
            continue;
        yield seconds;

listOfSeconds = [];

sumOfSeconds = 0;

generatorOfSeconds = getSeconds(file, delimeter);

#dodawanie sekund do listy
for seconds in generatorOfSeconds:
    listOfSeconds.append(seconds);



#sumowanie czasu trwania rozmów
for duration in listOfSeconds:

    #print(duration);
    sumOfSeconds = sumOfSeconds +int(duration);



print(sumOfSeconds) ;



'''
,
phoneCalls.csv

'''