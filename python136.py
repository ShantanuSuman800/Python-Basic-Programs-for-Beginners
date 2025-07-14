#Write a Python function that checks whether a passed string is palindrome or not.
def is_palindrome(string):
    print("The given string is:",string)
    if string == string[::-1]:
        print("The given string is a palindrome")
    else:
        print("The given string is not a palindrome")
is_palindrome(string ="malayalam")