# Author：DongXuewei
# Time  ：2021/7/2 11:05

# f=open("test_txt.txt")
# print(f.readable())
# print(f.readlines())

# f.close()
with open("test_file.jpg", 'rb') as f:
    print(f.read())
    """while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break"""
