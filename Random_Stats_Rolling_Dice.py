import random

Endurance = 0
CR = 0
Luck = 0
Endurance = random.randint(1, 15)
CR = random.randint(1, 20)
Luck = random.randint(1, 10)
print(f"Your character's stats are as follows:")
print(f"Endurance: {Endurance}.")
print(f"Combat Rating: {CR}.")
print(f"Luck: {Luck}.")


