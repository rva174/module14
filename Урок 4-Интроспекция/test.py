import requests
from pprint import pprint

# help(requests)
# help(requests.get)

some_string = 'I am a string'
some_number = 42
some_list = [some_string, some_number]

def some_function(param, param_2='n/a'):
    print('my params is', param, param_2)

class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self, attribute_1)

some_object = SomeClass()

func = some_function

# Пример 1- Аттрибут класса __name

print(some_function.__name__)
print(SomeClass.__name__)
print(requests.__name__)
print(func.__name__)
#print(some_string.__name__)
#print(some_object.__name__)

# Пример 2- Узнаем тип объекта

print(type(some_number))

print(type(some_number) is int)
print(type(some_number) is list)

print(type(requests))
print(type(requests.get))

# Пример 3- функция dir
# Функция dir возвращает отсортированный аттрибутов и методов,
# доступных для указаннного объекта, который может быть объявленной переменной или функцией

"""pprint(dir(some_number))
pprint(dir(some_list))
pprint(dir(some_function))
pprint(dir(SomeClass))
pprint(dir(some_object))
pprint(dir(requests))"""

# Без указания аргумента dir() выводит доступные в локальной области видимости,
# как показано ниже

#pprint(dir())

 