import random

def high_low():
    rand = random.randint(1,100)
    playing = True
    while playing:
        try:
            guess = int(input("guess a number! "))
            if guess == rand:
                print("congrats")
                playing = False
            else:
                print("LOWER" if guess > rand else "HIGHER")
        except Exception as e:
            print(f"Operation failed: {e}")



play = "y"
while play == "y":
    high_low()
    play = input("play again? (y/n)")

print("game over!")

            