
import math


class Circle:

    def __init__(self, r):
        self.r=float(r);

    def getArea(self,):
        return math.pi*(self.r*self.r)
class Square:

    def __init__(self, a, b):
        self.a=float(a);
        self.b=float(b);

    def getArea(self,):
        return self.a*self.b

class Triangle:

    def __init__(self, a, b, c):
        self.a=float(a);
        self.b=float(b);
        self.c=float(c);

    def getP(self):

        p= (self.a + self.b + self.c)/2
        return p

    def getArea(self,):

        p= self.getP()
        a= self.a
        b= self.b
        c= self.c

        return math.sqrt(p*(p-a)*(p-b)*(p-c))



#wprowadzanie danych
figures_no = int(input())
#print("figures_no", figures_no)
areas = []


for i in range (0,figures_no):
    figuresParam= input()
    figuresParam= figuresParam.split(" ")

    #print(figuresParam)
    #print(len(figuresParam))

    param_no= len(figuresParam)
    if param_no == 1:
        #print("Koło")

        circle= Circle(figuresParam[0])
        area= circle.getArea()
        areas.append(area)
        #print(area)

    elif param_no == 2:
        #print("Kwadrat")
        square= Square(figuresParam[0], figuresParam[1])
        area= square.getArea()
        areas.append(area)
        #print(area)
    elif(param_no == 3):
         #print("Trójkąt")
         triangle= Triangle(figuresParam[0], figuresParam[1], figuresParam[2])
         area= triangle.getArea()
         areas.append(area)
        #print(area)

    #print(areas)

sumaOfAreas=sum(areas)
sumaOfAreas= round(sumaOfAreas,2)
print(sumaOfAreas)







