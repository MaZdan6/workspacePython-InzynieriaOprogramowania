__author__ = '23901'



def a ( n ):
    if n == 0:
        return 10
    else :
        return 7 + a ( n - 1)



def sumaCiagu(n):

    suma =0
    wyraz = 0
    print("n= ", n)

    for i in range(0,n):
        wyraz= a(i)
        suma= suma+ a(i)

        print(i)
        print("Wyraz: ", wyraz)
        print("suma: ", suma)
        print(" ")
    return None

sumaCiagu(14)

def sumaCiagu2(n):

    suma =0
    wyraz1 = a(0)
    wyraz1 = a(n)

    suma= (a(0)+a(n-1))/2*n

    print("n: ", n)
    print("Suma: ", suma)



sumaCiagu2(14)
#ciag= a(0)
#print("a(1)", a(1))