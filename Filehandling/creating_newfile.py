#create new file
# x=open("file.txt","x")
# x.close()
#writing into file
# f=open("file.txt","w")
# f.write("Hello,\n")
# f.write("My name is Kishan\n")
# f.write("Welcome to Python\n")
# f.close()
#reading file
# f=open("file.txt","r")
# data=f.read()
# print(data)
# f.close()
#write mode
# f=open("file.txt","w")
# f.write("hello\n")
# f.write("Good Morning\n")
# f. write("Welcome to Python\n")
# f.write("This is file handling\n")
# f.write("This is write mode\n")
# f.write("This will overwrite the existing data in the file\n")
#readline mode
# f=open("file.txt","r")
# data=f.readline()
# print(data)
# f.close()
#readlines mode
# f=open("file.txt","r")
# data=f.readlines()
# print(data)
# f.close()
#append mode
# f=open("file.txt","a")
# f.write("This is append mode\n")
# f.write("This will be added at the end of the file\n")
#tail 
f=open("file.txt","r")
print(f.tell)
print(f.read(10))
print(f.tell)