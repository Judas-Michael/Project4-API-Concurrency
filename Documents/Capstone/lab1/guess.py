# Guess the number game, import random number module
import random

# Set guesses variable to 0
guesses = 0

# Set number variable with random number range between 1-10
number = random.randint(1,10)

# Guess loop allows 3 guesses
while guesses<3:
# Display question to user
	print('You have 3 chances to guess which number I am thinking of between 1 and 10... Guess a number!')
	guess = input()
	guess = int(guess)

# Once user takes a guess, number of guesses increased by 1
	guesses = guesses + 1

	if guess<number:
		print('Your guess is too low!')

	if guess>number:
		print('Your guess is too high!')

# Exit loop when user guesses correct number
	if guess == number:
		break

# If guess is correct, show how many tries it took user
if guess == number:
	guesses = str(guesses)
	print ('Awesome! You guessed my number in ' + guesses + ' guesses!')

if guess !=number:
	number = str(number)
	print('INCORRECT. The number I was thinking of was' + number)