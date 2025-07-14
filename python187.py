#Python Program to Check if a Substring is Present in a Given String
def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")
 
string =input("enter string:")
sub_str = input("enter substring:")
check(string, sub_str)

