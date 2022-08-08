# a = 10 
# b = 1
# if a == b:
#     print(True)
# else:
#     print(False)
# print(id(a))
# print(id(b))

list1 = [2,1,32,21,244,213]
list2 = [56,76,45,54,65]
for item in list1:
    if item in list2:
        print("overlapping")
    else:
        print("not overlapping")
           