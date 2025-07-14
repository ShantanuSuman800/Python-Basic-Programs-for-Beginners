#write a program to calculate sum of subjects and find percentage
math=int(input("enter math number:"))
english=int(input("enter english number:"))
physics=int(input("enter physics number:"))
chemistry=int(input("enter chemistry number:"))
computer=int(input("enter computer number:"))
sum_marks=math+english+physics+chemistry+computer
percentage=(sum_marks/500)*100
print("the sum of the marks is",sum_marks,"and the percentage is",percentage)