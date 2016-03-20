


class Employee:

    def __init__(self,name, bruttoSalary):
        self.name=name;
        self.bruttoSalary= float(bruttoSalary);



    def getNettoSalary(self):

        a= self.bruttoSalary
        b=a;

        #składki na ubezpieczenia społeczne finansowane przez pracownika
        c1= 0.0976*b;
        c1= round(c1,2)

        c2= 0.015*b;
        c2= round(c2,2)

        c3= 0.0245*b;
        c3= round(c3,2)

        c= c1+c2+c3
        c=round(c,2)
        #podstawa wymiaru składki na ubezpieczenie zdrowotne

        d= b-c;
        #składka na ubezpieczenie zdrowotne do pobrania z wynagrodzenia

        e= d*0.09;
        e=round(e,2);

        #składka na ubezpieczenie zdrowotne do odliczenia od podatku

        f=d*0.0775;
        f=round(f,2);

        #koszty uzyskania przychodu

        g= 111.25

        #podstawa obliczenia zaliczki na podatek dochodowy, po zaokrągleniu do pełnych złotych

        h= a-g-c;
        h=round(h,0);

        #zaliczka na podatek dochodowy przed odliczeniem składki zdrowotnej
        i=h* 0.18-46.33;
        i=round(i,2);
        #zaliczka na podatek dochodowy do pobrania, po zaokrągleniu do pełnych złotych

        j= i-f;
        j=round(j,0);

        #kwota do wypłaty
        k= a-c-e-j;
        k= round(k,2);

        #składki obciążające pracodawcę od kwoty

        l1= c1;

        l2=0.065* b
        l2=round(l2,2)

        l3= +0.0193*b
        l3=round(l3,2)

        l4=0.0245*b
        l4=round(l4,2)

        l5=0.001*b
        l5=round(l5,2)

        l=l1+l2+l3+l4+l5;

        #razem koszt pracodawcy
        ll= a+l;
        ll=round(ll, 2);

        #print(self.name, k, l,ll);


        return [self.name, k, l,ll];

        #return [self.name, '%.2f' % k, '%.2f' % l,'%.2f' % ll];




#input
employeesNumber = int(input());
#print("employeesNumber= ", employeesNumber);

employees= []
for i in range(0,employeesNumber):

    inputData= input();
    inputData= inputData.split(" ")
    e= Employee(inputData[0], inputData[1])
    employees.append(e)


#output
sumOfEmployeersCost=[]

for e in employees:
    output=e.getNettoSalary()

    #'%.2f' %
    print(output[0], '%.2f' % output[1], '%.2f' % output[2], '%.2f' % output[3],);

    sumOfEmployeersCost.append(output[3]);

print(sum(sumOfEmployeersCost));

