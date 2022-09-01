'''
Welcome to a very simple guessing game made in python

This game was made because I was bored waiting in class :)

author: Dama D. Daliman

'''

from random import randint

num = randint(1, 100)
guessed = False
while not guessed:
    guess = int(input("Enter your guess: "))
    if guess == num:
        print("That\'s correct!")
        guessed = True
    elif guess > num:
        print("That\'s too big")
        if guess-num > 50:
            print("You\'re waaay off")
    elif guess < num:
        print("That\'s too small")
        if num-guess > 50:
            print("You\'re waaaay off")
    else:
        print("Please enter a valid answer")
