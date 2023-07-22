import random 

a = random.randint(1, 100)
b = []
c = []
d = []
e = []

for i in range(0, 100, 1):
    b.append(random.randint(0, 100))
    c.append(random.randint(0, 100))
    d.append(random.randint(0, 100))

e.append(max(b))
e.append(max(c))
e.append(max(d))

print(f'Самый большой элемент: {max(e)}')
print(f'Сумма массивов: {sum(b) + sum(c) + sum(d)}')
