import math
import PySimpleGUI as psg #toolkit for creating a GUI

# organising the layout for the windows
layout=[
    [psg.Text("Enter A Number: ")],
    [psg.Input(" ")], # take the number input
    [psg.Button("Confirm")]
    ]

# creating the main window
window = psg.Window("Calculator", layout, margins=(150, 200))

# even listener for the main window
while True:
    event, values = window.read()
    # will end the program if use closes it
    if event == psg.WIN_CLOSED:
        break
    
window.close()
# infinite while loop waits for the user to close window for the progam to end











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
    if i == 1:
        print(FirstNum + SecondNum)
    elif i == 2:
        print(FirstNum - SecondNum)
    elif i == 3:
        print(FirstNum* SecondNum)
    elif i == 4:
        print(FirstNum / SecondNum)
    elif i == 5:
        print(FirstNum ** SecondNum)
    elif i == 6:
        print(FirstNum )

