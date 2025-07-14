"""Write a Python function to check whether a string is a pangram or not.
Note: Pangrams are words or sentences containing every letter of the alphabet at least once.
For example: "The quick brown fox jumps over the lazy dog"""

def is_Pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in string:
        if i in str.lower(string):
            return True
        else:
            return False
if True:
    print("The given string is a Pangram")
else:
    print("The given string is Not a Pangram")
    
is_Pangram("The quick brown fox jumps over the lazy dog")