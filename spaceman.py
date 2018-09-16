#test null characters, end of file characters
#ASCII credit to respective artists at textart.io

import random
#Need to import dictionary (spell check dictionary?)
#include error handling into each function

#def pick_category():
# dependent on whether or not can find dictionary with categories
# UPDATE: Taken out due to not finding a dictionary file separated by category

def generate_word():
# Pick random word from dictionary
    generated = open('words_alpha.txt', 'r')
    generate_list = []
    for line in generated:
        generate_list.append(line.strip('\n'))
    return random.choice(generate_list)

def unscramble_word(guess, secret_word, scrambled_word):
# If correct guess, unscramble associated letter
# Make exceptions for spaces. Auto revealed
    for i in range(0, len(secret_word)):
        if secret_word[i] == guess:
            scrambled_word[i] = guess

def make_a_guess():
# Guess the whole word. If matches, win condition activates
    whole_word_guess = input("What is your guess at the word?")
    return whole_word_guess   

def check_guess(guess, guessed_letters, scrambled_word, secret_word):
# Prompts user input with error handling for letters used and multiple letters. Checks if letters or guess is correct
    if guess.isalpha() and len(guess) == 1:
        if guess in guessed_letters:
            print("You already guessed that letter")      
            return False
        else:
            if guess not in secret_word:
                return False
            else:
                return True
    elif len(guess) != 1:
        return False
    else:
        return False
        
def win_condition(scrambled_word, secret_word):
# If no * then win
# Elif make_a_guess == generated word, win 
   #if str(scrambled_word) == secret_word:
    if str(''.join(scrambled_word)) == secret_word:
        print("                           *     .--.")
        print("                                / /  `")
        print("               +               | |")
        print("                      '         \ \__,")
        print("                  *          +   '--'  *")
        print("                      +   /\ ")
        print("         +              .'  '.   *")
        print("                *      /======\      +")
        print("                      ;:.  _   ;")
        print("                      |:. (_)  |")
        print("                      |:.  _   |")
        print("            +         |:. (_)  |          *")
        print("                      ;:.      ;")
        print("                    .' \:.    / `.")
        print("                   / .-'':._.'`-. \ ")
        print("                   |/    /||\    \|")
        print("                 _..-----````-----.._")
        print("           _.-'``                    ``'-._")
        print("         -'            You Win!            '-")
        return True  
    return False

