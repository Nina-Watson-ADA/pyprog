num1 = float(input("enter first number: "))
while not (1 < num1 < 100):
    print("invalid")
    num1 = float(input("enter first number: "))


num2 = float(input("enter second number: "))
answer = num1 + num2
print(answer)