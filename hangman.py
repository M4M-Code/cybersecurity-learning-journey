import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
def pick_word():
    with open("words.txt", "r") as file:
        hangman = file.readlines()
        hangman = [word.strip() for word in hangman]
    return random.choice(hangman)
ran_hangman = pick_word()


emptiness = ["_"] * len(ran_hangman)
print(" ".join(emptiness))
lives = 6
def show_state(lives, emptiness):
    print(HANGMANPICS[6 - lives])
    print("\n", " ".join(emptiness))
    print(f"\nyou have {lives} more tries")



guess_letter = []
def play():
    ran_hangman = pick_word()
    emptiness = ["_"] * len(ran_hangman)
    lives = 6
    guess_letter = []
    
    print(HANGMANPICS[0])
    print(" ".join(emptiness))

    while "_" in  emptiness and lives > 0:
        guess = input("please guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guess_letter:
                print("You guessed that before.")
                print(f"you have {lives} more trise")
                continue
            guess_letter.append(guess)
            if guess not in ran_hangman:
                lives -= 1
                
            
            for x in range(len(ran_hangman)):
                if ran_hangman[x] == guess:
                    emptiness[x] = guess
            show_state(lives, emptiness)
        else:
            print("❌ Error! Please enter exactly ONE alphabetic character (No numbers, symbols, or multiple letters).")

        
    if lives == 0:
        print("""
        **********
        YOU LOSE
        **********""")
    
    else:
        print("""
        **********
        YOU WIN!
        **********""")
        print("The word is ",ran_hangman)

play()