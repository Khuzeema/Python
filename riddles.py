def riddles():
    riddles = {
        "What has keys but can't open locks?": "Piano".lower(),
        "What comes once in a minute, twice in a moment, but never in a thousand years?": "The letter 'M'".lower()
    }
    print("Let's solve some riddles!")
    
    for riddle, answer in riddles.items():
        user_answer = input(f"Riddle: {riddle} ")
        if user_answer.strip().lower() == answer.lower():
            print("Correct!")
        else:
            print(f"Wrong! The answer is: {answer}")
            
riddles()
