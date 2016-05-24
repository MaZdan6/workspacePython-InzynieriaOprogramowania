from urllib import request
from bs4 import BeautifulSoup

#input
#url=input();
url = 'http://150.254.36.91/mt/mt1.html'
html_string = request.urlopen(url).read()

html_doc= html_string




soup = BeautifulSoup(html_doc, "html.parser")
#print(soup.findAll("p"))



#lista spanów z różnymi atrybutanami i atrybutem class="points"
listItemList= soup.select("ul.vp-ul li")

"""
(’Vessel Name ’, ’ATLOY VIKING ’) 1
(’IMO ’, ’8502418 ’) 2
(’MMSI ’, ’258559000 ’) 3
(’Call Sign ’, ’LCGV ’) 4
(’Flag ’, ’Norway (NO)’) 5 #zle
(’AIS Type ’, ’Fishing ’) #zle
"""
dataList=[]
dataDictionary= dict()
for text in listItemList:

    data=text.text
    key=str(data.split(':')[0])
    value=data.split(':')[1]
    dataDictionary[key]= value

#Call Sign
callSign= soup.select("div  b")[6].text




#print(dataDictionary)

outputDictionary= dict()

outputDictionary['Vessel Name']= dataDictionary['Name'];
outputDictionary['IMO']= dataDictionary['IMO'];
outputDictionary['MMSI']= dataDictionary['MMSI'];
outputDictionary['Call Sign']= callSign;
outputDictionary['Flag']= dataDictionary['Flag'];
outputDictionary['Type']= dataDictionary['Type'];


print("('"+"Vessel Name"+"','"+outputDictionary['Vessel Name']+"')")
print("('"+"IMO"+"','"+outputDictionary['IMO']+"')")
print("('"+"MMSI"+"','"+outputDictionary['MMSI']+"')")
print("('"+"Call Sign"+"','"+outputDictionary['Call Sign']+"')")
print("('"+"Flag"+"','"+outputDictionary['Flag']+"')")
print("('"+"AIS Type"+"','"+outputDictionary['Type']+"')")


"""
suma=0
oceny= []
for span in spanList:
    oceny.append(int(span.text));
#print(oceny);

mean= sum(oceny)/len(oceny)
print(mean)
"""