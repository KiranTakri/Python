#defaul,positional,keyword,arbitary positional,arbitrary keyword argument
def Stu(*args):
    print(args)
    print(type(args))
    print(len(args))
    print(args[0])
    print(args[len(args)-1])
Stu("Rohit","Raman","Raj","Ram")#positional argument
