#Python program to print even length words in a string

def printWords(s):
    s = s.split(' ')
    for word in s:
        if len(word)%2==0:
            print(word)


m = input("enter string:")
s = m.split(" ")
l = list(filter(lambda x: (len(x)%2==0),s))
print(l)