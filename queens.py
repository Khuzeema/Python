import random

def snapple():
    print('-----------------------------')
    print('     Welcome to Snapple      ')
    print('-----------------------------')

    num = random.randint(0,5)
    if num == 0 :
        print('Flamingos turn pink from eating shrimp')
    elif num == 1 : 
        print("The only food that doesn't spoil is honey")
    elif num == 2 : 
        print('Shrimps can only swim backwards')
    elif num == 3 :
        print("A taste bud's life span is about 10 days")
    elif num == 4 :
        print('It is impossible to sneeze while sleeping')
    else:
        print("It's illegal to sing off-key in North California")

snapple()