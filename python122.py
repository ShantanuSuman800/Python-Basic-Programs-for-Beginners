#Python Program to Print Odd Numbers within a Given Range.
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

print("Odd numbers from", start, "to", end,"are:")

for i in range(start, end + 1):
    if(i%2 != 0):
        print(i)
