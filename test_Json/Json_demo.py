# Author：DongXuewei
# Time  ：2021/7/2 17:04

import json

# Json由列表和字典组成，列表和字典的顺序没有强制要求
# 创建一个Json对象，命名为data
data = {
    "name": ["jerry", 'nickname'],
    "age": 26,
    "gender": "female"
}

data1 = json.dumps(data)
print(data1)
print('type befor:', type(data))
print('type affter:', type(data1))

data2 = json.loads(data1)
print(data2)
print(type(data2))
