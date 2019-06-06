# This is a guess the number game which asks the user to continue guessing until correct.
# author: Sooyong Lee
import random
randomNumber = random.randint(1, 20)
found = False
numGuesses = 0
print("I am thinking of a number between 1 and 20.")
while not found:
    print("Take a guess.")
    guess = int(input())
    numGuesses+=1
    if guess == randomNumber:
        print("Good job! You guessed my number in " + str(numGuesses) + " guesses!")
        found = True
    else:
        if guess > randomNumber:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")