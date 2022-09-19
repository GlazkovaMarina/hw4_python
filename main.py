#1
num = float(input("Введите число: "))
d = float(input("Введите точность: "))
s = len(str(d).split(".")[1])
print(s)

temp = '{:.' + str(s) + 'f}'
print(temp.format(num))

#2
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
list = [int(input("Введите число: ")) for i in range(int(input("Введите количество элементов в массиве: ")))]
print(f"список: {list}")
set = set()
for elem in list:
  set.add(elem)

print(f"множество: {set}")