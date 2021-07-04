# Author：DongXuewei
# Time  ：2021/7/1 12:01

dict1 = {"a": 1, "b": 2}
dict2 = {}
dict3 = dict2.fromkeys(("a", "b", "c"), 1)

print("dict2=", dict2)
print("dict3=", dict3)

dic4 = {i: i for i in range(3)}
print("dict4=", dic4)

dict5 = {i: j for i in range(1, 5) for j in range(1, 5)}
print("dict5=", dict5)
