import random

def evaluate(user, pc):
    if (user == pc):
        print("tie")
    elif (
        (user == "rock" and pc == "scisors") or
        (user == "paper" and pc == "rock") or
        (user == "scisors" and pc == "paper")
    ):
        print("you won")
    else:
        print("PC won")

user_pick = input("Your choice:")
choices = ["rock", "paper", "scisors"]

pc_choice = random.choice(choices)
print(pc_choice)
if user_pick in choices:
    evaluate(user_pick,pc_choice)
else:
    print("invalid input")

