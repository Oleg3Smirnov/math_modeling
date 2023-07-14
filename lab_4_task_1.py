a = int(input('Введите количество элементов в массиве: '))
b = []
c = 0

for i in range(0, a, 1):
    d = float(input(f'Введите элемент массива {i}: '))
    b.append(d)
    c += b[i]

def my_func(d):
    x = d / a
    return x

print(my_func(c))
