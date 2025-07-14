#Write a program to Convert Hexadecimal to Binary
hexadecimal = input("hex: ")

#Function to convert Hexadecimal to Binary
def hex_to_bin(hexadecimal):
    #Convert hexadecimal to decimal
    decimal = int(hexadecimal, 16)
    #Convert decimal to binary
    binary = bin(decimal)
    #Remove '0b' from binary
    binary = binary[2:]
    #Print binary
    print(binary)

#Call function
hex_to_bin(hexadecimal)
