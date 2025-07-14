#Python Program to Count the Number of Vowels in a String

s=input("Enter string:")
count = 0
vowels = ["a","e","i","o","u"]
s = s.lower()
for letter in s:
    if letter in vowels:
        count += 1
print("Count of the vowels is:")
print(count)