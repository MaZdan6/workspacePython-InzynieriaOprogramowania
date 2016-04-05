import csv;




class User:

    def __init__(self, id):

        self.id= id
        self.numberOfCalls=0
        self.numberOfReceivedCalls=0
        self.duration=0
        self.durationOfReceivedCalls=0

    #dodaje czas rozmowy do sumy
    def addDuration(self, duration):

        self.duration= self.duration+ int(duration)
        self.numberOfCalls= self.numberOfCalls+1

    #dodaje czas rozmowy do sumy
    def addDuration(self, duration):

        self.duration= self.duration+ int(duration)
        self.numberOfCalls= self.numberOfCalls+1

    #dodaje czas rozmowy przychodzącej do sumy
    def addDurationofReceivedCalls(self, duration):

        self.durationOfReceivedCalls= self.durationOfReceivedCalls+ int(duration)
        self.numberOfReceivedCalls= self.numberOfReceivedCalls+1
    def toString(self):
        return ("id:",self.id , "calls:", self.numberOfCalls, "duration:", self.duration,"numberOfReceiveCalls:", self.numberOfReceivedCalls, "durationOfReceivedCalls:", self.durationOfReceivedCalls)



class Kalkulator:

    def __init__(self, fileName,delimeter):
        self.fileName= fileName
        self.myDelimeter=delimeter
        self.users= self.readFile()

    #tworzenie słownika Uzytknowników na podstawie pliku
    def readFile(self):
        '''

        :return: słownik z użytkownikami
        '''

        #tworzenie dialectu
        file = open(self.fileName, 'r')
        csv.register_dialect('mojDialekt', delimiter =self.myDelimeter, quoting =csv.QUOTE_ALL)
        #czytanie pliku
        reader = csv.reader(file, dialect='mojDialekt')

        # slownik z userami klucz: id | wartosc: User
        users= dict()

        index_id=0
        index_duration= 3
        index_id_of_receiver=1
        for i, rekord in enumerate(reader):
            if i == 0:
                #wypisanie nagłówka
                naglowek = rekord
                #print(naglowek);
            else:
                #print(rekord[index_id],' ',rekord[index_duration]);
                id= rekord[index_id]
                duration= rekord[index_duration]

                #liczenie liczby połączeń wychodzącyh i sumy ich czasu
                if id in users:
                     users[id].addDuration(duration)
                     
                else:
                    user= User(id)
                    user.addDuration(duration)
                    users[id]= user

                #liczenie liczby połączeń przychodzących i sumy ich czasu
                id= rekord[index_id_of_receiver]
                if id in users:
                     users[id].addDurationofReceivedCalls(duration)

                else:
                    user= User(id)
                    user.addDurationofReceivedCalls(duration)
                    users[id]= user

        file.close()
        return users

    def getMaxNumberOfCalls(self):

        #lista liczby połączeń każdego użytkownika
        callsList=[];
        for key in self.users:
           callsList.append(self.users[key].numberOfCalls);

        #największa liczba połączeń
        maxCalls= max(callsList);

        #użytkownicy z max liczbą rozmow
        userTopDict=dict();

        for id in self.users:
            if(self.users[id].numberOfCalls == maxCalls):
                userTopDict[id]= self.users[id];
        #print(userTopDict)

        #użytkownik z najmniejszym id
        minId= min(userTopDict);
        #print(minId);

        output= "".join((str(minId),": ",str(self.users[minId].duration)));
        #print(output);
        return output






    def getMaxNumberofReceivedCalls(self):
        callsList=[];
        for key in self.users:
           callsList.append(self.users[key].numberOfReceivedCalls);

        maxCalls= max(callsList);

        #użytkownicy z max liczbą rozmow
        userTopDict=dict();

        for id in self.users:
            if(self.users[id].numberOfReceivedCalls == maxCalls):
                userTopDict[id]= self.users[id];
        #print(userTopDict)

        #użytkownik z najmniejszym id
        minId= min(userTopDict);
        #print(minId);

        output= "".join((str(minId),": ",str(self.users[minId].durationOfReceivedCalls)));
        #print(output);
        return output



    def printUsers(self):

        for key in self.users.keys():

            user= self.users.get(key)
            print(user.toString());

    # lista 10 identyfikatorów najczesciej dzwoniacych
    def mostFrequentyCallingUsers(self):

        #lista liczby połączeń wychodzących dla każdego użytkownika
        listOfNumberOfCalls=[];
        for id in self.users:
            listOfNumberOfCalls.append(self.users[id].numberOfCalls);
        print(listOfNumberOfCalls);


        #lista posortowana malejąco
        listOfNumberOfCalls= sorted(listOfNumberOfCalls, reverse=True );
        print(listOfNumberOfCalls);
        #dziesiąty największa licza połączeń
        tenthMaxNumber= listOfNumberOfCalls[9];
        print("tenthMaxNumber: ",tenthMaxNumber);

        #lista liczb połączeń większych, bądź równych of tenthMaxNumber
        topList=[]
        index=0;
        while listOfNumberOfCalls[index]>=tenthMaxNumber:
            topList.append(listOfNumberOfCalls[index]);
            index= index+1;
        print("topList: ", topList);

        #mozliwe liczby połączeń
        setOfTopNumbersOfCalls= sorted(set(topList), reverse=True);
        print("setOfTopNumbersOfCalls: ",setOfTopNumbersOfCalls);


        #lista id użytkowników
        #użytkownik jest na liście?
        #lista ma dziesięć elementów
        return "mostFrequentyCallingUsers()";



    #najczesciej uzywany nadajnik wraz łaczna liczba połaczen, do których został uzyty
    #def mostUsedCellTower(self):

    # dla najczesciej dzwoniacego wypisac jego
    # atrybuty: sredni czas połaczenia wychodzacego (zaokraglony do 2
    # miejsc po przecinku) oraz srednia liczba połaczen wychodzacych
    # (zaokraglona do 2 miejsca po przecinku)
    # statisicsorMostCallingUser(self):









'''
#zad1 test


#myDelimeter=',';
#plik='./phoneCalls.csv';

#input
myDelimeter=input();
plik=input();

kalkulator= Kalkulator(plik, myDelimeter);

#kalkulator.printUsers();

print(kalkulator.getMaxNumberOfCalls());
print(kalkulator.getMaxNumberofReceivedCalls());

# output:
# 226: 5387
# 5: 16797

'''











'''



myDelimeter=',';
plik='phoneCalls.csv';
#plik='sample.csv';
#tworzenie dialectu
csv.register_dialect('mojDialekt', delimiter =myDelimeter, quoting =csv.QUOTE_ALL);

#plik
plik_csv = open(plik, 'r');
czytaj = csv.reader(plik_csv, dialect='mojDialekt');




# slownik z userami klucz: id | wartosc: User
users= dict();


index_id=0;
index_duration= 3;
for i, rekord in enumerate(czytaj):
    if i == 0:
        #wypisanie nagłówka
        naglowek = rekord;
        print(naglowek);
    else:
        #print(rekord[index_id],' ',rekord[index_duration]);
        id= rekord[index_id];
        duration= rekord[index_duration];

        if id in users:
             users[id].addDuration(duration)
        else:
            user= User(id);
            user.addDuration(duration);
            users[id]= user;

#wypisanie wszystkich userów
for key in users.keys():

    user= users.get(key)
    print("id: ",user.id , "calls: ", user.numberOfCalls, "duration: ", user.duration );

plik_csv.close();





'''