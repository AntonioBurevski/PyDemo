import random

def play_game(): 
    
    availableWords = ['apple', 'banana', 'mango', 'strawberry',  
                      'orange', 'grape', 'pineapple', 'apricot', 
                      'lemon', 'coconut', 'watermelon', 'cherry', 
                      'papaya', 'berry', 'peach', 'lychee', 'muskmelon'] 

    keyword = random.choice(availableWords)
    turns = len(keyword) + 2

    print("\n")
    print("------------------------------")
    print("\tH A N G M A N")
    print("------------------------------")
    print("\n1.\tGuess individual characters, or go for the whole word.")
    print("2.\tIf a character has already been guessed, the turn resets.")
    print("3.\tYou only have", +turns, "tries to get the whole word.")
    print()
    
    initalEmptyWord = ''
    for i in keyword:
        initalEmptyWord += '_ '
    
    print(f"\nCan you guess the {len(keyword)} character word I'm thinking of?\t{initalEmptyWord}")
    print("\nHINT! It's a name of a fruit.")
    print()
    
    lettersGuessed = '' 
    gameState = 0 # 0 - In progress 
                  # 1 - Won
                  # 2 - Lost
 
    while (turns != 0) and gameState == 0: 
            
        print() 
 
        guess = str(input('Guess a letter, or try to guess the whole word: ')) 
              
        if not guess.isalpha(): 
            print('Enter only letters!') 
            continue
            
        if len(guess) > 1: 
            processed_input = guess.lower().replace(" ", "")
            if processed_input == keyword:
                gameState = 1
                print("\tYour guess is correct!")
            else:
                turns -= 1
                if turns == 0:
                    gameState = 2
                    print("\tIncorrect guess, no turns remaining.")
                    break
                else:
                    print("\tIncorrect guess,", +turns, "turns remaining.")
                    continue
            
        failed = 0
            
        if guess in lettersGuessed: 
            print('\tYou have already guessed that letter.') 
            continue
        elif guess in keyword:
            turns -= 1
            lettersGuessed += guess 
            if turns == 0:
                print("\tCorrect, no turns remaining.")
            else:
                print("\tCorrect,", +turns, "turns remaining.")
        else:
            turns -= 1
            lettersGuessed += guess 
            if turns == 0:
                print("\tWrong, no turns remaining.")
            else:
                print("\tWrong,", +turns, "turns remaining.")
  
        print()
        for char in keyword: 
            if char in lettersGuessed: 
                print(char, end=' ') 
            else: 
                failed += 1
                print('_', end=' ')
        print("\n")
            
        if failed == 0: 
            gameState = 1
            break
        elif turns == 0 and failed > 0:
            gameState = 2
            break 
   
    if gameState == 1: 
        print() 
        print('You won!') 
        print('The word was {}.'.format(keyword))
    else:
        print() 
        print('You lost!') 
        print('The word was {}.'.format(keyword))
   
if __name__ == "__main__":
    play_game() 