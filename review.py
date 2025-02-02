def review():
    print('--------------------------------------')
    print('-----Welcome To 5 Star Restaurant-----')
    print('--------------------------------------')
    rate = float(input('Enter your experience out of 5 : '))
    print('--------------------------------------')
    if rate >= 4.5 :
        print('-----Extraodinary-----')
    elif rate >= 4 :
        print('-----Excellent-----')
    elif rate >= 3 :
        print('-----Good-----')
    elif rate >= 2 :
        print('-----Fair-----')
    else :
        print('-----Poor-----')

review()
print('--------------------------------------')
print('------Thank You------')
print('--------------------------------------')

