import random

def play_game():
    
	availableWords = ['rainbow', 'computer', 'science', 'programming',
			'python', 'mathematics', 'player', 'condition',
			'reverse', 'water', 'board', 'geeks']

	keyword = random.choice(availableWords)
	turns = len(keyword)
 
	print("\n")
	print("--------------------------------------")
	print("\tW O R D  G U E S S E R")
	print("--------------------------------------")
	print("\nGuess the individual characters, forming a word!")
	print()
	print("1.\tPlease input one character at a time.")
	print("2.\tYou only have", +turns, "incorrect guesses.")
	print("3.\tFor every correct character, you are awarded 1 extra guess.")
	print("4.\tIf a character has already been guessed, the turn resets.")

	guesses = ''

	while turns > 0:

		failed = 0

		for char in keyword:
			print()
			if char in guesses:
				print(char)
			else:
				print("_")
				failed += 1

		if failed == 0:
			print()
			print("You Win!")
			print("The word is: ", keyword)
			break

		print()
		guess = input("Guess a character: ")

		if guess in guesses:
			print("Character already used, try again.")
		elif guess not in keyword:
			print("\nWrong!")
			guesses += guess
			turns -= 1
			if turns == 0:
				print("You have no more guesses left. You lose!")
			else:
				print("You have", + turns, 'more guesses.')
		else:
			print("\nCorrect!")
			guesses += guess
			turns += 1
			print("Extra guess has been awarded!")
			print("Number of incorrect guesses left:", +turns)

if __name__ == "__main__":
    play_game() 