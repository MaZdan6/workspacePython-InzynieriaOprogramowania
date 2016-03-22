
#'''
amount = 6
v = [1, 2, 3]



def dynamic(v, amount):

   # solution =[[0 for x in range(len(v)+1)] for x in range(amount+1)]
    solution =[[0 for x in range(0, amount+1)]  for x in range(0, len(v)+1)]


    #if amount=0 then just return empty set to make the change
    for i in range(0, (len(v)+1)):
        solution[i][0] = 1

    #if no coins given, 0 ways to change the amount
    for i in range(0, len(v)):
        solution[0][i] = 0


    #now fill rest of the matrix.
    for i in range (1,len(v)+1):
        for j in range (1, amount+1):
            if(v[i-1] <= j):

                b= solution[i - 1][j]
                c= solution[i][j - v[i-1]]
                a = b + c
                solution[i][j]= a

                print("solution[",i ,"][" ,j ,"] ", a)
            else:
                solution[i][j] = solution[i-1][j]
                print("solution[",i ,"][" ,j ,"] ", solution[i][j])
    return solution[len(v)][amount]
    #return solution

solution = dynamic(v, amount)

print(solution)