import random

import numpy as np

N = random.randint(1, 100)
c = np.zeros((1, N))
d = np.zeros((1, N))
e = np.zeros((1, N))

for i in range(0, N, 1):
    c[0, i] = random.randint(1, 100)

for i in range(0, N, 1):
    d[0, i] = random.randint(1, 100)

for i in range(0, N, 1):
    e[0, i] = random.randint(1, 100)

print(c)
print(d)
print(e)

h = max(c[0])
if h < max(d[0]):
    h = max(d[0])
    if h < max(e[0]):
        h = max(e[0])
elif h < max(e[0]):
    h = max(e[0])

print(f'наибольший элемент среди всех трех массивов: {h}')
print(f'сумма всех элементов созданных массивов: {sum(c[0]) + sum(d[0]) + sum(e[0])}')
