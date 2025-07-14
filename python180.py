#Python Program to Remove the Characters of Odd Index Values in a String

def newString(str1):
    str2 = ''

    for i in range(len(str1)):
        if(i % 2 == 0):
            str2 = str2 + str1[i]
    return str2

string = input("Please Enter your Own String : ")       
print("Original String :  ", string)
print("Final String :     ", newString(string))