def lose_condition(lives):
# if guessed letter incorrect, print ascii pt1, 2, etc. if * = len(word) - 1 , display this
#if part 7 ascii graphics plays then lose
    if lives == 7:
        print("                    /\ ")
        print("                   //\\\ ")
        print("                  ||##||")
        print("                 //##mm\\\ ")
        print("                //##*mmm\\\ ")
        print("               //###**mmm\\\ ")
        print("              //###***nmmm\\\ ")
        print("             //####***@nmmm\\\ ")
        print("             ||####***@nnmm||")
        print("             ||####**@@@nnm||")
        print("             |______________|")
        print("             |    Krogg97   |")
        print("              \____________/")
        print("               |          |")
        print("              /|    /\    |\ ")
        print("             /_|    || /\ |_\ ")
        print("               |      NUSA|")
        print("               |       \/ |")
        print("               |          |")
        print("              /|    /\    |\ ")
        print("             / |    ||    | \ ")
        print("            /  |    ||    |  \ ")
        print("           /  /\    ||    /\  \ ")
        print("          |__/  \   ||   /  \__|")
        print("            /____\      /____\ ")
        print("            |    |      |    |")
        print("            |    |______|    |")
        print("            |    | /--\ |    |")
        print("            |____|/----\|____|")    

    elif lives == 6:
        print("           /\ ")
        print("          /  \ ")
        print("         /^^^^\ ")
        print("         |----|")
        print("         /    \ ")
        print("        (|(||)|)")
        print("         |^^^^|")
        print("         /----\ ")
        print("        /      \ ")
        print("       /        \ ")
        print("    O-[{[[||||]]}]-O")
        print("      /|        |\ ")
        print("     / |        | \ ")
        print("    /  |        |  \ ")
        print("   / -[{[[||||]]}]- \ ")
        print("  /####|        |####\ ")
        print(" / I ^ /(::::::)\ ^ I \ ")
        print("^--____{|!....!|}____--^")
        print("       /--------\ ")
        print("      /_|######|_\ ")
        print("    Budget Cuts x 1")

    elif lives == 5:
        print("             .")
        print("           .d$ .")
        print("           d$$  :")
        print("          .$$$")
        print("          :$$$   :")
        print("          $$$$   :")
        print("          $$$$   :")
        print("         .$$$$")
        print("         :$$$$    :")
        print("         :$$$$    :")
        print("         $$$$$    :")
        print("         $$$$$    :")
        print("         :    $$$$$")
        print("         :    $$$$$")
        print("         :    $$$$$")
        print("        .:    $$$$$.")
        print("       / :    $$$$: \ ")
        print("      /  :    $$$$:  \ ")
        print("     '        $$$$`   '")
        print("     |    :   $$$$    |")
        print("     |   /:   $$$$\   |")
        print("     |  /     $$$` \  |")
        print("     |_/   :__$$P   \_|")
        print("       Budget Cuts x2")

    elif lives == 4:
        print("       !")
        print("       !")
        print("       ^")
        print("      / \ ")
        print("     /___\ ")
        print("    |=   =|")
        print("    |     |")
        print("    |     |")
        print("    |     |")
        print("    |     |")
        print("    |     |")
        print("    |     |")
        print("    |     |")
        print("    |     |")
        print("    |     |")
        print("   /|##!##|\ ")
        print("  / |##!##| \ ")
        print(" /  |##!##|  \ ")
        print("|  / ^ | ^ \  |")
        print("| /         \ |")
        print("|/           \|")
        print("Budget Cuts x3")

    elif lives == 3:
        print("         /\ ")
        print("        |==|")
        print("        |  |")
        print("        |  |")
        print("        |  |")
        print("       /____\ ")
        print("       |    |")
        print("       |tre |")
        print("       |  IX|")
        print("       |    |")
        print("      /| |  |\ ")
        print("     / | |  | \ ")
        print("    /__|_|__|__\ ")
        print("       /_\/_\ ")
        print("  Budget Cuts x4") 

    elif lives == 2:
        print("        |")
        print("       / \ ")
        print("      / _ \ ")
        print("     |.o '.|")
        print("     |'._.'|")
        print("     |     |")
        print("   ,'|  |  |`.")
        print("  /  |  |  |  \ ")
        print("  |,-'--|--'-.| ")
        print(" Budget Cuts x5")

    elif lives == 1:
        print("      /\ ")
        print("     (  )")
        print("     (  )")
        print("    /|/\|\ ")
        print("   /_||||_\ ")
        print("Budget Critically Low!") 
    else:
        print("The mission has been cancelled. You lose")

def start_game():
    game_running = True
    lives = 7
    secret_word = generate_word()
    scrambled_word = list("*" * len(secret_word))
    guessed_letters = []

    print("You have " + str(lives) + " tries to make it into space. Best of luck!")
    print("The secret word has " + str(len(secret_word)) + " letters in it")
    #print(secret_word)
    
    while game_running and lives > 0:
        #Guess whole word at a time section

        guess = input("What letter would you like to guess? Type \"guess\" to guess the word ")
        print(scrambled_word)
        lose_condition(lives)
        print(secret_word)

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        if guess == "guess":
            guessed = make_a_guess()
            if win_condition(guessed, secret_word):
                game_running = False
            else:
                lives -= 1

        #Guess one letter at a time section

        else:
            valid_guess = check_guess(guess, guessed_letters, scrambled_word, secret_word)
            if not valid_guess:
                if len(guess) != 1:
                    print("Only one character at a time")
                elif guess.isalpha() == False:
                    print("I'm afraid that's not a letter I recognize")
                else:
                    guessed_letters.append(guess)
                    print(list(guessed_letters))
                    lives -= 1
            else:
                guessed_letters.append(guess)
                unscramble_word(guess, secret_word, scrambled_word)
                print(scrambled_word)
                print(list(guessed_letters))

                if win_condition(scrambled_word, secret_word):
                    game_running = False
        
        if lives <= 0:
            game_running = False
            lose_condition(lives)


start_game()