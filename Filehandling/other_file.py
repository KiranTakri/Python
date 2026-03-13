#read data
# f=open("C:\\Users\\kiran\\Desktop\\newfile.txt","r")
# print(f.read())
#write data
# f=open("C:\\Users\\kiran\\Desktop\\newfile.txt","w")
# f.write("Brundaban Rendy")
#Binary file image
f=open("mustang.jpeg","rb")
f2=open("f2.jpeg","wb")
for i in f:
    f2.write(i)

