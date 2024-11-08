import sys
from pprint import pprint

# Что доступно в библиотеке sys
# Обширный набор инструментов для работы с системными операциями
pprint(dir(sys))

# Путь к интерпретатору Python
#print(sys.executable)

# В какой операционной системе мы работаем
print(sys.platform)

# Текущая версия Python
print(sys.version)
print(type(sys.version))
print(sys.version_info)

def func(x):
    if sys.version.split(' ')[0] == '3.12.4':
        return x + 10
    else:
        raise Exception('Недопустимая версия')

print(func(10))

# Список, содержащий параметры командной строки, если она была задана
print(sys.argv)

# Путь поиска модуля, список каталогов, в которых Python будет искать модули во время импорта
print(sys.path)

# Словарь, который отображает имена модулей для всех загруженных
# загруженных в текущий проект модулей
print(sys.modules)

# Стоит упомянуть __builtins__ - псевдо-модуль, содержащий
# встроенные в интерпретатор объекты (константы, исключения, функции)
print(__builtins__)
pprint(dir(__builtins__))


# sys используется не только для того, чтобы узнавать новую информацию
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
# print(factorial(2000))

# Функция 'sys.setrecursionlimit' позволяет увеличить
# максимальную глубину стека вызовов функций

sys.setrecursionlimit(5000)
sys.set_int_max_str_digits(10000)
print(factorial(2000))

# Функция 'getsizeof'- узнать сколько памяти занимает наш объект- факториал
print(sys.getsizeof(factorial))  # 160 байт


# Интроспекция помогает разработчикам анализировать структуру
# и функциональность объектов, что, в свою очередь, способствует
# олее эффективному написанию и отладке программ.
#
# Знание о возможностях интроспекции открывает новые горизонты в работе
# с Python, улучшая понимание кода и его взаимодействия с различными
# библиотеками и модулями