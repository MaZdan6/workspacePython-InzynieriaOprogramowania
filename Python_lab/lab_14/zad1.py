from urllib import request
from bs4 import BeautifulSoup

#input
#url=input();
url = 'http://150.254.36.91/mt/cokupic.html'
html_string = request.urlopen(url).read()

html_doc= html_string




soup = BeautifulSoup(html_doc, "html.parser")
#print(soup.findAll("p"))



#lista spanów z różnymi atrybutanami i atrybutem class="points"
spanList= soup.select("div.opinion span.points")

suma=0
oceny= []
for span in spanList:
    oceny.append(int(span.text));
#print(oceny);

mean= sum(oceny)/len(oceny)
print(mean)