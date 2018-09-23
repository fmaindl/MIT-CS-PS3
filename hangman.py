
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
 
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
#    print("  ", len(wordlist), "words loaded.")
    return wordlist




def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



def is_word_guessed(secret_word, letters_guessed):


    if set(letters_guessed).issuperset(set(secret_word)) == True:
        print("Woohoo you won! The word was", secret_word_display,"!")
        return True
    else: 
        return False
        
     
            



def get_guessed_word(secret_word, letters_guessed):
  
    
    guessed_word=secret_word[:]
#
    
    for i in range(len(secret_word)):
        if guessed_word[i] not in letters_guessed:
            guessed_word[i] = "_"
    return guessed_word
            

def get_available_letters(letters_guessed):
    
    
    all_letters="abcdefghijklmnopqrstuvwxyz"
    all_letters_list=list(all_letters)
    
    
    for i in letters_guessed:
        if i in all_letters_list:
            all_letters_list.remove(i)
    return all_letters_list
    



def hangman(secret_word):
    
    guesses=6
    oops_counter=3
    print("Welcome to the game of Hangman!\nI am thinking of a word that is",
          len(secret_word), "letters long\n----------\nYou have", guesses,"guesses left.\n"
          "Available letters:", get_available_letters(letters_guessed))
    
    while is_word_guessed(secret_word, letters_guessed) == False:
        x=str(input("Please guess a letter:"))
        y=(x.lower())
        z=list(y)
        if z[0] in secret_word and z[0] not in letters_guessed:
            letters_guessed.append(z[0])
            print("Good guess:", " ".join(get_guessed_word(secret_word, letters_guessed)),
            "\nYou have", guesses, "guesses remaining.\n-----------------------"
            "\nAvailable letters:", get_available_letters(letters_guessed))
#                                        
        elif z[0] in secret_word and z[0] in letters_guessed and oops_counter > 0:
            print("Oops... you already guessed that letter...I give you", (oops_counter-1)," more"
                  " warnings\nAvailable letters:", get_available_letters(letters_guessed),
                  "\nThe word is:", " ".join(get_guessed_word(secret_word, letters_guessed)))
            oops_counter-=1
        elif z[0] not in list("abcdefghijklmnopqrstuvwxyz") and oops_counter > 0:
            print("Oops! That is not a letter. I give you", (oops_counter-1)," more"
                  " warnings\nAvailable letters:", get_available_letters(letters_guessed),
                  "\nThe word is:", " ".join(get_guessed_word(secret_word, letters_guessed)))
            oops_counter-=1
        elif z[0] in list("abcdefghijklmnopqrstuvwxyz"):
            letters_guessed.append(z[0])
            guesses-=1
            if guesses == 0:
                print("Oh... seems like you are out of luck... The word was", 
                      secret_word_display,"Better luck next time...")
                break
            else:
                print("Oopsy-doodles!, that is not in the word! You have", guesses,
                      "guesses remaining.\n---------------------\n"
                      "Available letters:", get_available_letters(letters_guessed),
                         "\nThe word is:", " ".join(get_guessed_word(secret_word, letters_guessed)))
        else:
            guesses-=1
            if guesses == 0:
                print("Oh... seems like you are out of luck... The word was", 
                      secret_word_display,"Better luck next time...")
                break
            else:
                print("Oopsy-doodles!, that is not in the word! You have", guesses,
                      "guesses remaining.\n---------------------\n"
                      "Available letters:", get_available_letters(letters_guessed),
                         "\nThe word is:", " ".join(get_guessed_word(secret_word, letters_guessed)))
    
            
        
            
            

        


wordlist=load_words()
#secret_word=["f","a","r", "t"]
#secret_word_display=choose_word(wordlist)
secret_word_display="because"
secret_word=list(secret_word_display)

letters_guessed=list()
x=(is_word_guessed(secret_word, letters_guessed))
guessed_word1=" ".join(get_guessed_word(secret_word, letters_guessed))
available_letters=get_available_letters(letters_guessed)
guesses=6
hangman (secret_word)






# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



#def match_with_gaps(my_word, other_word):
#    '''
#    my_word: string with _ characters, current guess of secret word
#    other_word: string, regular English word
#    returns: boolean, True if all the actual letters of my_word match the 
#        corresponding letters of other_word, or the letter is the special symbol
#        _ , and my_word and other_word are of the same length;
#        False otherwise: 
#    '''
#    # FILL IN YOUR CODE HERE AND DELETE "pass"
#    pass
#
#
#
#def show_possible_matches(my_word):
#    '''
#    my_word: string with _ characters, current guess of secret word
#    returns: nothing, but should print out every word in wordlist that matches my_word
#             Keep in mind that in hangman when a letter is guessed, all the positions
#             at which that letter occurs in the secret word are revealed.
#             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
#             that has already been revealed.
#
#    '''
#    # FILL IN YOUR CODE HERE AND DELETE "pass"
#    pass
#
#
#
#def hangman_with_hints(secret_word):
#    '''
#    secret_word: string, the secret word to guess.
#    
#    Starts up an interactive game of Hangman.
#    
#    * At the start of the game, let the user know how many 
#      letters the secret_word contains and how many guesses s/he starts with.
#      
#    * The user should start with 6 guesses
#    
#    * Before each round, you should display to the user how many guesses
#      s/he has left and the letters that the user has not yet guessed.
#    
#    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
#      
#    * The user should receive feedback immediately after each guess 
#      about whether their guess appears in the computer's word.
#
#    * After each guess, you should display to the user the 
#      partially guessed word so far.
#      
#    * If the guess is the symbol *, print out all words in wordlist that
#      matches the current guessed word. 
#    
#    Follows the other limitations detailed in the problem write-up.
#    '''
#    # FILL IN YOUR CODE HERE AND DELETE "pass"
#    pass
#
#
#
## When you've completed your hangman_with_hint function, comment the two similar
## lines above that were used to run the hangman function, and then uncomment
## these two lines and run this file to test!
## Hint: You might want to pick your own secret_word while you're testing.
#
#
#if __name__ == "__main__":
#    # pass
#
#    # To test part 2, comment out the pass line above and
#    # uncomment the following two lines.
#    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)
#
################
#    
#    # To test part 3 re-comment out the above lines and 
#    # uncomment the following two lines. 
#    
#    #secret_word = choose_word(wordlist)
#    #hangman_with_hints(secret_word)