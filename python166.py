#Python program to accept the strings which contains all vowels

def check_v(str):
    str = str.lower()
    v = ["a","e","i","o","u"]
    s = []
    for i in str:
        if i in v:
            s.append(i)
        else:
            pass
    if sorted(s)==sorted(v):
        print("Accepted")
    else:
        print("Not Accepted")
a=input("enter string: ")
check_v(a)