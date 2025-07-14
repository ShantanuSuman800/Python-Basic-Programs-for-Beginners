"""WAP that accepts the marks of 5 subjects and finds the percentage marks obtained by the student. It
also prints grades according to the following criteria: Between 90-100% Print 'A', 80-90% Print 'B', 60-
80% Print 'C', 50-60% Print 'D', 40-50% Print 'E', Below 40% Print F."""

math=int(input("enter math marks:"))
chem=int(input("enter chem marks:"))
phy=int(input("enter phy marks:"))
cse=int(input("enter cse marks:"))
eng=int(input("enter eng marks:"))
s=math+chem+phy+cse+eng
per=s/5
print("the percentage is {}%".format(per))
if(90<=per<=100):
    print("A")
if(80<=per<=90):
    print("B")
if(60<=per<=80):
    print("C")
if(50<=per<=60):
    print("D")
if(40<=per<=50):
    print("E")
if(per<40):
    print("F")