from urllib import request
from bs4 import BeautifulSoup

#input
url=str(input());
#url = 'http://150.254.36.91/mt/mt1.html'
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
    value=data.split(':')[1].strip()
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
#outputDictionary['AIS Type']= dataDictionary['AIS Type'];



#kod html- tabela z danymi
table= soup.select("div.row");
#print(listItemList);
soupTable = BeautifulSoup(str(table), "html.parser")
#print(soupTable);
list= soupTable.select("div.group-ib");
#print(list);
'''
for div in list:
    print(div.text)
'''

for div in list:

    data=div.text
    #pozbywanie się białych spacji
    data= data.rstrip();
    data=data.strip();
    #print(data)

    #'''
    text= data.split(':');


    try:
        key= text[0];
        value=text[1].strip();
        #print("key: "+key)
        #print("value: "+value)

        if key=="Flag":
            #print("FLAAAAAAAAG")
            outputDictionary['Flag']= value;

        elif key=="AIS Type":
            #print("AIS Typeeeeeee")
            outputDictionary['AIS Type']= value;
    except Exception:
        pass

    #'''


keyLst= ('Vessel Name','IMO','MMSI','Call Sign','Flag','AIS Type')

for key in keyLst:
    tup=(key,outputDictionary[key])
    print(tup)