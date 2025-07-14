#Write a program to Convert the given Binary Number into Decimal.
num = int(input("Enter the Binary number:"))
dn = 0
n = num
i = 1
while n>0:
    r = n%10
    dn = dn+(r*i)
    i = i*2
    n = n//10
print("Equivalent Decimal number is:",dn)