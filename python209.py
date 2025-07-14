#WAP that prompts user to enter an alphabet and then print all the words that starts with that alphabet from the list of words

alp = input("Enter an alphabet:")
list1 = ["work","is","worship","god","is","great"]
for i in list1:
    if i.startswith(alp):
        print(i)