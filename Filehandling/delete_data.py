f=open("file.txt","r")
line=f.readlines()
del line[2]
f=open("file.txt","w")
f.writelines(line)
f.close()