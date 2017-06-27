import random  # Importing random function

guessesTaken = 0  # Setting the number of guesses at 0

print('Hello! What is your name?')  # Asks the users name
myName = input()  # Stores the name which was given for the question

number = random.randint(1, 20)  # Generates a random number between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # Asks the user for a number between 1 and 20

while guessesTaken < 6:  # While cycle which allows max 5 guesse for the user to find out the right number
    print('Take a guess.')  # Asks the user for a guess
    guess = input()  # Stores the imput as guess
    guess = int(guess)  # Turns guess to an integer

    guessesTaken += 1  # Adds 1 to number of guesses

    if guess < number:  # Checks if the guessed number is smaller than the generated one
        print('Your guess is too low.')  # If it is smaller it will tell the user

    if guess > number:  # Checks if the guessed number is bigger than the generated one
        print('Your guess is too high.')  # If it is bigger it will tell the use

    if guess == number:  # Checks if the guessed number is equal than the generated one
        break  # If its equal breaks the while cycle

if guess == number:  # Checks if the guessed number is equal than the generated one
    guessesTaken = str(guessesTaken)  # If its equal turns guessTaken to a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    # Prints out this sentence with the users name and the numbers of the guesses

if guess != number:  # Checks if the guessed number is not equal than the generated one
    number = str(number)  # If its not equal turns number to a string
    print('Nope. The number I was thinking of was ' + number)  # Prints out this sentence with the right number