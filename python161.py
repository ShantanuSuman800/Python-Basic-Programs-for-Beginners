#Python program to check whether the string is Symmetrical or Palindrome

def pal_str(str):
    if str==str[::-1]:
        print("The given string is Palindrome")
    else:
        print("The given string is not Palindrome")

def sym_str(str):
    n = len(str)
    flag = 0
    if n%2==0:
        mid = n//2+1
    else:
        mid = n//2
    start1 = 0
    start2 = mid
    while(start1<mid and start2<n):
        if(str[start1]==str[start2]):
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break
    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")

pal_str("malayalam")
sym_str("moom")