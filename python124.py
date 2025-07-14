#Python Program to Count the Number of Digits in a Number
# take input from the user
num = int(input("Enter a number: "))

# initialize count
count = 0

# loop until the number becomes 0
while (num > 0):
    # increment count
    count = count + 1
    num = num // 10

# print result
print ("Total number of digits : ", count)


