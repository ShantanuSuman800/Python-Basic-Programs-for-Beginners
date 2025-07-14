#Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary
#Initializing the string 
string = "Programming is fun. It is a good way to learn new things"

#Splitting the string into a list of words
list_of_words = string.split()

#Creating an empty dictionary
dictionary = {}

#Loop to count the frequency of each word
for word in list_of_words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

#Printing the dictionary
print(dictionary)