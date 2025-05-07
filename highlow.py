import random

def high_low():
    rand = random.randint(1,100)
    playing = True
    while playing:
        guess = int(input("guess a number! "))
        if guess == rand:
            print("congrats")
            playing = False
            break
        print("LOWER" if guess > rand else "HIGHER")
        '''
        elif guess > rand:
            print("LOWER") 
        else:
            print("HIGHER")
        '''


play = "y"
while play == "y":
    high_low()
    play = input("play again? (y/n)")

print("game over!")

            