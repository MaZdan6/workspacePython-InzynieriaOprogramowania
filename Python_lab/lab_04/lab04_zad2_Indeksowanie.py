
#liczba dokumentow
n= int(input())
print('n= ', n)
#wprowadzanie dokumentów

documents = []

for i in range (0, n):
    documents.append(input())


    #print
    '''
for i in range (0, m):
    print(documents[i])'''

#liczba zapytan do przetworzenia (m)
m= int(input())
print('m= ', m)
#m linijek z jednowyrazowymi zapytaniami
words=[]

for i in range(0, m):
    words.append(input())
#wypisanie wyrazów
for i in range(0, m):
    print(words[i])


#funkcja zwracająca słownik (klucz, wartość)= indeks dokumentu, ilość wystąpień danego wyrazu
#input - zapytanie, lista dokumentów

def countWords(word, dokuments):

    #print("Word", word)
    #print("Documents=", documents)

    indexAndNumberOfWord= dict({})

    for document in documents:

        index= documents.index(document)
        numberOfWord=0
        wordsOfDocuments= documents[i].split()
        print("wordsOfDocuments= ", wordsOfDocuments)



    return 0

print(countWords(words[0],documents))

#funkcja zwracająca posortowaną listę dla danego zapytania

#funkcja zwracają listę posortowanych list dokumentów dla zapytań