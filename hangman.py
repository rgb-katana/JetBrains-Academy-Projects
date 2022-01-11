import random
list_of_answers = ['python', 'java', 'kotlin', 'javascript']
the_answer = random.choice(list_of_answers)
lives = 8
game_on = True

print("H A N G M A N")
while game_on:

    starter_choice = input('Type "play" to play the game, "exit" to quit: ')
    if starter_choice == "exit":
        game_on = False
    elif starter_choice == "play":

        game_word = list("-" for element in the_answer)
        letters_not_used = []
        while lives > 0:
            print("")
            print("".join(game_word))
            user_input = input("Input a letter: ")

            if len(user_input) == 1:
                if user_input.isalpha() and user_input == user_input.lower():

                    if user_input in game_word or user_input in letters_not_used:
                        print("You've already guessed this letter")

                    elif user_input in the_answer:
                        num_of_letters = the_answer.count(user_input)
                        position = 0

                        for j in range(num_of_letters):
                            letter = the_answer.find(user_input, position)
                            game_word[letter] = user_input
                            position += letter + 1

                        if "-" not in game_word:
                            break

                    else:
                        letters_not_used.append(user_input)
                        print("That letter doesn't appear in the word")
                        lives -= 1

                else:
                    print("Please enter a lowercase English letter")
            else:
                print("You should input a single letter")

        if "-" in game_word and lives >= 0:
            print("You lost!\n")
        else:
            print("")
            print(the_answer)
            print("You guessed the word!\nYou survived!\n")

    else:
        continue
