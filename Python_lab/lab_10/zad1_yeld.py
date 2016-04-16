

def my_range(start,end):

    while start < end:

        yield start;

        start+=1;


numberOfTuples= int(input())
output=[]
for i in range(numberOfTuples):

    tuple=eval(input());

    outputOfRange = my_range(tuple[0],tuple[1]);
    output.append(sum(outputOfRange));


#wypisanie wyniku
for out in output:
    print(out);


'''
2
(0 , 1000000)
(717 , 18000)
'''