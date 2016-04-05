from lab_08.zad1 import Kalkulator;
import csv;


myDelimeter=',';
plik='phoneCalls.csv';

kalkulator= Kalkulator(plik, myDelimeter);

#kalkulator.printUsers();

print(kalkulator.getMaxNumberOfCalls());
print(kalkulator.getMaxNumberofReceivedCalls());
# maxNumberofCalls= kalkulator.getMaxNumberofCalls();
#maxNumberofReceivedCalls= kalkulator.getMaxNumberofReceivedCalls();

# print(maxNumberofCalls);
#print(maxNumberofReceivedCalls);