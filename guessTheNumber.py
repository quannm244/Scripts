import random

correctNumber = random.randint(1,20)
print("I'm thinking of a number between 1 and 20")

# Ask the player to guess 5 times
for noGuess in range (1,6):
	print("Please take a guess: ")
	guess = int(input())
	if guess < correctNumber:
		print("Your guess is lower than correct number.")
	elif guess > correctNumber:
		print("Your guess is higher than correct number.")
	else:
		break
if guess == correctNumber:
	print("You have guessed my number in "+ str(noGuess)+' guesses')
else:
	print("The number I was thinking of was: "+str(correctNumber))
