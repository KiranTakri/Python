import Calculate
print(dir(Calculate))
for i in dir(Calculate):
    if("__" not in i):
        print(i)