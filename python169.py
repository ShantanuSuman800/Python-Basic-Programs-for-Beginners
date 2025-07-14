#Python Program to check if a string contains any special character

'[@_!#$%^&*()<>?/\|}{~:]'

def check_sp_ch(str):
    sp = "[@_!#$%^&*()<>?/\|}{~:]"
    s = ""
    count = 0
    for i in str:
        if i in sp:
            s+=i
            count+=1
        else:
            pass
    if count!=0:
        print("The string contains special character:",s)
    else:
        print("The string does not contains special character")
a=input("enter string: ")
check_sp_ch(a)
