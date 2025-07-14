#Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively


def check(string,ch):
      if not string:
        return 0
      elif string[0]==ch:
            return 1+check(string[1:],ch)
      else:
            return check(string[1:],ch)
print("Count is:")
print(check("anjali","a"))