'''Input a temperature and a time in hours e.g. 01 - 23, 
If the temperature is less than 21 and the time is between 6 and 22 
output "turn heating on" Otherwise output "turn heating off" 
Repeat this forever 
Test with temp = -1, 0, 6, 20, 21, 22, 25, 999999
and time = -1, 0, 5,6,7, 21,22,23, 99999
'''
while True:
    temp = int( input("Enter a temperature: ") )
    time = 999
    while not (0 <= time <= 23):
        time = int( input("Enter a time (0-23): ") )
    if (temp < 21) and (6 <= time <= 22):
        print("turn heating on")
    else:
        print("turn heating off") 