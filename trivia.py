def trivia_quiz():
    questions = {
        "What is the capital of France?": "Paris",
        "What is the chemical symbol for water?": "H2O",
        "Who wrote 'To Kill a Mockingbird'?": "Harper Lee"
    }
    score = 0
    print("Welcome to the Trivia Quiz!")
    
    for question, answer in questions.items():
        user_answer = input(f"{question} ")
        if user_answer.strip().lower() == answer.lower():
            score += 1
    
    print(f"You scored {score}/{len(questions)}")

trivia_quiz()
