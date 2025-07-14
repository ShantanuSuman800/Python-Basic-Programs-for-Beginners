#Python program to split and join a string

s = input("enter string: ")

print(s.split(" "))

print("--".join(s.split()))




def split_string(string):
    list_string = string.split(' ')
    return list_string
 
def join_string(string):
    string = '-'.join(string.split())
    return string
string = input("enter string: ")
print(split_string(string))
print(join_string(string))