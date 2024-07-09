import random

choiceMap = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

def play_game(): 
    
    print("\n")
    print("---------------------------------------------------")
    print("\tR O C K  P A P E R  S C I S S O R S")
    print("---------------------------------------------------")
    print('\nRules of the game ROCK PAPER SCISSORS are:\n'
      + "\tRock vs Paper -> Paper wins \n"
      + "\tRock vs Scissors -> Rock wins \n"
      + "\tPaper vs Scissors -> Scissor wins \n")
    print("\nGood luck!")
    print("\n")
    
    while True:
        
        print("Choose an option (1-3): ")
        
        try:
            userChoice = int(input("\n1. Rock \t2. Paper\t3. Scissors\n\nChoose: "))
            while userChoice > 3 and userChoice < 1:
                userChoice = int(input("Please enter a valid option: "))
        except ValueError:
            print("Please enter a number.")
            continue
        
        if userChoice in choiceMap:
            userChoiceName = choiceMap[userChoice]
        else:
            print("\nPlease enter a valid option.")
            continue
        
        print(f"\nUser choice is: {userChoiceName}")
        print("\nNow it's the computers turn...")
        
        computerChoice = random.randint(1, 3)
        computerChoiceName = choiceMap[computerChoice]
        
        print(f"\nThe computer chose {computerChoiceName}.\n")
        
        if userChoice == computerChoice:
            result = 'DRAW'
            print("==> Draw!\n", end="")
        elif (userChoice == 1 and computerChoice == 2):
            result = 'COMP'
            print("==> Paper wins!\n", end="")
        elif (userChoice == 1 and computerChoice == 3):
            result = 'USER'
            print("==> Rock wins!\n", end="")
        elif (userChoice == 2 and computerChoice == 1):
            result = 'USER'
            print("==> Paper wins!\n", end="")
        elif (userChoice == 2 and computerChoice == 3):
            result = 'COMP'
            print("==> Scissors wins!\n", end="")
        elif (userChoice == 3 and computerChoice == 1):
            result = 'COMP'
            print("==> Rock wins!\n", end="")
        elif (userChoice == 3 and computerChoice == 2):
            result = 'USER'
            print("==> Scissors wins!\n", end="")
            
        if result == 'DRAW':
            print("\n==> IT'S A TIE <==")
        elif result == 'USER':
            print("\n==> USER WINS <==")
        elif result == 'COMP':
            print("\n==> COMPUTER WINS <==")
        else:
            print("\n An error has occured while processing results.")
        
        break
            
if __name__ == "__main__":
    play_game() 