# This program calls the collatz sequence on the given positive integer, which if called repeatedly will
# eventually render the input to 1.
# author: Sooyong Lee


def collatz(number):
    if number % 2 == 0:
        print(str(number // 2))
        return number // 2
    else:
        print(str(3 * number + 1))
        return 3 * number + 1


print("Enter a positive integer.")
while True:
    try:
        userInput = int(input())
        if userInput <= 0:
            print("You must enter a positive integer.")
            continue
        while userInput != 1:
            userInput = collatz(userInput)
    except ValueError:
        print("You must enter a positive integer.")
