import random


def menu():

    while True:

        command = input('Type "play" to play the game, "exit" to quit: ')
        if command == "play":
            return play()
        elif command == "exit":
            break


def play():

    word = random.choice(["python", "java", "kotlin", "javascript"])
    word_letters = set(word)
    correct_letters = set()
    wrong_letters = set()
    lives = 8

    while lives > 0:

        # Creating a hint
        hint = ""
        for i in word:
            if i in correct_letters:
                hint += i
            else:
                hint += "-"
        print(f"\n{hint}")

        # Check if the user won and ask for the user's letter
        if correct_letters == word_letters:
            print("You guessed the word!\nYou survived!\n")
            return menu()
        else:
            new_letter = input("Input a letter: ")

        # Check user input for errors
        if len(new_letter) != 1:
            print("You should input a single letter")
            continue
        elif not new_letter.islower():
            print("Please enter a lowercase English letter")
            continue

        # Add or not add user letter to sets
        if new_letter in wrong_letters or new_letter in correct_letters:
            print("You've already guessed this letter")
        elif new_letter not in word_letters:
            print("That letter doesn't appear in the word")
            wrong_letters.add(new_letter)
            lives -= 1
        else:
            correct_letters.add(new_letter)

    # User is lost
    print("You lost!\n")
    return menu()


# Beginning of the game
print("H A N G M A N")
menu()
