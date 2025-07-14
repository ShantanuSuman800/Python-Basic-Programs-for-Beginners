#Python Program to Find the Binary Equivalent of a Number Recursively

l=[]
def convert(b):
    if(b==0):
        return l
    dig=b%2
    l.append(dig)
    convert(b//2)
a=int(input("Enter a number: "))
convert(a)
l.reverse()
print("Binary equivalent:")
for i in l:
    print(i,end="")

print("******\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*********")

def convert_binary(num):
  if num > 1:
    convert_binary(num//2)
  print(num % 2,end = '')
decimal = int(input("ENTER A DECIMAL NUMBER : "))
print("THE BINARY EQUIVALENT OF %d IS : "%decimal,end='')
convert_binary(decimal)