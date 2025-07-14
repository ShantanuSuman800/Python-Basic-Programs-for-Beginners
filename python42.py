#Write a Program to check whether an alphabet entered by the user is a vowel or a consonant
a=input("enter the alphabet:")
vowels=["a","e","i","o","u"]
if (a in vowels):
    print("it is a vowel")
else:
    print("it is a consonant")