people = []
loop = True

def ending():
    print (len(people))
    quit()

def add_peeps():
    addpeople = input("Who are you inviting to your party?: ")
    people.append(addpeople)
    print(people)

for i in range (3):
    add_peeps()


def add_more_people():
    yesno = input ("Do you want to invite more people y/n?: ")
    if yesno == "y":
        add_peeps()

    elif yesno == "n":
        print ("No more invites")
        ending()

    else:
        print("invalid answer. Sorry")
        ending()
        
while loop == True: 
    add_more_people()

