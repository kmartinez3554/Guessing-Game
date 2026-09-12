import random

number = random.randint(1, 10)

player_name = input("Hello, what is your name?\n")

number_of_guesses = 0

print("Okay " + player_name + ". I'm guessing a number between 1 and 10: ")

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1

    if guess < number:
        print("Your guess is too low. Try again!")
    elif guess > number:
        print("Your guess is too high. Try again!")
    else:
        break

if guess == number:
    print("Congratulations, " + player_name + "! You guessed the number in " + str(number_of_guesses) + " tries!")
else:
    print("Sorry, " + player_name + ", you did not guess the number. The number was " + str(number))
