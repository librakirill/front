#задание №1
new_list = []
def simple_func(arg):
    if type(arg) is list:
        print("это список и длина его " + str(len(arg)))
        if len(arg) > 1:
            for i in arg:
                new_list.append(type(i))
            print("список состоит из следующих классов " + str(list(set(new_list))))
    elif type(arg) is int:
        print("это число")
    elif type(arg) is str:
        print("это строка")
    elif type(arg) is tuple:
        print("это неизменяемый список и длина его " + str(len(arg)))
        if len(arg) > 1:
            for i in arg:
                new_list.append(type(i))
            print("список состоит из следующих классов " + str(list(set(new_list))))
    else:
        print("это что то другое")

# пример
simple_func([16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD'])

# задание №2

import numbers
list_2 = []
list_1 = [16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD']
list_2 = [num for num in list_1 if isinstance(num, (int,float))]
print(list_2)
list_2.sort()
print(list_2)