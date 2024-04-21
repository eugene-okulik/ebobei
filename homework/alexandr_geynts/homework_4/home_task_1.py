my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [1, 2, 3, 4, 5],
    'dict': {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'},
    'set': {1, 2, 3, 4, 5}
}

# Выводим на экран последний элемент кортежа
print("Последний элемент кортежа:", my_dict['tuple'][-1])

# Добавляем в конец списка еще один элемент
my_dict['list'].append(6)
# Удаляем второй элемент списка
del my_dict['list'][1]

# Добавляем элемент с ключом ('i am a tuple',) и значением 'new tuple'
my_dict['dict'][('i am a tuple',)] = 'new tuple'
# Удаляем какой-нибудь элемент
del my_dict['dict']['key1']

# Добавляем новый элемент в множество
my_dict['set'].add(6)
# Удаляем элемент из множества
my_dict['set'].remove(3)

# Выводим на экран весь словарь
print(my_dict)
