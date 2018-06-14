#!/usr/local/bin/python3
"""Guess number between 1-10."""
def main():
    from random import randint
    secret = randint(1,10)
    print("Welcome!")
    guess = 0
    while guess !=secret:
        g = input("Guess the number: ")
        guess = int(g)
        if guess == secret:
            print ("You win!")
        else:
            if guess > secret:
                print("Too high!")
            else:
                print("Too low!")
        print("Game Over.")


    #fix this
    
if __name__ == "__main__":
    main()
