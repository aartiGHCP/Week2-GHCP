
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a command-line Hangman game in Python so students practice string manipulation, loops, conditionals, and handling user input.

**Skills practiced:** String manipulation, loops, conditionals, random selection

## 📝 Tasks

### 🛠️ Implement the Hangman game

#### Description
Create a playable Hangman game that selects a word randomly from a list, accepts single-letter guesses, displays progress after each guess, and ends when the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list.
- Accept single-letter guesses from the user (case-insensitive) and ignore repeats.
- Display the current word progress (for example: c _ _ e) after each guess.
- Track and display remaining incorrect attempts.
- Maintain and show the list of guessed letters.
- End the game when the word is fully guessed (win) or attempts reach zero (loss), and reveal the word.
- Print a clear win or lose message.

#### Example play (illustrative)
```
Secret word: "code"
Guesses remaining: 6
Guessed: c
Progress: c _ _ _
Guessed: o
Progress: c o _ _
Guessed: x
Guesses remaining: 5
...
```

---

Starter code: see [assignments/games-in-python/starter-code.py](assignments/games-in-python/starter-code.py) (optional)
