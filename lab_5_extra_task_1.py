import time

def is_devide_by_three(a):
    return (a%3 == 0) 

nums = [24, 28, 19, 179]
timer_1 = time.time()
result = list(map(is_devide_by_three, nums)) 
timer_2 = time.time()

	
symbols = 'Python'
timer_3 = time.time()
symbol_codes = [ord(symbol) for symbol in symbols]
timer_4 = time.time()

a = []
timer_5 = time.time()
for i in range(0, 5000, 1):
    b = 2*i**4 - 5*i**3 - i**2 + 8*i -10
    a.append(b)
timer_6 = time.time()

print(f'Map: {- timer_1 + timer_2}')
print(f'Списковое включение: {- timer_3 + timer_4}')
print(f'Цикл: {- timer_5 + timer_6}')

c = [- timer_1 + timer_2, - timer_3 + timer_4, - timer_5 + timer_6]
if min(c) == - timer_1 + timer_2:
    print('Map - самый быстрый')
elif min(c) == - timer_3 + timer_4:
    print('Списковое включение - самое быстрое')
else:
    print('Цикл - самый быстрый')
