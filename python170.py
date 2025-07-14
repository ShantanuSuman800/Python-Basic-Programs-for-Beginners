#Find words in string which are greater than given length k

def string_k(k, str):
    string = []
    text = str.split(" ")
    for x in text:
        if len(x) > k:
            string.append(x)
    return string
k = int(input("enter length: "))
str =input("enter string: ")
print(string_k(k, str))

