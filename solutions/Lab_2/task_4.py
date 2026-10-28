import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)
print("Сборщик мусора включен:", gc.isenabled())
print("Пороги поколений:", gc.get_threshold())
print("Статистика поколений (get_stats) ДО сбора:")
for i, stat in enumerate(gc.get_stats()):
    print(f"Поколение {i}: {stat}")
collected_count = gc.collect()
for i, stat in enumerate(gc.get_stats()):
    print(f"Поколение {i}: {stat}")

print('-'*10+"Доп. задача"+"-"*10)
print(id(first))
print(id(second))
del first, second
print(gc.collect())

print('-'*10+"Доп. эксперимент"+"-"*10)
gc.disable()
third = []
fourth = []
fifth = []

third.append(fourth)
fourth.append(third)
fifth.append(fifth)

del third, fourth, fifth
print(gc.collect())
gc.enable()

print('-'*10+"Практическая задача"+"-"*10)
garbage1 = gc.collect()

a = {'Name' : 'A', 'Near' : []}
b = {'Name' : 'B', 'Near' : []}
c = {'Name' : 'C', 'Near' : []}
d = {'Name' : 'D', 'Near' : []}

a['Near'].append(b)
b['Near'].append(c)
c['Near'].append(a)

print(id(a), id(b), id(c), id(d))
print('В a было добавлено b')
print('В b было добавлено c')
print('В c было добавлено a')

del a, b, c

garbage2 = gc.collect()
print('Сбор мусора 1 и 2: ', garbage1,',', garbage2)
print("Независимый узел:", d)
