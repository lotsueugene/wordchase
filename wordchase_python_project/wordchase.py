from wordchase_module import *

print("Name: Eugene Lotsu")

categories = {
    "days_of_week(A)": ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"],
    "months_of_year(B)": ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"],
    "artists_in_ghana(C)": ["sarkodie", "shatta wale", "stonebwoy", "eazzy", "mzvee", "kuami eugene", "joey b"],
    "seasons(D)": ["Spring", "Summer", "Autumn", "Winter"]
}

mode = int(input('''Select your preferred level of difficulty
            1. Easy
            2. Hard (Input the corresponding numbers. e.g. 1): '''))  ## THIS PART ALLOWS USER TO SELECT PREFERRED GAME DIFFICULTY

print('''      <---Let's GO!--->

''')  ## PROMPTS THE USER THAT THE GAME IS ABOUT TO START AND ADDS BEAUTY TO MY GAME

new_list = []  ## STORES LIST FROM IF STATEMENTS

if mode == 1:  ## Easy Mode
    print('''For Level 1, you will be required to select categories of words to guess a randomly selected word. Select From Below!

    ''')
    for key in categories:
        print(f"{key}: {categories[key]}")  ## PRINTS OUT THE KEYS AND VALUES OF THE CATEGORIES
    user = input('''Select at least 2 items from the categories (e.g., AB): ''')  ## GETS AN INPUT FROM THE USER

    if "A" in user:
        new_list.extend(categories["days_of_week(A)"])  ## adds a list to new_list=[]
    if "B" in user:
        new_list.extend(categories["months_of_year(B)"])  ## adds a list to new_list=[]
    if "C" in user:
        new_list.extend(categories["artists_in_ghana(C)"])  ## adds a list to new_list=[]
    if "D" in user:
        new_list.extend(categories["seasons(D)"])  ## adds a list to new_list=[]
        
    comp_list = []
    for lists in new_list:
        comp_list.append([lists])  ## Puts the new_list in another list to enable me to access words in the list
    
    with open("guess.txt", "w") as f:  ## Using 'with' ensures the file is automatically closed
        for word in new_list:
            f.write("\n" + str(word))  ## Writes the selected word into a txt file
    
    print('''


        <--Your selected categories have been stored in a file called 'guess.txt' on your local computer-->
                              <----USE AS REFERENCE!---->

    ''')  ## Informs user about the file location of the selected categories

    tries = 10 ##Ensures that the user has 10 tries
    wins = 0 ##Tracks wins
    score = 0 ##Tracks scores for each round 
    total_score = 0 ##Tracks total score at the end of the game
    game_count=0 ##Counts the number of games played
    while tries > 0: ##User is asked to guess word 10 times.
        player = input('''Select any word from your selected categories.
            2 points for guessing the same word as the COMPUTER! ZERO(0) for a WRONGLY guessed word: ''').lower()
        selected_word = [player]
        game = guess(comp_list) ##Inserts a list and fetchs a randomly selected list from the "wordchase" module
        counted = compare(game, selected_word) ##Fetchs scores from the "wordchase" module
        score =score+counted ##Tracks scores for each round 
        tries =tries-1 ##tracks tries
        game_count=game_count+1
        print(f'''You selected: {selected_word}
          Computer chose: {game}''') ##Displays user's choice and computer's choice to user
        print(f"Your score is: {score}")##Displays scores to user
        print(f"Remaining tries: {tries}")##Displays remaining tries to user
        print('''
                                        ''')##Adds space to the code when displayed
        if counted == 2:
            wins=wins+1
            play_again=input('''Do you want to play again?
                            Type: Y for YES or N for NO: ''')##Gives the user the option to continue or stop the game
       
            if play_again=="N": ##Stops the game if user's response is NO
                tries=0
                print("GAME OVER!")
           
       
            

    total_score=total_score+score ##Tracks total score at the end of the game
    print(f"Your Total score is: {total_score}")
    print(f"Out of {game_count} games you had: {wins} win(s)")

elif mode == 2:  ## Hard Mode
    print("Word Guessing Game")
    print("*************")
    guessed_letters=[]##Stores the letters guessed by the user
    secret_word = choose_word()

    print("Secret Word:", status(secret_word, guessed_letters))##This code prints out the lenth of the word to be guessed in an underscore format

    attempts = 7 ##Gives the user 7 attempts to get it right
    while attempts > 0: ##Code runs as long as the number of attempts is greater than zero
        guess = input("Guess A Letter: ").lower() ##Takes alphabetical inputs from user and converts to a lowercase 
        
        if len(guess) != 1: ##Prompts the user to input just one letter
            print("You must enter a single letter!")
            guess = input("Guess A Letter: ").lower()
        
        if guess in guessed_letters:
            print("You have already guessed that letter.") ##Prompts the user to input a new letter because the previous input is in the list
            guess = input("Guess A Letter: ").lower()

        guessed_letters.append(guess) ##adds new letter to  guessed_letters=[]

        if guess not in secret_word:
            attempts = attempts - 1 ##number of attempts reduces after every wrong guess
            print(f"{guess} does not occur in word!")
            print(f"You have {attempts} attempts remaining")##Displays the number of attempts left
        else:
            occurrences=secret_word.count(guess) ##Counts the number of times the letter appears in the list(if it's in the selected word)
            print(f"Letter '{guess}' occurs {occurrences} times.")

        current_status = status(secret_word, guessed_letters)##From the status module, it helps to print out the new status of the word
        print("Secret Word: ", current_status)

        if "_" not in current_status: ##Runs  if there's no underscore in current_status
            print("Congratulations! You guessed the word.")
            
            user = input('''Do you want to play again?
                        Input Y for YES and N for NO: ''') #...

    if "_" in current_status: ##This code runs after the user uses the total number of attempts. If an underscore is still present, it gives the user the option to play again
        print(f"You run out of attempts! The word was {secret_word}")##displays the word

    user = input('''Do you want to play again?
                    Input Y for YES and N for NO: ''') ##...
    if user == "N":
        attempts=0
        print("Thank You for playing")
            
        
       
