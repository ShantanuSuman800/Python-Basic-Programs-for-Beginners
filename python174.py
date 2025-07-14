#Python program to find all duplicate characters in string

def find_dup_char(input):
    x=[]
    for i in input:
        if i not in x and input.count(i)>1:
            x.append(i)
    print(" ".join(x))
a=input("enter string: ")
find_dup_char(a)




