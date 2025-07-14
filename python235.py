#Python program to read file word by word
file = open("pranjal.txt","r") 
  
# loop to read line by line 
for line in file: 
    # split words of each line 
    words = line.split() 
      
    # iterate over words and print one by one 
    for word in words: 
        print(word) 

file.close()
