# testing using While loops
# loop basically checks for conditions here; as Python typcasts inputs as str
while True:
    try:      
        FirstNum = int(input("Enter a number: "))  #while FirstNum is an int is True, loop will break
        break
    except ValueError: #Excpet for ValueError, if anything except for a String is entered
        print ('Try Again\n')  #Will print this and loop back to Start!


while True:
    try:
        SecondNum = int(input("Enter a number: "))
        break
    except ValueError:
        print ("Try Again\n")


