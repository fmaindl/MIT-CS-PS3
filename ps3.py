

import math
import random
import string

VOWELS = 'aeiou*'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
LETTER=VOWELS+CONSONANTS

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}


    


        

def highscores_display(highscores):
    
    
    from collections import OrderedDict
    highscores_update=OrderedDict(sorted(highscores.items(), key=lambda x: x[1], reverse=True))
    print("Here are the current highscores...:\n")    
    for i in highscores_update:
        print(i, highscores_update[i])
    return highscores_update
        

import json
from operator import itemgetter
try:
    highscores=json.load(open("highscores.txt"))
except:
    highscores={}
highscores_display(highscores)


WORDLIST_FILENAME = "words.txt"

def load_words():

    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):

    
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	



def get_word_score(word, n):
   
    a=0
    b=0
    
    for i in (word.lower()):
        a+=SCRABBLE_LETTER_VALUES[i]
    
    if 7*len(word)-3*(n-len(word)) > 1:
        b=7*len(word)-3*(n-len(word))
    else:
        b=1
    return a*b
    


def display_hand(hand):
  
    
        for i in hand.keys():                        
            for j in range(hand[i]):
                print(i, end=' ')      
        print()


def deal_hand(n):

    
    hand={}
    num_vowels = int(math.ceil(n / 3))
    
    
    
    
    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    if "*" not in hand.keys() or hand["*"] > 1:
        return deal_hand(n)
        
        
            
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand


def update_hand(hand, word):
    
    
    hand_clone=hand.copy()
    
    if word == "!!":
        return 0
    elif len(word) <= sum(hand.values()):
        for i in word.lower():
            if i in hand.keys() and hand[i] > 0:
                hand_clone[i]=hand_clone.get(i, 0) - 1                                   
        return hand_clone
                
    else:
        print("Oopsy Doopsy, there are too many letters in there...")
        for i in hand_clone:
            hand_clone[i]= 0
        return hand_clone


def is_valid_word(word, hand, word_list):

    VOWELS = list('aeiou')
    hand_clone=hand.copy()
    wildcardtest=list(word.lower())
    
    
    if len(word) > sum(hand.values()):
        return False
    else:
        if word.lower() in word_list:
            for i in word.lower():
                if i not in hand_clone:
                    return False
                elif hand_clone[i] == 0:
                    return False
                else:
                    hand_clone[i]=hand_clone.get(i, 0) - 1                         
            return True
        else:
            if "*" in word:
                for i in range(len(wildcardtest)):
                    if wildcardtest[i] == "*":
                        for j in range(0,5): 
                            wildcardtest[i] = VOWELS[j]
                            if (''.join(wildcardtest)) in word_list:
                                return True
                else:
                    return False
            else:
                 return False




def calculate_handlen(hand):
 
    
    return sum(hand.values())
    
 
def play_hand(hand, word_list):

    total_word_score=0
    stop=0
    
    while calculate_handlen(hand) > 0:
        print("Current Hand: ", end=' '), display_hand(hand)
        word=str(input("Enter word, or '!!' to indicate that you "
                   "are finished:"))               
        if word == "!!":            
            print("Alright... Total score for this round: ", total_word_score)            
            stop=1
            break                       
        elif is_valid_word(word, hand, word_list) == True:
            hand=update_hand(hand, word)
            total_word_score+=get_word_score(word, n)
            print(word, "earned", get_word_score(word, n), "points. Total:", total_word_score, " points.")
        else:
            hand=update_hand(hand, word)
            print("That is not a valid word. Please choose another word.")
    if stop == 1:
        return total_word_score
    else:
        print("Ran out of letters I see... Total score for this round is: ", total_word_score, " points.")
        return total_word_score
            
         





def substitute_hand(hand, letter):

    hand_clone=hand.copy()
    x=random.choice(LETTER)    
    
    if letter in hand.keys() and hand[letter] > 0:        
        hand_clone[letter]=hand_clone.get(letter, 0) - 1    
        hand_clone[x] = hand_clone.get(x, 0) + 1
        return hand_clone
    else:
        return hand_clone
    
        

       
    
def play_game(word_list):
#
#    Allow the user to play a series of hands
#
#    * Asks the user to input a total number of hands
#
#    * Accumulates the score for each hand into a total score for the 
#      entire series
# 
#    * For each hand, before playing, ask the user if they want to substitute
#      one letter for another. If the user inputs 'yes', prompt them for their
#      desired letter. This can only be done once during the game. Once the
#      substitue option is used, the user should not be asked if they want to
#      substitute letters in the future.
#
#    * For each hand, ask the user if they would like to replay the hand.
#      If the user inputs 'yes', they will replay the hand and keep 
#      the better of the two scores for that hand.  This can only be done once 
#      during the game. Once the replay option is used, the user should not
#      be asked if they want to replay future hands. Replaying the hand does
#      not count as one of the total number of hands the user initially
#      wanted to play.
#
#            * Note: if you replay a hand, you do not get the option to substitute
#                    a letter - you must play whatever hand you just had.
#      
#    * Returns the total score for the series of hands

    number_of_games=int(input("Please enter the number of hands you want to play: "))
    ini_number_of_games=number_of_games
    Total_score=0
    
    while number_of_games > 0:
        hand=deal_hand(n)
        print("Current Hand: ", end=' '), display_hand(hand)
        yes_or_no=str(input("Would you like to substitute a letter? "))
        if yes_or_no == "yes":
            what_letter=str(input("What letter would you like to replace: "))
            hand2=substitute_hand(hand, what_letter)            
            x=play_hand(hand2, word_list)
            retry=str(input("Would you like to replay this hand? "))
            if retry == "yes":
                x=play_hand(hand2, word_list)
                number_of_games-=1
                Total_score+=x
            else:
                number_of_games-=1
                Total_score+=x
        elif yes_or_no != "yes":           
            x=play_hand(hand, word_list)
            retry=str(input("Would you like to replay this hand? "))
            if retry == "yes":
                x=play_hand(hand, word_list)
                number_of_games-=1
                Total_score+=x
            else:
                number_of_games-=1
                Total_score+=x                     
    print("Your total score is", Total_score/ini_number_of_games/n, " points per letter.")
    name=str(input("Please enter your name "))
    if name not in highscores:
        highscores[name]=Total_score/ini_number_of_games/n
        print("Your current highscore is:", Total_score/ini_number_of_games/n,"\n\n")
    elif name in highscores and Total_score/ini_number_of_games/n > highscores[name]:
        print("Congratulations", name, "you have a new highscore!\n")
        highscores[name]=Total_score/ini_number_of_games/n
        print("You new highscore is", Total_score/ini_number_of_games/n)
    highscores_display(highscores)
    json.dump(highscores, open("highscores.txt",'w'))

n=8
                
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
