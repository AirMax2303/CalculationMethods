import math

n1 = 2
n2 = 3
x, e = input('Введите значение аргумента и относительной точности ').split()
s = b = x = float(x)
y = x * x
e = float(e)
while abs(b / s) > e:
    b *= -y / (n1 * n2)
    n1 += 2
    n2 += 2
    s += b
print(s)
print(math.sin(x))
input()  # команда ДЕРЖИТ экран
