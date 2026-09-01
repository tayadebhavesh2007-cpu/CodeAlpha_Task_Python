"""
Hangman - a simple text-based word guessing game.

Rules:
  - The computer picks a random word from a small list.
  - You guess one letter at a time.
  - You are allowed 6 incorrect guesses.

Concepts used: random, while loop, if-else, strings, lists.
"""

import random

# ---- Game data ----------------------------------------------------------
WORDS = ["python", "keyboard", "monsoon", "guitar", "network"]
MAX_WRONG = 6


def build_display(secret, guessed):
    """Return the word with unguessed letters hidden, e.g. 'p _ t h _ n'."""
    shown = []
    for letter in secret:
        if letter in guessed:
            shown.append(letter)
        else:
            shown.append("_")
    return " ".join(shown)


def get_guess(guessed):
    """Ask the player for one new, valid letter and return it."""
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1:
            print("Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Letters only, please.")
        elif guess in guessed:
            print("You already tried '" + guess + "'. Pick another letter.")
        else:
            return guess


def play():
    secret = random.choice(WORDS)
    guessed = []      # every letter the player has tried
    wrong = 0         # number of incorrect guesses so far

    print("=" * 40)
    print("HANGMAN")
    print("The word has " + str(len(secret)) + " letters.")
    print("You can make " + str(MAX_WRONG) + " wrong guesses.")
    print("=" * 40)

    # Keep playing while lives remain and letters are still hidden.
    while wrong < MAX_WRONG and "_" in build_display(secret, guessed):
        print("\nWord:  " + build_display(secret, guessed))
        print("Wrong guesses left: " + str(MAX_WRONG - wrong))
        if guessed:
            print("Tried: " + ", ".join(sorted(guessed)))

        guess = get_guess(guessed)
        guessed.append(guess)

        if guess in secret:
            print("Correct! '" + guess + "' is in the word.")
        else:
            wrong += 1
            print("Nope, no '" + guess + "' in the word.")

    # ---- Game over ------------------------------------------------------
    print("\n" + "=" * 40)
    if wrong < MAX_WRONG:
        print("You win! The word was '" + secret + "'.")
        print("You used " + str(wrong) + " wrong guess(es).")
    else:
        print("Out of guesses. The word was '" + secret + "'.")
    print("=" * 40)


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
