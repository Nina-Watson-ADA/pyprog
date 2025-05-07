def is_palindrome(s):
    # lovely lovely making everything clean and uniform
    cleaned = ''.join(c.lower() for c in s if c.isalnum()) # lowercase all, for count (c) in string (s), checks if the characters are alphanumeric and joins all this into one string with no seperators 
    return cleaned == cleaned[::-1]

# Testing
print(is_palindrome("Aibohphobia")) # True
print(is_palindrome("racecar")) # True
print(is_palindrome("hello"))   # False
user_pal = str(input("Please put in a word you want to test for being a palindrome!\n(does remove whitespace and punctuation): "))
print(is_palindrome(user_pal))