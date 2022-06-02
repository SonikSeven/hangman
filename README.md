# Hangman

This is a simple implementation of the classic word guessing game Hangman in Python. To win the game, you must guess the hidden word one letter at a time before running out of attempts.

## Features

- Play Hangman with a selection of words.
- Keeps track of your win/loss record.
- Command-line interface for clear and simple interaction.

## How to Play

After starting the script, you can choose to do one of the following:

- Type `play` to start a new game.
- Type `results` to view your win/loss record.
- Type `exit` to close the program.

## Game Rules

1. The game selects a word from a predefined list of words (`python`, `java`, `kotlin`, `javascript`).
2. The word to guess is represented by a row of dashes.
3. You guess by suggesting letters within a certain number of attempts.
4. For each incorrect guess, the number of attempts decreases.
5. You can only guess one lowercase English letter at a time.
6. If you guess the word within the limit of attempts, you win. Otherwise, you lose.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/hangman.git
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## License

This project is licensed under the [MIT License](LICENSE.txt).
