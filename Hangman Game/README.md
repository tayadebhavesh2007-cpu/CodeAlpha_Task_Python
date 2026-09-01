# Hangman

A simple text-based Hangman game in Python. The computer picks a random word, and you guess it one letter at a time before running out of tries.

Written as a beginner Python practice project — no external libraries, no frameworks, just the standard library.

## Features

- Random word chosen from a small built-in list
- Letter-by-letter guessing with the word shown as `g u i t _ _`
- 6 incorrect guesses allowed
- Tracks and displays letters already tried
- Input validation: rejects empty input, multiple characters, digits, and symbols
- Repeated guesses don't cost you a life
- Play-again loop after each round

## Requirements

Python 3 (no packages to install).

## How to Run

```bash
git clone https://github.com/tayadebhavesh2007-cpu/hangman.git
cd hangman
python hangman.py
```

On some systems use `python3 hangman.py`.

## Sample Gameplay

```
========================================
HANGMAN
The word has 6 letters.
You can make 6 wrong guesses.
========================================

Word:  _ _ _ _ _ _
Wrong guesses left: 6
Guess a letter: g
Correct! 'g' is in the word.

Word:  g _ _ _ _ _
Wrong guesses left: 6
Tried: g
Guess a letter: e
Nope, no 'e' in the word.

Word:  g _ _ _ _ _
Wrong guesses left: 5
Tried: e, g
Guess a letter: u
Correct! 'u' is in the word.

========================================
You win! The word was 'guitar'.
You used 1 wrong guess(es).
========================================

Play again? (y/n):
```

## How It Works

The game is split into small functions so each part does one job:

| Function | Purpose |
| --- | --- |
| `build_display(secret, guessed)` | Builds the masked word, showing guessed letters and `_` for the rest |
| `get_guess(guessed)` | Loops until the player enters one new, valid letter |
| `play()` | Runs a single round and prints the win/lose result |
| `main()` | Repeats rounds until the player chooses to stop |

The main game loop is driven by a single condition — keep going while the player has lives left *and* hidden letters remain:

```python
while wrong < MAX_WRONG and "_" in build_display(secret, guessed):
```

The word list and guess limit are set as constants at the top of the file, so they're easy to change:

```python
WORDS = ["python", "keyboard", "monsoon", "guitar", "network"]
MAX_WRONG = 6
```

## Concepts Practiced

`random` module, `while` loops, `if`/`elif`/`else` branching, string methods (`strip`, `lower`, `isalpha`, `join`), lists, and organising code into functions.

## Possible Improvements

- Load a larger word list from a text file
- Draw the classic ASCII hangman figure as lives are lost
- Add difficulty levels based on word length
- Keep a win/loss score across rounds
- Add a hint or category for each word

## Author

**Bhavesh Tayade** — BCA student, Sanjivani College of Engineering, Kopargaon

GitHub: [@tayadebhavesh2007-cpu](https://github.com/tayadebhavesh2007-cpu)
