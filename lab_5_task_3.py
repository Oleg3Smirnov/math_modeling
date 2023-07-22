import time

M = int(input())
N = int(input())

timer = time.time()
for i in range(0, M, 1):
    print(f'Значение внешней переменной цикла: {i}')
    time.sleep(1)

    for j in range(0, N, 1):
        print(f'Значение внутренней переменной цикла: {j}')
        time.sleep(1)

print(f'{time.time() - timer} seconds')
