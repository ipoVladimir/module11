# Цель задания:
#
# Закрепить знания об интроспекции в Python.
# Создать персональную функции для подробной интроспекции объекта.
#
# Задание:
# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).

# Пример работы:
# number_info = introspection_info(42)
# print(number_info)
#
# Вывод на консоль:
# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
from pprint import pprint


def introspection_info(obj):
    info_type = type(obj)
    info_attributes = []
    info_methods = []
    for attr_name in dir(obj):
        if callable(getattr(obj, attr_name)):
            info_methods.append(attr_name)
        else:
            info_attributes.append(attr_name)
    info_module = __name__
    return {'type': info_type, 'attributes': info_attributes, 'methods': info_methods, 'module': info_module}


number_info = introspection_info(42)
pprint(number_info)


class User:
    def __init__(self, f, i, o):
        self.f = f
        self.i = i
        self.o = o

    def info(self):
        print(f"I'm {self.f} {self.i}, {self.o}")


user = User('Ivanov', 'Petr', 'Sergeevich')

user_info = introspection_info(user)
print("\nclass User:")
pprint(user_info)