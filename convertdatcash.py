POUNDS_TO_EUROS = 1.18 
POUNDS_TO_DOLLARS = 1.31 


def convertor(v,f,t):  
    if f == "p" and t == "e":
        outval = v * POUNDS_TO_EUROS
        if x == 1:
            pass
    elif f == "p" and t == "d":
        outval = v * POUNDS_TO_DOLLARS
    else:
        outval = 999
    return outval

# MAIN PROGRAM
val = float(input("how much?"))
fromcurr = input("currency from (p/d/e)?")
tocurr = input("currency to   (p/d/e)?")
convertor(val, fromcurr, tocurr)
#print(convertor(100, "p", "d"))
# print(result)