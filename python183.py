'''Python Program to Check if a String is a Pangram or Not
(A pangram is a sentence that uses all 26 letters of the English alphabet at least once. like” The quick brown fox
jumps over the lazy dog”)'''
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