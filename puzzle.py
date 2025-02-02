def escape_room_puzzle():
    print('Welcome to Escape Room Puzzle ')
    print("In this game, you will have to answer 3 questions.\nEach question requires 1 point.\nSo best of luck! ")
    print("Let's begin the game !!!!!!")

    points = 0
    ques = 0

# Question 1
    print('Question 1: If you drop me, I crack. If you smile at me, I smile back. What am I?')
    ans1 = input('What is your Answer: ').lower()  
    if ans1 == 'mirror':
        print('You did it!')
        points += 1
        ques += 1 
    else:
        print("It's totally fine; the answer to question no.1 was 'mirror'.")
        ques -=1

# Question 2
    print('Question 2: What is half of two plus two?')
    ans2 = input('What is your Answer: ')
    if int(ans2) == 2:  
        print('Well done!')
        points += 1
        ques += 1 
    else:
        print("Nice try, the answer was '2'.")
        ques -= 1

# Question 3
    print('What is the answer to (2 * 2 / 2 * 6)?')
    ans3 = input('What is your Answer: ')
    if int(ans3) == (2 * 2 / 2 * 6) :  
        print('Nice job!')
        points += 1 
        ques += 1 
    else:
        print("You basically go to school just go to sleep right.The answer was '12'!!!")
        ques -= 1
   
    print(f'You got {points} points.As You answered {ques} question correctly')
    if int(ques) == 3 :
        print('You answered all questions correctly')
        print('Your parents are proud of you')
        print('also you escaped the room Congrats!')
    elif int(ques) == 2:
        print('You are just a point behind')
        print('That is how a point matters')
        print('burn in fire now you should have tried to answer that question')
    else :
        print('ohhh myyy god!')
        print('SSTTUUDDYY HHAARRDD')
        print('gburn in fire now you should have tried to answer the questions')
    print('Good Bye!!!!')

escape_room_puzzle()
