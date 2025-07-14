#Python Program to Accept Three Digits and Print all Possible Combinations from the Digits
# Store the digits in a list
list1 = [int(digit) for digit in input("Enter three digits separated by space: ").split()]

# Iterate over the list to print all possible combinations
for num1 in list1:
    for num2 in list1:
        for num3 in list1:
            print(num1, num2, num3)

#122
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

print("Odd numbers from", start, "to", end,"are:")

for i in range(start, end + 1):
    if(i%2 != 0):
        print(i)