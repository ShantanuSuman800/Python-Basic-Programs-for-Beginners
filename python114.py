#Write a program to Convert Decimal to Hexadecimal.
decimal=int(input("enter decimal number: "))
hexadecimal = str(hex(decimal))
print(hexadecimal[2:].upper())