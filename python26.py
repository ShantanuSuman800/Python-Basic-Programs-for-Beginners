#Python program to convert all units of time into seconds.
h=int(input("enter time in hours:"))
m=int(input("enter time in minutes:"))
s=int(input("enter time in seconds:"))
time=(h*3600)+(m*60)+s
print("the time in seconds is", time)