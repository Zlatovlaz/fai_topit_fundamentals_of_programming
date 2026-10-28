import numbers
import tracemalloc
import sys
from traceback import print_tb

print("-"*10+"Part one"+"-"*10)
empty = []
list_num = [1,2,3,4,5,6,7,8,9,10]
tuple_num = (1,2,3,4,5,6,7,8,9,10)
stroka_of_ten = "0123456789"
num = 42
None_object = None

print(sys.getsizeof(empty))
print(sys.getsizeof(list_num))
print(sys.getsizeof(tuple_num))
print(sys.getsizeof(stroka_of_ten))
print(sys.getsizeof(num))
print(sys.getsizeof(None_object))

print("-"*10+"Part two"+"-"*10)
empty = []
sys_size = sys.getsizeof(empty)
for i in range(100):
    empty.append(i)
    if sys.getsizeof(empty) != sys_size:
        sys_size = sys.getsizeof(empty)
        print(len(empty), sys_size)

print("-"*10+"Part three"+"-"*10)

tracemalloc.start()
numbers1 = list(range(100_000))
curr, all = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"list: текущая {curr / 1024:.1f} KB, пиковая {all / 1024:.1f} KB")

tracemalloc.start()
numbers2 = range(100_000)
curr, all = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"range: текущая {curr / 1024:.1f} KB, пиковая {all / 1024:.1f} KB")

