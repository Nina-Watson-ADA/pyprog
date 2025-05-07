from colored import Fore, Back, Style

hours = float(input("hours worked? "))
target = input("target met (y/n)? ")


if hours > 60:
    double_time = hours - 60
    overtime_hours = hours - 40 - double_time 
elif hours > 40:
    double_time = 0
    overtime_hours = hours - 40 
else:
    double_time = 0
    overtime_hours = 0

base_hours = hours - overtime_hours - double_time
wages = base_hours * 12 + overtime_hours * 12 * 1.5 + double_time * 12 * 2
if target == "y":
    wages += 50

wages = max(wages, 20) 
wages = min(wages, 600) 

print(f'{Fore.white}{Back.green}wages = {wages}{Style.reset}')