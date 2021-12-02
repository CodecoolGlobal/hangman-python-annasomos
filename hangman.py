from typing import Text
import random
import os
from hangman_ascii_art import hangman, hangmantext, goodbye, dead, congrat, fool
from playsound import playsound

c = open("countries-and-capitals.txt")
all = c.readlines()
history = set()


def secrethard():
    randomline = random.choice(all)
    secretlist = randomline.split(" | ")
    return random.choice(secretlist).strip().upper()

def secreteasy():
    randomline = random.choice(all)
    secretlist = randomline.split(" | ")
    return secretlist[0].strip().upper()

def showsecret():
    showsecret = list("_" * len(secret))

    for index,character in enumerate(secret):
        if character == " ":
            showsecret[index] = " "
        elif character == "-":
            showsecret[index] = "-"
    return showsecret

def clearscreen():
    os.system("clear")

def play(secret, lives, display):
    while lives > 0:
        print(" ".join(display))
        guess_is_invalid = True
        while guess_is_invalid:
            guess = input("Enter a letter: ").upper()
            clearscreen()
            if guess == "QUIT":
                guess_is_invalid = False
            elif len(guess) == 1 and guess.isalpha() == True and guess != "":
                guess_is_invalid = False
            else:
                guess_is_invalid = True
            if guess_is_invalid:
                playsound("foolsound.wav",False)
                print(f"{fool}\nPlease only enter 1 letter from the alphabet!")
                continue
        if guess == "QUIT":
            return goodbye
        else:
            if guess in history:
                print(f"You already tried {guess}. These are your guesses: {history}.\n{hangman[lives]}")
            else:
                history.add(guess)
                if guess in secret:
                    new_show = ""
                    for index, letter in enumerate(secret):
                        if letter == guess:
                            new_show += guess
                        else:
                            new_show += display[index]
                    display = new_show
                    playsound("right.wav", False)
                    print(f"{hangman[lives]}\nYay! {guess} is in the secret word.")
                elif guess not in secret:
                    playsound("wrong.mp3", False)
                    print(f"These are your guesses: {history}.")
                    lives -= 1
                    print(hangman[lives])
                if display == secret:
                    clearscreen()
                    playsound("yay.mp3", False)
                    return f"{hangman[lives]}\n{congrat}\nThe secret was {secret}."
    return print(f"{dead}\nThe secret was {secret}"), playsound("die.mp3")




print(hangmantext)
name = input("Please enter your name: ")
print(f"Hello, {name}! Let's play hangman!")
level_is_invalid = True
while level_is_invalid:
    level = input("Please choose level EASY or HARD: ").upper()
    clearscreen()
    if level == "QUIT":
        level_is_invalid = False
    elif level == "EASY" or level == "HARD":
        level_is_invalid = False
    else: 
        level_is_invalid = True
    if level_is_invalid:
        print("Please type 'EASY' or 'HARD' to continue.")
        continue
    if level == "QUIT":
        print(goodbye)
    elif level == "EASY":
        print(hangman[12])
        lives = 12
        secret = secreteasy()
        showsecret_easy = showsecret()
        result = play(secret, lives, showsecret_easy)
        print(result)
    elif level == "HARD":
        print(hangman[8])
        lives = 8
        secret = secrethard()
        showsecret_hard = showsecret()
        result = play(secret, lives, showsecret_hard)
        print(result)

