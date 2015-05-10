import mystery_word
import random

def word_len_input():
    """Asks user for the length of word they want to play the game."""
    word_length = int(input("Choose a word length: "))
    for word in my_list:
        if len(word) == word_length:
            return word_length
    print("Invalid input. Try again.")
    return word_len_input()

def num_guess_input():
    """Asks user for number of guesses they want to solve the word."""
    number_of_guesses = int(input("Choose the number of guesses: (1 - 26):  "))
    while number_of_guesses < 1 or number_of_guesses > 27:
        print("Invalid input. Try again.")
        number_of_guesses = int(input("Choose the number of guesses: (1 - 26):  "))
    return number_of_guesses

def list_of_words(my_list, word_len_input):
    """Takes a full list of words and returns separate list of words with
       the length of words user wants to play with."""
    words_list = []
    for word in my_list:
        if len(word) == word_len_input:
            words_list.append(word)
    return words_list

def guess_letter():
    """Asks user to guess a letter and returns the letter upper case."""
    guess = input("Guess a letter: ")
    while True:
        if not(guess.isalpha()):
            print("Invalid input. Try again.")
            guess = input("Guess a letter: ")
        elif len(guess) != 1:
            print("Invalid input. Only one letter please.")
            guess = input("Guess a letter: ")
        else:
            break
    return guess.upper()


def cat_dict(a_list, letter):
    """Categorizes the list by the appearance of the letter in the word.
       Returns the modified dictionary"""
    mod_dict = {}
    for word in a_list:
        display = mystery_word.display_word(word, letter)
        if display in mod_dict:
            mod_dict[display].append(word)
        else:
            mod_dict[display] = [word]
    return mod_dict

def most_words_list(my_dict):
    """Takes a dictionary and returns the value that has most items in
       the list."""
    max_count = 0
    count = 0
    most_words = []
    for key, value in my_dict.items():
        count = len(my_dict[key])
        if count > max_count:
            max_count = count
            most_words = value
    return most_words

if __name__ == "__main__":
    my_list = (mystery_word.read_file("dictionary.txt")) #reads list of words(CAPS) from the file
    word_length = word_len_input() #gets length of word user wants to play
    num_guesses = num_guess_input() #gets number of guesses user wants to solve the word
    modified_list = (list_of_words(my_list, word_length)) #seperates words to user input
    guesses = ""

    while num_guesses > 0:
        num_guesses -= 1
        guess = guess_letter()
        while guess in guesses:
            print("You already guessed that word. Try again.")
            guess = input("\nGuess a letter: ").upper()
        guesses += guess
        my_dict = cat_dict(modified_list, guess)
        most_words = (most_words_list(my_dict))
        modified_list = most_words
        #print(most_words)
        display = mystery_word.display_word(most_words[0], guesses)
        print(display)

        if guess in most_words[0]:
            num_guesses += 1

        if (mystery_word.is_word_complete(most_words[0], guesses)):
            print("You win!")
            break
        elif num_guesses == 0:
            print("Sorry, you lose!")
            print("{} is the mystery word.".format(most_words[0]))
        else:
            print("{} turns left.".format(num_guesses))
