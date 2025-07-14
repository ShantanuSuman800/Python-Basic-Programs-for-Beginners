#Program to Find ‘n’ Character Words in a Text File
import re
f = open('pranjal.txt', 'r')
text = f.read()
f.close()
words = re.findall(r"\b\w{n}\b", text)
print(words)