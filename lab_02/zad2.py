

#print("Wprowadz ciąg znaków")
string = input()
#print(string)

numberOfLeftBracket= 0
numberOfRightBracket= 0

validBrakets = True

for s in string:
    #print(s)
    if s=="(":
        numberOfLeftBracket+=1;
        #print("numberOfLeftBracket",numberOfLeftBracket)
        continue
    if s==")":

        numberOfLeftBracket-=1;

        #print("numberOfLeftBracket",numberOfLeftBracket)
    #jesli prawych nawiasow jest więcej niż lewych, to przerwij pętlę
    if numberOfRightBracket> numberOfLeftBracket:
        validBrakets= False
        break

print(validBrakets)
#print(numberOfLeftBracket)
#print(numberOfRightBracket)