

#print("")
#print("Wprowadz wyraz wzorcowy")
pattern = input()
#print(pattern)

#posortowany wyraz wzorcowy
patternSortedList=sorted(pattern)
patternSorted = str("".join(patternSortedList))

#print( patternSorted)

#lista z danymi
anagramList=[]

#dodawanie wyrazów do listy
for i in range (0,5):

    #print("Wprowadz "+str(i+1)+" wyraz do listy")


    #wprowadzanie wyrazu
    word = input()
    #print(word)
    #sortowanie wyrazu
    wordSorted= str("".join(sorted(word)))
    #print("Posortowany wyraz: ",wordSorted)

    #dodawanie wyrazu jesli jego posortwania wersja jest rowna posortowanemu wzorcowi
    if patternSorted == wordSorted:
        anagramList.append(word)
    #print(anagramList)


#sortowanie listy
anagramListSorted= sorted(anagramList)
print(str(anagramListSorted))