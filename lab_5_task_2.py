name = 'Smirnov Oleg'
a = []
b = ''
c = ''
d = []
e = ''
h = 0
t = 0
for symbol in name:
    b += symbol + '_'
print(b)

for symbol in b:
    if symbol == 95:
        c = c
    elif ord(symbol) > 64 and ord(symbol) < 97 or ord(symbol) == 32:
        c += symbol
    else:
        c += chr(ord(symbol) - 32)
    a.append(ord(c[h]))
    h += 1

print(a)

for symbol in b:
    if symbol == 95:
        e = e
    elif ord(symbol) > 97 or ord(symbol) == 32:
        e += symbol
    else:
        e += chr(ord(symbol) + 32)
    d.append(ord(e[t]))
    t += 1

print(d)

print(f'Максимальное значение из списка с верхним регистром: {max(a)}')
print(f'Максимальное значение из списка с нижним регистром: {max(d)}')

#print(f'Максимальное значение из списка с верхним регистром: {ord(max(c))}')
#print(f'Максимальное значение из списка с нижним регистром: {ord(max(e))}')
