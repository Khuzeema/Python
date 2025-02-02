def story_builder():
    print("Let's create a story together! I'll start the story, and you add the next sentence.")
    story = "Once upon a time, there was a dragon who loved to explore."
    print(story)
    next_sentence = input("Your turn! Add the next sentence: ")
    story += " " + next_sentence
    print("Here is the story so far:")
    print(story)

story_builder()
