def earth():
    earth_weight = float(input('Enter your weight: '))
    planet = int(input('Enter your planet number (1-7): '))

    if planet == 1:
        print('Your weight on Mercury is:', earth_weight * 0.38)
    elif planet == 2:
        print('Your weight on Venus is:', earth_weight * 0.91)
    elif planet == 3:
        print('Your weight on Mars is:', earth_weight * 0.38)
    elif planet == 4:
        print('Your weight on Jupiter is:', earth_weight * 2.53)
    elif planet == 5:
        print('Your weight on Saturn is:', earth_weight * 1.07)
    elif planet == 6:
        print('Your weight on Uranus is:', earth_weight * 0.89)
    elif planet == 7:
        print('Your weight on Neptune is:', earth_weight * 1.14)
    else:
        print('Invalid Input')

# Call the function to test
earth()

    