"""Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321" """
def rev_str(str1="123abcd"):
    print("Given string:",str1)
    rev = (str1[::-1])
    print("Reverse of the given string is:",rev)
rev_str()