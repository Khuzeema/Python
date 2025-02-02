answer = input('Are we there yet? ')

while answer.strip().lower() != 'Yes':
    answer = input('Are we there yet? ')
    if answer == 'yes'.lower():
        break
    else:
        continue
    
print('Finally we arrived')