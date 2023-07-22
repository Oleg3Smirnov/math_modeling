[ 22 июля 2023 г. 2:33 ] ⁨Олег⁩: import random 

n = random.randint(2, 50)
x = random.randint(1, n*8//10)
a = []

print(f'n = {n}')
print(f'Количество элементов в списке: {x}')
print('Числа в списке могут повторяться')
for i in range(0, x, 1):
    b = random.randint(1, 100)
    a.append(b)
print(f'Список: {a}')

c = random.randint(1, n-1)

h = 0
while h < 1:
    e = 1
    f = 1
    for i in range(0, x, 1):
        if c == a[i]:
            e += 1
    if e == f:
        h += 1
    else:
        c = random.randint(1, n-1)

print(f'Рандомное число: {x}')
