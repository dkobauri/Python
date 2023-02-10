import random

guessesUsed = 0
Name = input("Hello! what is your name? ")
number = random.randint(1, 100)
print(f"Greetings, {Name} i am thinking of a number between 1 and 100.")
while guessesUsed < 5:
    guess = int(input(f"Guess the number within 5 guesses... "))
    guessesUsed = guessesUsed + 1
    if guess < number:
        print(f"Too low try again.")
    if guess > number:
        print(f"Too high, try again.")
    if guess == number:
        break
if guess == number:
    guessesUsed = str(guessesUsed)
    print(f"Well done {Name}! You guessed correctly in {guessesUsed} guesses.")

if guess != number:
    number = str(number)
    print(f"Sorry, out of guesses. The number I was thinking of is {number}.")
