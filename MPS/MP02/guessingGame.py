import random

def guessingGame(min, max, guesses):
    print("You are to guess a number between " + str(min) + " and " + str(max) + " inclusive, in " + str(guesses) + " guesses or less!") 
    
    answer = random.randint(min, max)

    for x in range(guesses):
        guess = int(input("Enter your guess "))
        if guess == answer:
            print("You guessed it!")
            return
        elif guess > answer:
            print("HIGH guess")
        elif guess < answer:
            print("LOW guess")
    print("You ran out of guesses!!!")

guessingGame(0, 200, 10)