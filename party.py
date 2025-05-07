names = []
for i in range(3):
    names.append(input("name? "))


more = True
while more:
    names.append(input("name?"))
    more =(input("more? ") == "y")

print(names) 