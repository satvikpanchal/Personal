# rock, paper, scissors with the computer - computer generate a
# random option out of stone/paper or scissors; user inputs the
# option and scorekeeper shares the score

import random

print("*Warning*")
print("This game is best out of 3")

comp_score = 0
human_score = 0

#main
while True:

    list_obj = ['Stone', 'Paper', 'Scissors']
    random_Option = random.choice(list_obj)

    user_option = input(str("Please select from these options: Stone, Paper, Scissors: "))

    if random_Option == user_option:
        print("Draw again, both, the computer and you drew", random_Option)

    if user_option == "Stone" and random_Option == "Scissors":
        print("You have won this draw")
        human_score += 1
    elif user_option == "Stone" and random_Option == "Paper":
        print("Computer won this draw, it was", random_Option)
        comp_score += 1

    elif user_option == "Paper" and random_Option == "Stone":
        print("You have won this draw")
        human_score += 1
    elif user_option == "Paper" and random_Option == "Scissors":
        print("Computer won this draw, it was", random_Option)
        comp_score += 1

    elif user_option == "Scissors" and random_Option == "Paper":
        print("You have won this draw")
        human_score += 1
    elif user_option == "Scissors" and random_Option == "Stone":
        print("Computer won this draw it was", random_Option)

    print("Your score is", human_score)
    print("Computer's score is", comp_score)

    if comp_score == 2:
        print("Computer won the game!")
        break
    elif human_score == 2:
        print("You have won the game!")
        break
