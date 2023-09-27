import math

# testing using While loops
# loop basically checks for conditions here; as Python typcasts inputs as str
while True:
    try:      
        FirstNum = int(input("Enter A Number: "))  #while FirstNum is an int is True, loop will break
        break
    except ValueError: #Excpet for ValueError, if anything except for a String is entered
        print ('Try Again\n')  #Will print this and loop back to Start!

#  mirrored the above statement to error check for an invalid user input
while True:
    try:
        SecondNum = int(input("Enter Your Second Number: "))
        break
    except ValueError:
        print ("Try Again\n")

# created a dictionary to store key-value pairs, designed to act as a menu 
menu = {
    "Addition" : "1",
    "Subtraction" : "2",
    "Multiplication" : "3",
    "Division" : "4",
    "Exponent" : "5",
    "Square Root" : "6",
    "Remainder" : "7"
}
print("\n")
for key, value in menu.items():
    print({value},{key})

NumSelect = input("Select An Operation: ")
for i in NumSelect:
    if i is 1:
        print(FirstNum + SecondNum)
    elif i is 2:
        print(FirstNum - SecondNum)
    elif i is 3:
        print(FirstNum* SecondNum)
    elif i is 4:
        print(FirstNum / SecondNum)
    elif i is 5:
        print(FirstNum ** SecondNum)
    elif i is 6:
        print(FirstNum )

