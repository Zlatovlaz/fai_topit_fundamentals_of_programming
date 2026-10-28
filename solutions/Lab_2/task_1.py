import copy
from idlelib import config

'''Эксперимент A'''
a = 10
b = a

print(a, b, id(a), id(b)) # оба раза вернёт значение 10, id одинаковый

a += 1

print(a, b, id(a), id(b)) # выведет 11 и 10, id различны

'''Эксперимент B'''
first = [10, 20]
second = first

print(first, second,id(first), id(second)) # оба раза вернёт значение [10, 20] id одинаковый

second.append(30)

print(first, second,id(first), id(second)) # оба раза вернёт значение [10, 20, 30] id одинаковый

'''Дополнение к программе'''
second = [10, 20, 30]
print(first, second, id(first), id(second)) # оба раза вернёт значение [10, 20, 30] id разный
print((first == second, first is second)) # True, False
second.append(40)
print(first, second, id(first), id(second)) # вернёт [10, 20, 30, 40] [10, 20, 30], id разный

config1 = {'name':'Phyton_users', 'members':['Vanya', 'Felicia', 'Jessica', 'Adam'], 'launch_parameters':['time_and_date', 'logs']}
config2 = config1
print(f"config1:{config1}")
print(f"config2:{config2}")

config1['members'].append('Volodya')
config1['launch_parameters'].append('directory')

print(f"config1:{config1}")
print(f"config2:{config2}")

config3 = copy.deepcopy(config1)

config1['members'].remove('Vanya')
config1['launch_parameters'].remove('logs')
print(f"config1:{config1}")
print(f"config3:{config3}")

assert config1 is not config3
assert config1['launch_parameters'] is not config3['launch_parameters']
assert config1['members'] is not config3['members']


