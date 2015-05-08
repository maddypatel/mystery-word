import random

def user_input():
    print ("Let's play \"Mystery Word\". You have 8 guesses to solve the word.")
    mode = input('\nChoose the game mode ("Easy, Normal or Hard"): ').lower()
    words_list = read_file("/usr/share/dict/words")

    if mode == "easy":
        words_list = easy_words(words_list)
    elif mode == "normal":
        words_list = medium_words(words_list)
    elif mode == "hard":
        words_list = hard_words(words_list)

    mystery = random_word(words_list)
    game(mystery)

def random_word(words_list):
    mystery = random.choice(words_list)
    return mystery

def game(mystery):
    turns = 8
    guesses = ""
    print("The mystery word has {} characters.".format(len(mystery)))
    while turns > 0:
        guess = input("\nGuess a letter: ").upper()
        while len(guess) != 1:
            print("Invalid input! Only one letter allowed.")
            guess = input("\nGuess a letter: ").upper()
        while guess in guesses:
            print("You already guesses that word. Try again.")
            guess = input("\nGuess a letter: ").upper()

        guesses += guess
        if guess in mystery:
            turns += 1

        print(display_word(mystery, guesses))
        turns -= 1
        print("\n{} turns left.".format(turns))

        if is_word_complete(mystery, guesses):
            print("\nYou win!")
            break
        elif turns == 0:
            print("\n{} is the mystery word".format(mystery))

    play_again = input("Play again? (Y or N): ").lower()
    if play_again == "y":
        user_input()

def display_word(mystery, guesses):
    user_guess = ""
    for char in mystery:
        if char in guesses:
            user_guess += char
        else:
            user_guess += "_"
    user_guess = " ".join(user_guess)
    return user_guess

def is_word_complete(mystery, guesses):
    missed = 0
    for char in mystery:
        if char not in guesses:
            missed += 1
    if missed == 0:
        return True

def read_file(input_file):
    with open(input_file) as file:
        lines = file.read().upper()
    lines = lines.split()
    return lines

def easy_words(my_list):
    easy_words_list = []
    for word in my_list:
        if len(word) >= 4 and len(word) <= 6:
            easy_words_list.append(word)
    return easy_words_list

def medium_words(my_list):
    medium_words_list = []
    for word in my_list:
        if len(word) >= 6 and len(word) <= 8:
            medium_words_list.append(word)
    return medium_words_list

def hard_words(my_list):
    hard_words_list = []
    for word in my_list:
        if len(word) >= 8:
            hard_words_list.append(word)
    return hard_words_list

if __name__ == "__main__":
    user_input()
