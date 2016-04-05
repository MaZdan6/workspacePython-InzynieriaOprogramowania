from lab_08.zad2 import Kalkulator;
import csv;


myDelimeter=',';
plik='phoneCalls.csv';

kalkulator= Kalkulator(plik, myDelimeter);

#kalkulator.printUsers();

#print(kalkulator.getMaxNumberOfCalls());
#print(kalkulator.getMaxNumberofReceivedCalls());

print(kalkulator.mostFrequentyCallingUsers());
# #[’226 ’, ’47 ’, ’75 ’, ’152 ’, ’158 ’, ’176 ’, ’297 ’, 359 ’, ’363 ’, ’375 ’]

#print(kalkulator.mostFreuqentyReceiveUsers());
# [’5’, ’0’, ’2’, ’13 ’, ’172 ’, ’1’, ’15 ’, ’32 ’,’23 ’, ’42 ’]

#print(kalkulator.mostUsedCellTower());
# (’15 ’, 54)

#print(kalkulator.statisicsorMostCallingUser());
# 1077.4 0.71

# maxNumberofCalls= kalkulator.getMaxNumberofCalls();
#maxNumberofReceivedCalls= kalkulator.getMaxNumberofReceivedCalls();

# print(maxNumberofCalls);
#print(maxNumberofReceivedCalls);