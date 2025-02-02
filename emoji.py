def emoji_pictionary():
    emoji = "🦁👑"
    answer = "The Lion King"
    
    print("Guess the movie based on these emojis!")
    user_answer = input(f"Here are the emojis: {emoji} ")
    
    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
    else:
        print(f"Wrong! The answer is: {answer}")
def new():
    emoji = '🛸✨🌌🚀🧹'
    answer = 'Space Sweepers'

    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
    else:
        print(f"Wrong! The answer is: {answer}")

    



emoji_pictionary()
new()