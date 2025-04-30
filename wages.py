hours = int(input("Hours worked?: "))
if hours > 40:
    overtimehours =  hours - 40
else:
    overtimehours =  0

base_hours =  hours - overtimehours
pay = (base_hours * 12) + (overtimehours * (12*1.5))