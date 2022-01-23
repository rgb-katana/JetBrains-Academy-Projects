import random

items = ["paper", "rock", "scissors"]


def game_conditions(user_option, comp_option):
    if user_option == "paper" and comp_option == "rock":
        return 100
    elif user_option == "rock" and comp_option == "scissors":
        return 100
    elif user_option == "scissors" and comp_option == "paper":
        return 100
    elif comp_option == "paper" and user_option == "rock":
        return 0
    elif comp_option == "rock" and user_option == "scissors":
        return 0
    elif comp_option == "scissors" and user_option == "paper":
        return 0
    else:
        return 50


def reading_user_score(file):
    u_scores = {}
    for line in file:
        (key, val) = line.split()
        u_scores[key] = val
    return u_scores


def writing_user_score(file, player_scores):
    for player in player_scores:
        print(player + " " + str(player_scores[player]), file=file)


def default_game():
    while True:  # game

        user_play = input()
        if user_play == "!exit":  # quit playing
            print("Bye!")
            break

        elif user_play == "!rating":  # know your score
            print(f"Your rating: {scores_dict[player_name]}")

        elif user_play in items:  # results
            computer_play = random.choice(items)
            result = game_conditions(user_play, computer_play)
            if result == 100:
                scores_dict[player_name] = int(scores_dict[player_name]) + 100
                print(f"Well done. The computer chose {computer_play} and failed")
            elif result == 0:
                scores_dict[player_name] = int(scores_dict[player_name]) + 0
                print(f"Sorry, but the computer chose {computer_play}")
            elif result == 50:
                scores_dict[player_name] = int(scores_dict[player_name]) + 50
                print(f"There is a draw ({computer_play})")

        else:
            print("Invalid input")


def list_format(og_list, u_play):
    pos = og_list.index(u_play)
    preceding = og_list[:pos]
    formatted_list = og_list[pos:]
    formatted_list.extend(preceding)
    return formatted_list[1:]


def advanced_game(original_list):
    while True:  # game

        user_play = input()
        if user_play == "!exit":  # quit playing
            print("Bye!")
            break

        elif user_play == "!rating":  # know your score
            print(f"Your rating: {scores_dict[player_name]}")

        elif user_play in original_list:  # results
            choosing_list = list_format(original_list, user_play)
            comp_play = random.choice(original_list)
            if user_play == comp_play:
                scores_dict[player_name] = int(scores_dict[player_name]) + 50
                print(f"There is a draw ({comp_play})")
            else:
                comp_play_index = choosing_list.index(comp_play) + 1
                if comp_play_index <= len(choosing_list) / 2:
                    scores_dict[player_name] = int(scores_dict[player_name]) + 0
                    print(f"Sorry, but the computer chose {comp_play}")
                elif comp_play_index > len(choosing_list) / 2:
                    scores_dict[player_name] = int(scores_dict[player_name]) + 100
                    print(f"Well done. The computer chose {comp_play} and failed")

        else:
            print("Invalid input")


player_name = input("Enter your name: ")
print("Hello,", player_name)

scores = open("rating.txt", "r")
scores_dict = reading_user_score(scores)  # creating a dict from file
scores.close()

if player_name not in scores_dict:
    scores_dict[player_name] = 0


list_of_options = input().split(",")
print("Okay, let's start")
if len(list_of_options) == 1:
    default_game()
else:
    advanced_game(list_of_options)


scores = open("rating.txt", "w")
writing_user_score(scores, scores_dict)
scores.close()
