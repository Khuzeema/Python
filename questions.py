class TwentyQuestions:
    def __init__(self):
        self.questions = [
            ("Is it alive?", ["animal", "plant"]),
            ("Is it man-made?", ["object"]),
            ("Can it be found indoors?", ["furniture", "electronics", "food", "object"]),
            ("Is it something you use every day?", ["furniture", "electronics", "object"]),
            ("Is it larger than a car?", ["vehicle", "building"]),
            ("Is it used for entertainment?", ["electronics", "toy", "object"]),
            ("Is it something you can eat?", ["food"]),
            ("Is it a household item?", ["furniture", "electronics", "object"]),
            ("Can it fly?", ["bird", "airplane"]),
            ("Does it require electricity?", ["electronics"]),
            ("Can it be worn?", ["clothing"]),
            ("Does it have fur or hair?", ["animal"]),
            ("Can it be dangerous?", ["weapon", "animal"]),
            ("Is it a living creature?", ["animal", "plant"]),
            ("Is it something you can buy online?", ["object", "electronics", "clothing"])
        ]
        self.possible_answers = {"animal": "It could be an animal.", 
                                 "plant": "It could be a plant.",
                                 "object": "It could be an object.",
                                 "furniture": "It could be a piece of furniture.",
                                 "electronics": "It could be an electronic item.",
                                 "food": "It could be food.",
                                 "vehicle": "It could be a vehicle.",
                                 "toy": "It could be a toy.",
                                 "clothing": "It could be clothing.",
                                 "weapon": "It could be a weapon.",
                                 "airplane": "It could be an airplane.",
                                 "bird": "It could be a bird.",
                                 "building": "It could be a building."
                                }

    def play(self):
        print("I will try to guess what you're thinking by asking yes/no questions!")
        print("Please answer with 'yes' or 'no'.")
        possible_choices = set(["animal", "plant", "object", "furniture", "electronics", "food", "vehicle", "toy", "clothing", "weapon", "airplane", "bird", "building"])
        
        for question, options in self.questions:
            answer = input(question + " (yes/no): ").lower().strip()
            if answer == "yes":
                possible_choices.intersection_update(options)
            if len(possible_choices) == 1:
                print(f"\nI think you are thinking about a {next(iter(possible_choices))}.")
                print(self.possible_answers[next(iter(possible_choices))])
                return

        print("\nI couldn't guess exactly, but here are the possibilities:")
        for choice in possible_choices:
            print(self.possible_answers[choice])

if __name__ == "__main__":
    game = TwentyQuestions()
    game.play()
