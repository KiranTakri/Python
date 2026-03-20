
# l=[1,2,3,4,5]
# empty_list=[]
# for i in l:
#     empty_list.append(i)
# print(empty_list)

#syntax:[expression, for variable_name in iterator]
l=[1,2,3,4,5]
# empty_list=[i*i for i in l] prnt the list number
empty_list=[i**2 for i in l]# print the square 
print(empty_list)

empty_list2=[i for i in l if i%2==0]
print(empty_list2)