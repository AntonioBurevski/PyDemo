import random
import math

def play_game():

    print("\n")
    print("------------------------------------------")
    print("\tN U M B E R  G U E S S E R")
    print("------------------------------------------")
        
    attempts = 0
    
    print("\n")
    print("Enter your desired range.")
    while True:
        try:
            lower_bound = int(input("Lower Bound: "))
            upper_bound = int(input("Upper Bound: "))
            break
        except ValueError:
            print("\nInvalid value. Please enter a valid integer.\n")
    
    print("\n")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}. Can you guess it?")

    minimum_guesses = round(math.log(upper_bound - lower_bound + 1, 2))
    
    print("\n")
    print(f"Careful, you only have {minimum_guesses} guesses")
    
    secret_answer = random.randint(lower_bound, upper_bound)
    
    while attempts < minimum_guesses:
        
        print("\n")
        
        correct_guess = False
        
        while True:
            try:
                guess = int(input("Enter your guess: "))
                break
            except ValueError:
               print("\nInvalid value. Please enter a valid integer.\n") 
        
        attempts += 1

        if guess < secret_answer:
            print("\tToo low. Try again.")
        elif guess > secret_answer:
            print("\tToo high. Try again.")
        else:
            print(f"\nCongratulations! You guessed the number in {attempts} attempts.")
            correct_guess = True
            break
        
    if attempts >= minimum_guesses and not correct_guess:
        print("\nThe number is %d" % secret_answer)
        print("Better Luck Next time!")
    
if __name__ == "__main__":
    play_game() 