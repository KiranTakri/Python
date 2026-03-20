import zipfile
# with zipfile.ZipFile("Python.zip","w") as f:
#     f.write("file1.txt")
#     f.write("file2.txt")
# with zipfile.ZipFile("Python.zip","r") as f:
#     f.extractall()
with zipfile.ZipFile("Python.zip","r") as f:
    con=f.read()
    print(con)

