# r+ - read write over write nhi hga jab hum write karenge to
# f=open("file.txt","r+")
# print(f.read())
# f.write("/n Pabana Sanga")
# print(f.read())
# f.write("Namaskar")
# print(f.tell())
# print(f.seek(0))
# print(f.read())

# w+- write read isme override h jayega
# f=open("file.txt","w+")
# f.write("Hello, Good morning Akash")
# print(f.read())
# print(f.tell())
# print(f.seek(0))
# print(f.read())
#a+ -append(write) and read
f=open("file.txt","a+")
f.write(" Dharua")
print(f.read())
print(f.seek(0))
print(f.read())

 