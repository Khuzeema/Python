def grade():
    print('***********************************')
    print('           Welcome                 ')
    print('***********************************')

    grade = int(input('Enter your grade 9/10/11/12 : '))
    if grade == 9 :
        print("You're a Freshman")
    elif grade == 10 :
        print("You're a Sophorome")
    elif grade == 11 :
        print("You're a Junior")
    else:
        print("You're a Senior")
grade()
print('---------Enjoy Your Life---------')