def season():
    month = int(input('Enter months in the form of numbers : '))
    if month == 1 or month == 2 or month == 3 :
        print("----------It's Winter----------")
    elif month == 4 or month == 5 or month == 6 :
        print("----------It's Summer----------")
    elif month == 7 or month == 8 or month == 9 :
        print("----------It's Autumn----------")
    elif month == 10 or month == 11 or month == 12 :
        print("----------It's Spring----------")
    else :
        print('Invalid Input\nTry again')

season()
