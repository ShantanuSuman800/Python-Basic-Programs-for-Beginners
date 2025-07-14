#Write a program to Convert Binary to Hexadecimal
num = int(input("Enter the Binary number:"))
dn = 0
n = num
i = 1
while n>0:
    r = n%10
    dn = dn+(r*i)
    i = i*2
    n = n//10
k = 1
he =0
for h in str(dn):
    he = he+int(h)*k
    k = k*16
print(he)