

import random

def guess(user):
    c=random.sample(user,5) ##Selects 5 words in a list
    return c


def compare(c,x):#Checks whether the word selected by the user matches with any of the computer selected words
    if x in c:
        return 2 ##user scores 2 if the word is in the computer selected words
    elif x not in c:
        return 0 ##user scores 0 if the word is absent



def choose_word(): ##Randomly selects a word
    words=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday","january",\
           "february", "march", "april", "may", "june", "july", "august", "september", "october", \
           "november", "december","michael", "mango", "banana", "apple", "sciece", "programming",\
           "computer","data","william", "jewell", "random", "eugene", "project",]
    d=random.choice(words)
    return d

def status(word_to_guess, guessed_letters): ##Takes in the word to guess(word chosen by the computer
    display=" " ##A variable and an empty string to store user inputs and also to display the computer selected word
    for letter in word_to_guess:
        if lette  0r in guessed_letters:
            display=display+letter ##Adds a new letter to the display variable if the letter is in the computer selected word
        else:
            display=display+" "+ "_" ##Adds underscores if the letter is  still not present in the computer selected word
    return display ##stores the new value of display for later use



