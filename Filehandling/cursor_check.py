f=open("demo.txt","r")
print(f.tell()) #prints the current position of the cursor
print(f.read(5)) #reads 5 characters and moves the cursor to the right
print(f.tell()) #prints the current position of the cursor
f.close()