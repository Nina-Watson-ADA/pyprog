def average():
    a,b,c,d = get_vals()
    ave = sum([a,b,c,d]) / 4
    return ave

def get_vals():
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    return a,b,c,d

# main program
print(average()) 