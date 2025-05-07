print("starting....")

#Loop while asking the user for a password. If they type “summer” output “correct” 
# and end the loop, else output “wrong” and ask again. It should loop until they get it right.

password = ""
while password != "summer":
    print("Wrong password!")
    password = input()


print("Correct!")