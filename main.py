import playing as sis
import random as random
import os as os

while True:
    if sis.kplaying():
        break
    else:
        file = open("words.txt", "r")

        word = []

        for i in file:
            word.append(i)

        word = word[random.randrange(0, word.__len__())]
        final = word
        secret = []

        for i in word:
            secret.append('_')

        secret.pop(secret.__len__()-1)

        life = 4

        while life != 0:
            sis.space()

            if "_" not in secret:
                print("YOU WON!")
                break

            print("It is a Fruit!")

            currentword = ""
            for i in secret:
                currentword = currentword + i + "-"

            print("The word is: " + currentword)

            print("You have: " + str(life) + " try(s)")

            while True:
                letter = input("What Letter? -> ")
                if len(letter) != 1:
                    print("It must be a single letter!")
                else:
                    break

            if letter not in word:
                life = life -1
            else:
                while letter in word:
                    secret[word.index(letter)] = letter
                    word = word.replace(letter,"|",1)



        if life == 0:
            sis.space()
            print("YOU LOSE!")

        print("The word was: " + final)

        input()

        sis.space()
