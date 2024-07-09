from ConsoleGames import number_guesser, word_guesser, hangman, rock_paper_scissors

def run_game(game_function):
    game_function() 

def main():
    
    try: 
        while True:
        
            print("\n")
            print(" ====================================")
            print("| WELCOME TO THE CONSOLE GAME LIBRARY |")
            print(" ====================================")
            print("\n")
            print("Choose a game to play:")
            print("\n1. Number Guesser")
            print("2. Word Guesser")
            print("3. Hangman")
            print("4. Rock/Paper/Scissors\n")
            
            choice = 0
            while True:
                try:
                    choice = int(input("\nEnter your choice (1-4), or 0 to exit: "))
                    if choice == 0:
                        print("\nGoodbye!")
                        exit()
                    elif choice not in switch:
                        print("\nPlease enter a valid choice (1-4 or 0): ")
                    else:
                        switch[choice]()  # Run the game
                        break
                except ValueError:
                    print("\nInvalid value. Please enter a valid integer.")
            
            while True: 
                playAgain = str(input("\nPlay again? (y/n): "))
                if playAgain.lower() == "y": 
                    switch[choice]()
                else: 
                    anotherGame = str(input("\nDo you want to try another game? (y/n): "))
                    if anotherGame.lower() == "y": main()
                    else: switch[0]()
                        
    except KeyboardInterrupt: 
        print() 
        print('\nThe game was interrupted by the user.\nGoodbye!') 
        exit()

def caseExit():
    print()
    print("Thanks for playing.\nGoodbye!")
    exit()

def caseNumberGuesser():
    run_game(number_guesser.play_game)

def caseWordGuesser():
    run_game(word_guesser.play_game)

def caseHangman():
    run_game(hangman.play_game)
    
def caseRockPaperScissors():
    run_game(rock_paper_scissors.play_game)
    
switch = {
    0: caseExit,
    1: caseNumberGuesser,
    2: caseWordGuesser,
    3: caseHangman,
    4: caseRockPaperScissors
}

if __name__ == "__main__":
    main() 
