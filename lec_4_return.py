def my_func(a, b):
  x1 = 3 * a - 2 * b
  x2 = b * 5 - 4 * a
  return x1, x2

tmp = my_func(3, 2)

print(tmp)
print(tmp[0])
print(tmp[1])

print(my_func(3, 2)[1])
