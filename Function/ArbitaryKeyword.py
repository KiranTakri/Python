def Emp(**info):
    print(type(info))
    print(info["name"])
    print(info["age"])
    print(info["dept"])
Emp(name="Rohit",age=22,dept="IT")