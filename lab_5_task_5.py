name = 'Smirnov Oleg Vladimirovich'
a = []
b = ''
c = ''
d = []
e = ''
h = 0
t = 0

for symbol in name:
    if symbol == 95:
        c = c
    elif ord(symbol) > 64 and ord(symbol) < 97 or ord(symbol) == 32:
        c += symbol
    else:
        c += chr(ord(symbol) - 32)
    a.append(ord(c[h]))
    h += 1

print(a)

for symbol in name:
    if symbol == 95:
        e = e
    elif ord(symbol) > 97 or ord(symbol) == 32:
        e += symbol
    else:
        e += chr(ord(symbol) + 32)
    d.append(ord(e[t]))
    t += 1

print(d)

print(f'Сумма значений из списка с верхним регистром: {sum(a)}')
print(f'Сумма значений из списка с нижним регистром: {sum(d)}')
