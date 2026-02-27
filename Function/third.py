# def stu(info):
#     for i in info:
#         print(f"{i}={info[i]}")
        

# x={"name":"Rohit","age":22,"sec":"j"}
# stu(x)
def stu(info):
    for i,j in info.items():
        print(f"{i}={j}")
x={"name":"Rohit","age":22,"sec":"j"}
stu(x)