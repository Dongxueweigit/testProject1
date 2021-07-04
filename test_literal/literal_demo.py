# Author：DongXuewei
# Time  ：2021/7/2 8:52

name = "hellotest"
age = 30
workyears = 3.5
list1 = [1, 2, 3, 4]
dict1 = {"name": "zhangsan", "age": 18}

print('name is:{name},age is:{age},workyears is:{workyears}')
print(f'name is:{name}。age is:{age}。workyears is:{workyears}。list is:{list1}。dict is:{dict1}')
print(f'list is:{list1[0]}。dict is:{dict1.get("name")}')

print("我的名字：%s\n我的年龄：%d\n工作年限：%.2f\n" % (name, age, workyears))

print("my name is: {}\nmy age is: {}\nmy workyears is: {}\n".format(name, age, workyears))

print('list is: {},dict is: {},name is : {},value is :{}'.format(list1, dict1, dict1.get("name"), list1[0]))
print('{2},{3},{age},{name}'.format(*list1, **dict1))
