#Python program to Reverse a single line of a text file
#Open the text file
text_file = open("text_file.txt", "r")

#Read the text file
text_data = text_file.read()

#Reverse the text
reversed_data = text_data[::-1]

#Close the text file
text_file.close()

#Open the text file in write mode
text_file = open("text_file.txt", "w")

#Write the reversed text to the file
text_file.write(reversed_data)

#Close the text file
text_file.close()
