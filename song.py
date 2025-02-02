import random

def guess_the_song():
    bts_songs = {
        "Dynamite": "Cause I, I, I'm in the stars tonight",
        "Butter": "Smooth like butter, like a criminal undercover",
        "Boy With Luv": "Nan neoreul salanghae",
        "Fake Love": "I don't know, I don't know, I don't know why",
        "Blood Sweat & Tears": "Pi ttam nunmul (Blood, sweat, tears)"
    }
    
    song, lyrics = random.choice(list(bts_songs.items()))
    
    print("Guess the BTS Song!")
    user_answer = input(f"Here are the romanized lyrics: {lyrics} ")
    
    if user_answer.strip().lower() == song.lower():
        print("Correct!")
    else:
        print(f"Wrong! The song is: {song}")

guess_the_song()
