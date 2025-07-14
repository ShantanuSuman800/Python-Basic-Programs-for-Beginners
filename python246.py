#Python Program to merge two files into a third file
#open the two files
f1=open('file1.txt','r')
f2=open('file2.txt','r')
#open the third file in write mode
f3=open('file3.txt','w')
#read the content from the two files
content1=f1.read()
content2=f2.read()
#write the content in the third file
f3.write(content1)
f3.write(content2)
#close the files
f1.close()
f2.close()
f3.close()
print("Merging of two files completed")

