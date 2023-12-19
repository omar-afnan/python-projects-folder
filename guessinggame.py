#question Guessing game: Write a program that generates a 
#random number between 1 and 100 and asks the user to guess it. 
#Give the user hints like "too high" 
#or "too low" until they guess correctly.
import random

number=random.randint(1,100)
guess=0
guessed=False

while not guessed:
    guess=int(input("enter a number will ya  between 1 to 100"))
    guess +=1


    if guess<number:
        print("try again")
    elif guess>number:
        print("the number is tooo high")
    else:
        guessed=True
        print("finally you have guess the correct number {guess}" )

print(f"The secret number was {number}.")