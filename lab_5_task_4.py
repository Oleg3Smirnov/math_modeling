import random

flowers = ['Обезьяний дракула', 'Танцующие девушки', 'Психотрия возвышенная']
colours_1 = ['Скандальный оранжевый', 'Шапки деда мороза', 'Цвет бедра испуганной нимфы', 'Яиц странствующего дрозда', 'Звезды в шоке']
colours_2 = []

for i in range(0, len(flowers), 1):
    a = random.randint(0, len(colours_1)-1)
    colours_2.append(colours_1[a])

print("flowers colours:", dict(zip(flowers, colours_2)))
