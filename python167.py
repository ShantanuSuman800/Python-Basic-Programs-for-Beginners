#Remove all duplicates from a given string in Python


def duplicate_rem(str):
    s = ""
    for h in str:
        if h not in s:
            s = s+h
    print(s)
str1=input("enter string: ")
duplicate_rem(str1)