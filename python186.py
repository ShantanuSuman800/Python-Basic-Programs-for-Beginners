#Python Program to Count the Occurrences of Each character in a Given String Sentence
s = input("Enter a string:")
freq = {} 
for ele in s: 
    if ele in freq: 
        freq[ele] += 1
    else: 
        freq[ele] = 1
    
print(freq)