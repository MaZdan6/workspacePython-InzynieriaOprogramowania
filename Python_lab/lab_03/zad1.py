__author__ = '23901'


import math

values = input ()
v=values.split(" ")

a= int(v[0])
b= int(v[1])
#print(a)
#print(b)


def binomial(a, b):
    try:
        binom = math.factorial(a) /( math.factorial(b) * math.factorial(a - b))
    except ValueError:
        binom = 0
    return binom

def binomial2(a, b):

    binom = math.factorial(a) /( math.factorial(b) * math.factorial(a - b))
    return binom

bin= binomial2(a,b)
bin= int(bin)
#print("Binomial", bin)
print(bin)