#Python program to Check for URL in a String


def Find(string):
    x=string.split()
    res=[]
    for i in x:
        if i.startswith("https:") or i.startswith("http:"):
            res.append(i)
    return res
string = input("enter string: ")
print("Urls: ", Find(string))