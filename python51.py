#WAP to enter a character and then determine whether it is a vowel, consonants, or a digit.
a=input("enter a character:")
l=["a","e","i","o","u","A","E","I","O","U"]
if(a.isalpha()==True):
    if(a in l):
        print("a is a vowel")
    else:
        print("a is a consonant")
else:
    print("a is a digit")