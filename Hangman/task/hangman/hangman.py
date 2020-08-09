# Write your code here
from random import shuffle
from string import ascii_lowercase

possible_words = ['python', 'java', 'kotlin', 'javascript']


def hangman():
    shuffle(possible_words)
    word_to_guess = possible_words[0]
    letters = set(word_to_guess)
    used_letters = set()
    charted_word = '-' * len(word_to_guess)
    i = 0
    while i < 8:
        print()
        print(charted_word)
        if "-" not in charted_word:
            print(f"You guessed the word {word_to_guess}!")
            print("You survived!")
            break
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
        elif letter not in ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        elif letter in used_letters:
            print("You already typed this letter")
        elif letter not in letters:
            used_letters.add(letter)
            print("No such letter in the word")
            i += 1
        else:
            for j in range(len(word_to_guess)):
                if word_to_guess[j] == letter:
                    used_letters.add(letter)
                    charted_word = charted_word[:j] + letter + charted_word[j+1:]
    if i == 8:
        print("You are hanged!")


print("H A N G M A N")
while True:
    player_choice = input('Type "play" to play the game, "exit" to quit: ')
    if player_choice == "play":
        hangman()
    elif player_choice == "exit":
        break
