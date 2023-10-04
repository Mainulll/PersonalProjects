import math
import PySimpleGUI as psg #toolkit for creating a GUI

# organising the layout for the windows

# setting the font
font = ("Arial", 15)

layout=[
    [psg.Text("Enter First Operator: "), psg.Input(key='-INPUT-')], # take the number input | PySimpleGUI takes inputs and stores them in a dict,
    ## [psg.Text("Enter Second Number: "), psg.Input(key='-INPUT2-')],# this here will allow for easy access
    [psg.Button("+",size=(3,3), font=font), psg.Button("-",size=(3,3), font=font), psg.Button("/",size=(3,3), font=font), 
     psg.Button("x",size=(3,3), font=font), psg.Button("^",size=(3,3), font=font)],
    [psg.Multiline(default_text='', size=(30, 5), key=('-OUTPUT-'))],
    [psg.Button("Confirm"), psg.Button("Clear"), psg.Button("Backtrack")]
    ]

# creating the main window
window = psg.Window("Calculator", layout, margins=(150, 200), background_color='#808080')

curr_val = 0 # create a variable to store the current value
curr_op = None # initialise a variable with a null value

# even listener for the main window
while True:
    event, values = window.read()
    # will end the program if use closes it
    if event in (psg.WIN_CLOSED, "Exit"):   # because I have added an Exit button, I can modify the break loop to close the program if Exit is clicked;
        break                               # I can do this by making the event belong to multiple operations, including closing the window
    NumIn = values['-INPUT-']
    if event in ("+", "-", "/", "x", "^"):
        curr_op = event # this stores the current operation
    if event == "Confirm":  # reading for an event, if you hit confirm will run this loop
        try:
            NumIn = float(NumIn)  # checking if the number that was inut was an integer 
            print(f"{NumIn}")
        except ValueError: # if a ValueError is caused
            response = psg.popup("Please Enter A Number")  # creates a popup that tells you to correct this issue
            continue
        if curr_op is None:  # if the current operation is none, we will leave the value as it is
            curr_val = NumIn
        elif curr_op is "+": # else run this loop
            curr_val += NumIn
        elif curr_op is "-":
            curr_val -= NumIn
        elif curr_op is "/":
            curr_val /= NumIn
        elif curr_op is "^":
            curr_val ^= NumIn

        # create a running log of previous calculations
        calc_history = f"{curr_val} {curr_op if curr_op else ''} {NumIn if curr_op else ''}\n"
        # updating the output box we created with the history, appending to it
        window['-OUTPUT-'].update(calc_history, append=True)
        window['-INPUT-'].update(" ")
    
    elif event is "Clear":
        curr_val = 0
        curr_op = None
        window['-INPUT-'].update(" ")
        window["-OUTPUT-"].update(" ")

        
window.close()
# infinite while loop waits for the user to close window for the progam to end




# -------
# testing using While loops
# loop basically checks for conditions here; as Python typcasts inputs as str

""" while True:
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
"""
