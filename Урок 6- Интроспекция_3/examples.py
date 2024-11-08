# Полезный системный пакет- sys
# https://dacs.python.org/3/library/sys.html

import sys
from pprint import pprint


# Что доступно в библиотеке sys
# Обширный набор инструментов для работы с системными операциями
# pprint(dir(sys))

# Путь к интерпретатору Python
print(sys.executable)

# В какой операционной системе мы работаем
print(sys.platform)

# Текущая версия Python
print(sys.version)
print(sys.version_info)

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
print(dir(__builtins__))

