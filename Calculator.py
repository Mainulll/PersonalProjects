while True:
    try:
        FirstNum = int(input("Enter a number: "))
        break
    except ValueError:
        print ('Try Again')

