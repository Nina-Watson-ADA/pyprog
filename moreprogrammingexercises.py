#Write a program to display the 7 times table (3 marks) 
for i in range(1,11): 
    print(i*7)
  



# Write a program to display all the squares of the even numbers from 1 to 100 inclusive (4 marks)

for number in range(1, 101):
    if number % 2 == 0:
        square = number ** 2
        print(f"The square of {number} is {square}")