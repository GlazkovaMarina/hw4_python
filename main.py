#1
print("task 1")
num = float(input("Введите число: "))
d = float(input("Введите точность: "))
s = len(str(d).split(".")[1])
print(s)

temp = '{:.' + str(s) + 'f}'
print(temp.format(num))

#2
print("task 2")
def Factor(n):
    list = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            list.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        list.append(n)
    return list

num = int(input("Введите число: "))
print(Factor(num))

#3
print("task 3")
list = [int(input("Введите число: ")) for i in range(int(input("Введите количество элементов в массиве: ")))]
print(f"список: {list}")
set = set()
for elem in list:
  set.add(elem)

print(f"множество: {set}")

#4
print("task 4")
import random
import numpy as np

dict_ = {
    0: "\u2070",
    1: "\u00B9",
    2: "\u00B2",
    3: "\u00B3",
    4: "\u2074",
    5: "\u2075",
    6: "\u2076",
    7: "\u2077",
    8: "\u2078",
    9: "\u2079"
}

k = int(input("Введите степень многочлена: "))
list = []
for i in range(k+1):
    list.append(random.randint(0,100))
print(f"Список: {list}")
print(f"Корни уравнения: {np.roots(list)}")
with open('file.txt', 'w') as f:
    t = k
    str1 = ""
    for i in range(k-1):
        if (list[i] != 0):
            str1 += f"{list[i]}" + "x" + dict_[t]  + " + "
        t -= 1
    str1 += f"{list[k - 1]}" + "x + " + f"{list[k]}" + " = 0"
    f.write(str1)