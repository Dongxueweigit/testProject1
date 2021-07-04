# Author：DongXuewei
# Time  ：2021/7/1 7:09

lista = [1, 2, 3, 4, 5, 6]
print(lista)
lista.append("append")
print(lista)
lista.insert(2, "insert2")
lista.insert(0, "insert0")
lista.insert(len(lista), "insertlen")
lista.insert(-1, "insert-1")
print(lista)
lista.remove(2)
print(lista)
y = lista.pop(0)
x = lista.pop()
print(lista)
print(y, x)

listb = [1, 5, 3, 6, 4, 2, 1.1]
listb.sort()
print(listb)
listc = ['a', 'c', "bd", "bcd"]
listc.sort()
print(listc)

listb.reverse()
print(listb)

listcopy = lista.copy()
print("listcopy=", listcopy)

listd = []
for i in range(1, 11):
    listd.append(i ** 2)
print("listd=", listd)

liste = [i ** 2 for i in range(1, 11)]
print("liste=", liste)

listf = [i for i in range(31)]
print("listf=", listf)

listg = [i * j for i in range(1, 4) for j in range(1, 4)]
print("listg=", listg)
