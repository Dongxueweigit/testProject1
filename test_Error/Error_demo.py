# Author：DongXuewei
# Time  ：2021/7/3 6:51

class MyException(Exception):
    def __init__(self, msg):
        print(f"这是一个异常：{msg}")


def set_age(num):
    if num <= 0 or num > 200:
        raise MyException(f"值错误：{num}")
    else:
        print(f"age is : {num}")


set_age(-10)
