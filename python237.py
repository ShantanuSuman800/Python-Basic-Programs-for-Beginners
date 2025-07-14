#Python – Get number of characters, words, spaces and lines in a file
fo = open("test.txt", "r")

charCount = 0

wordCount = 0

lineCount = 0

spaceCount = 0

for line in fo:
    charCount += len(line)
    wordCount += len(line.split())
    lineCount += 1
    spaceCount += line.count(' ')
fo.close()

print("Number of characters :", charCount)

print("Number of words :", wordCount)

print("Number of lines :", lineCount)

print("Number of spaces :", spaceCount)

