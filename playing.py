def kplaying():
    while True:

        print("--------------------")
        print("-----HANGED MAN-----")
        print("--------------------")
        print("")
        print("Want to play? <y/n>")
        answer = input()

        if answer != 'n' and answer != 'y':
            print("Please insert a valid ")
        elif answer == 'y':
            return False
        else:
            return True

def space():
    print("\n"*20)