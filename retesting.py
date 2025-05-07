import re

valid_whole_number_regex = r"^[0-9]+$"
valid_positive_whole_decimal_number = r"^(?:0|[1-9]\d*)(?:\.\d+)?$"
valid_floating_point_2dp = r"^[0-9]+\.[0-9][0-9]$"
valid_alphabetic_string = r"^[A-Za-z]+$"

# Use the match method to check whether something matches the rules. 
if re.match(valid_whole_number_regex, "456"):
  print("Match found!") 
else:
  print("No match.")

person_name = "123abc"   # should return False
person_age = 15.5  # should this be allowed? - Depends on requirements, but generally, age is a whole number
person_height = "blah blah blah"  # should this be allowed? - No, height should be numeric

# Other regex methods do exist such as search() (which looks for matching
# characters) and sub() (which replaces characters), but match is 
# probably the most commonly used and the one you should use here.


# Validate name (alphabetic only)
def is_valid_name(name):
    return bool(re.match(valid_alphabetic_string, name))

# Validate age (whole number only, non-negative)
def is_valid_age(age):
    return isinstance(age, int) and age >= 0

# Validate height (floating-point with 2 decimal places)
def is_valid_height(height):
    if isinstance(height, str):
        return bool(re.match(valid_floating_point_2dp, height))
    return False


print("Name valid:", is_valid_name("Alice"))    # True
print("Name valid:", is_valid_name("123abc"))   # False

print("Age valid:", is_valid_age(25))   # True
print("Age valid:", is_valid_age(15.5)) # False

print("Height valid:", is_valid_height("170.50"))   # True
print("Height valid:", is_valid_height("blah blah"))    # False