#Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character
my_dict={}
str1 = "Hello there how are you"

for word in str1.split():
    if word[0] not in my_dict:
        my_dict[word[0]] = [word]
    else:
        my_dict[word[0]].append(word)

print(my_dict)