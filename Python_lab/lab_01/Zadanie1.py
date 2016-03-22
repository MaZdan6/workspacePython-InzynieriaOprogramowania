__author__ = '23901'


# liczba wprowadzonych wyrazow
numberOfString=0
###liczba wyrazów zaczynających się z wielkiej Litery
upper=0

while numberOfString<5:
    string=input()
    if(string[0].isupper()):
        upper=upper+1
    numberOfString= numberOfString+1

print(upper)
###Podaj imię: (imie)
#print ( " Jak masz na imie ? " )
#imie = input ()