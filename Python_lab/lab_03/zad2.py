__author__ = '23901'


#Oblicz, na ile sposobów mozna rozmienic okreslona kwote pieniedzy,
#majac do dyspozycji okreslone nominały.

#input


amount = int(input ())
print("Amount= ", amount)


denominations = input ()
d=denominations.split(" ")

# zamiana listy z stringami na liste z int
d = [int(i) for i in d]

print("Denomintation: ")
for i in d:
    print(i)


def ile1( n):

    return 1

def ile2( n):

    if(n<1):
        return 1;
    if(n==2):
        return 2;
    else:
        return ile2(n-2)+ile1(n-1);

def ile3( n):

    if(n>=3):
        return ile3(n-3)+ile2(n);
    return ile2(n);

def ile5(n):

    if(n>=5):
        return ile5(n-5)+ile3(n);
    return ile3(n);

def ile10( n):

    if(n>=10):
        return ile10(n-10)+ile5(n);
    return ile5(n);


#print(str(ile10(amount)))


def coin1(n, d):


    return d[0]

def coin2(n, d):


    if(n<d[0]):
        return d[0];
    if(n==d[1]):
        return d[1];
    else:
        return coin2(n-d[1],d)+coin1(n-d[0], d);

def coin3(n, d):


    if(n>=d[2]):
        return coin3(n-d[2], d)+coin2(n, d);
    return coin2(n, d);


def getOutput(n, d):

    if len(d)==1:
        return coin1(n,d)
    if len(d)==2:
        return coin2(n, d)
    if len(d)==3:
        return coin3(n, d)

print(getOutput(amount,d))
'''def combinations(denominations,n):
    for i in range(0, len[denominations]):

        if(n>=d[-i]):
            return combinations(n-d[-i],n)+ combinations(n-d[-i-1],n)
        combinations(n-d[-i-1],n)

print(combinations(d,amount))
'''
'''def q(n):
    return 1

def r(n):




    return q(n)+ r(n-10)

def s(n):
    return r(n)+ s(n-20)

def p(n):
    return s(n)+p(n-50)


print(p(100))
'''

'''def r(denomination, n):
    return q(n)+r(n-denomination)

def p(n):
    p=0
    for i in d:
        p= p+r(i,1)
    return p
'''


#print(a)
#print(b)

