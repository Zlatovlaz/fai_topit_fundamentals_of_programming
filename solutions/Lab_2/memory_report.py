import sys
import tracemalloc


def scenaryi(name, count, create_func):
    tracemalloc.start()
    obj = create_func()
    size = sys.getsizeof(obj)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {
        'name': name,
        'count': count,
        'size': size,
        'peak': peak,
        'current': current,
    }

def all_scenarii():
    result = []

    result.append(scenaryi("Пустой список", 0, lambda: []))
    result.append(scenaryi("Список из 10 целых чисел", 10, lambda: [0,1,2,3,4,5,6,7,8,9]))
    result.append(scenaryi("Кортеж из 10 целых чисел", 10, lambda: (0,1,2,3,4,5,6,7,8,9) ))
    result.append(scenaryi("Строка из 10 символов", 10, lambda: "0123456789"))
    result.append(scenaryi("Целое число", 1, lambda: 42))
    result.append(scenaryi("Объект None", 1, lambda: None))
    result.append(scenaryi("list(range(100_000))", 100_000, lambda: list(range(100_000))))
    result.append(scenaryi("range(100_000)", 100_000, lambda: range(100_000)))

    return result

def report(result):
    for i in result:
        print(f"Сценарий: {i['name']}")
        print(f"Число элементов: {i['count']}")
        print(f"Размер внешнего объекта: {i['size']} : ")
        print(f"Пиковый объем памяти : {i['peak']}")
        print(f"Текущий объем памяти : {i['current']}")
        print()

    list_result = next((r for r in result if r["name"] == "list(range(100_000))"), None)
    range_result = next((r for r in result if r["name"] == "range(100_000)"), None)

    if list_result and range_result:
        if range_result["peak"] > 0:
            range_peak = range_result["peak"]
        else:
            range_peak = range_result["size"]

        if list_result["peak"] > 0:
            list_peak = list_result["peak"]
        else:
            list_peak = list_result["size"]
        ratio = list_peak / range_peak
        print()
        print('Сравнение list(range()) и range()')
        print(f'Отношение пиковых объемов: {ratio:.1f}x')
        print(f'list использует в {ratio:.0f} раз больше памяти, чем range')

result = all_scenarii()
report(result)

