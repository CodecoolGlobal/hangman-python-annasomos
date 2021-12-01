from typing import Text
import random


#create separate lists for countries and capitals
c = open("countries-and-capitals.txt")
all = c.readlines()

#countries = []
#capitals = []
#for line in countries_capitals:
#    countries.append(line.split(" | ")[0])
#    capitals.append(line.strip())

#6-8-12 lives - hard - medium - easy
#spaceket kiteszi ha van benne, ugy vonalkaz (pl. _ _ _  _ _ _ _ _  _ _)

randomline = random.choice(all)
secretlist = randomline.split(" | ")
secret = random.choice(secretlist).strip().upper()
showsecret = list("_" * len(secret))

for index,character in enumerate(secret):
    if character == " ":
        showsecret[index] = " "
    elif character == "-":
        showsecret[index] = "-"

history = []


def play(secret, lives, display):
    while lives > 0:
        print(" ".join(display))
        guess = input("Enter a letter: ").upper()
        guess_is_invalid = True
        while guess_is_invalid:
            if guess == "QUIT":
                guess_is_invalid = False
            elif len(guess) == 1 and guess.isalpha() == True and guess != "":
                guess_is_invalid = False
            else:
                guess_is_invalid = True
            if guess_is_invalid:
                print("Please only enter 1 letter from the alphabet!")
                break
        if guess == "QUIT":
            print("Good-bye!")
            exit()
        elif guess in secret:
            new_show = ""
            for index, letter in enumerate(secret):
                if letter == guess:
                    new_show += guess
                else:
                    new_show += display[index]
            display = new_show
            lives -=1
            print(f"Yay! {guess} is in the secret word.")
        elif not guess in secret:
            history.append(guess)
            lives -= 1
        
lives = 15
play(secret, lives, showsecret)
