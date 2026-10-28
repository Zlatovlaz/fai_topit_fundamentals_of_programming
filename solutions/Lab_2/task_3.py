import sys
import weakref


data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))

class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

print("-"*10+"Практическая задача"+"-"*10)

register = weakref.WeakValueDictionary()

reg1 = Record()
reg2 = Record()

register["first"] = reg1
register["second"] = reg2

register["third"] = Record()
print(*register.keys())

del reg1

print(*register.keys())



