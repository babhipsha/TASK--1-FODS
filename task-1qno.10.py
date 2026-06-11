# 10. Dice Rolling Game: Build a game where the computer and the user each roll a
# random 6-sided die for 5 rounds.
# a. Track the score for both.
# b. After each round, announce the winner of that round.
# c. At the end of 5 rounds, declare the overall winner or if it was a draw.

import random

user_score = 0
computer_score = 0

for round in range(1, 6):
    print("\nRound", round)

    user_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print("User rolled:", user_roll)
    print("Computer rolled:", computer_roll)

    if user_roll > computer_roll:
        print("User wins this round")
        user_score += 1

    elif computer_roll > user_roll:
        print("Computer wins this round")
        computer_score += 1

    else:
        print("Round Draw")

print("\nFinal Scores")
print("User Score =", user_score)
print("Computer Score =", computer_score)

if user_score > computer_score:
    print("User is the Overall Winner!")
elif computer_score > user_score:
    print("Computer is the Overall Winner!")
else:
    print("The Game is a Draw!")
