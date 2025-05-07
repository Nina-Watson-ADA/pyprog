def checker(seasons):
    for season in seasons:
       if season  == "summer":
           return "valid"
    return "invalid"

print(checker(["x","summer","z"])) 