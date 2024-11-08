import requests
from pprint import pprint
import inspect

# help(requests)
# help(requests.get)


some_string = 'I am a string'
some_number = 42
# some_list = [some_string, some_number]

def some_function(param, param_2='n/a'):
    print('my params is', param, param_2)

class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)

some_object = SomeClass()

# Пример 1-Функция hasattr()- проверка на существование аттрибута
# attr_name = 'attribute_1'
attr_name = 'attribute_2'
print(hasattr(some_object, attr_name))
print(hasattr(some_object, 'attribute_1'))
pprint(dir(some_object))

# Пример 2- Функция getattr- получение аттрибута

print(getattr(some_object, 'attribute_1'))
#print(help(getattr))
print(getattr(some_object, 'attribute_2', 'Этого не может быть!'))
#print(getattr(some_object, 'attribute_2'))

"""for attr_name in dir(requests):
    attr = getattr(requests, attr_name)
    print(attr_name, type(attr))"""

# Пример 3- Функция callable()- проверка на тоБ можем ли мы вызывать этот объект
print(callable(some_string))
print(callable(some_function))
print(callable(some_object.attribute_1))
print(callable(some_object.some_class_method))

# Пример 4- Функция isinstance()- мы можем определить,
# является ли определенный объект экземпляром указанного класса
print(isinstance(some_number, str))
print(isinstance(some_function, int))
print(isinstance(some_function, SomeClass))
print(isinstance(some_object, SomeClass))

# Модуль inspect- https://docs.python.org/3/library/inspect.html
# Этот модуль собирает удобные методы и классы для отображения
# интроспектной информации

# Пример 5- самые употребляемые функции
print(inspect.ismodule(requests))
print(inspect.ismodule(some_object), '\n')

print(inspect.ismodule(requests))
print(inspect.isfunction(requests))
print(inspect.isbuiltin(requests), '\n')

# getmodule- позволяет узнать, из какого модуля был получен объект

# some_function_module = inspect.some_function_getmodule() # Неправильно
print(type(some_function_module), some_function_module)

# http://docs.python.org/3/library/inspect.html