__author__ = '23901'


#Oblicz, na ile sposobów mozna rozmienic okreslona kwote pieniedzy,
#majac do dyspozycji okreslone nominały.

#input


amount = int(input ())
#print("Ammount= ", amount)


denominations = input ()
d=denominations.split(" ")

# zamiana listy z stringami na liste z int
v = [int(i) for i in d]

def dynamic(v, amount):


    solution =[[0 for x in range(0, amount+1)]  for x in range(0, len(v)+1)]



    for i in range(0, (len(v)+1)):
        solution[i][0] = 1


    for i in range(0, len(v)):
        solution[0][i] = 0



    for i in range (1,len(v)+1):
        for j in range (1, amount+1):
            if(v[i-1] <= j):

                b= solution[i - 1][j]
                c= solution[i][j - v[i-1]]
                a = b + c
                solution[i][j]= a

                #print("solution[",i ,"][" ,j ,"] ", a)
            else:
                solution[i][j] = solution[i-1][j]
                #print("solution[",i ,"][" ,j ,"] ", solution[i][j])
    return solution[len(v)][amount]


solution = dynamic(v, amount)

print(solution)