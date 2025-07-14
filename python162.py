#Ways to remove i’th character from string in Python

test_str = "helloworld"
new_str = "" 
for i in range(len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]
print ("The string after removal of i'th character : " + new_str)


test_str = "helloworld"
 
# Removing char at pos 3
# using replace
test_str = "helloworld"
new_str = test_str.replace('e', '')
print ("The string after removal of i'th character : " + new_str)

new_str = test_str.replace('s', '', 1)
print ("The string after removal of i'th character : " + new_str)


test_str = "helloworld"
new_str = test_str[:2] + test_str[3:]
print ("The string after removal of i'th character : " + new_str)




def remove_ith_character(s, i):
    if i == 0:
        return s[1:]
     
    # Recursive case: return first character concatenated with result of calling function on string with index decremented by 1
    return s[0] + remove_ith_character(s[1:], i - 1)
 
test_str = "helloworld"
new_str = remove_ith_character(test_str, 5)
print("The string after removal of ith character:", new_str)