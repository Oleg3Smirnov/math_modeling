import numpy as np

i = 0
j = 0
name = 'Smirnov Oleg'

name = '_'.join(name)
print(name)
name = name.upper()
print(name)

massive_1 = np.zeros((1, len(name)))

for symbol in name:
    massive_1[0, i] = ord(symbol)
    i += 1
print(massive_1)

name = name.lower()
print(name)

massive_2 = np.zeros((1, len(name)))

for symbol in name:
    massive_2[0, j] = ord(symbol)
    j += 1
print(massive_2)

print(f'Максимальное значение из списка с верхним регистром: {max(massive_1[0])}')
print(f'Максимальное значение из списка с нижним регистром: {max(massive_2[0])}')
