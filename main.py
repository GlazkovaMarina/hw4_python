#1
num = float(input("Введите число: "))
d = float(input("Введите точность: "))
s = len(str(d).split(".")[1])
print(s)

temp = '{:.' + str(s) + 'f}'
print(temp.format(num))

