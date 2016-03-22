__author__ = '23901'

pesel= input()

# pisze ostatnia litere print(pesel[-1])
lastNumberOfInput= int(pesel[-1])
#print("ostatni pesel", lastNumberOfInput)

#12345678901
#abcdefghijk
#1*a + 3*b + 7*c + 9*d + 1*e + 3*f + 7*g + 9*h + 1*i + 3*j

a=1*int(pesel[0])
b=3*int(pesel[1])
c=7*int(pesel[2])
d=9*int(pesel[3])
e=1*int(pesel[4])
f=3*int(pesel[5])
g=7*int(pesel[6])
h=9*int(pesel[7])
i=1*int(pesel[8])
j=3*int(pesel[9])
k=1*int(pesel[10])
#dodaje iloczyny
#a+b+c+d+e+f+g+h+i+j+k
calculation= a+b+c+d+e+f+g+h+i+j+k
#print(calculation)

modulo= calculation%10

if modulo==0:
    print(1)
else:
    print(0)

