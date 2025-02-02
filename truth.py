import random

def truth_or_dare():
    print("Let's play Truth or Dare!")
    
    # Randomly choose whether the challenge is a truth or a dare
    choice = random.choice(["truth", "dare"])
    
    if choice == "truth":
        truths = [
            "What is your biggest fear?",
            "What is the most embarrassing thing you've ever done?",
            "What is your biggest secret?"
        ]
        print(f"Truth: {random.choice(truths)}")
    elif choice == "dare":
        dares = [
            "Do 10 jumping jacks!",
            "Send a funny message to your friend!",
            "Sing a song!"
        ]
        print(f"Dare: {random.choice(dares)}")

truth_or_dare()
