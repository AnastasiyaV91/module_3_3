def print_params(a = 1, b = "строка", c = True):           # Создаtv функцию print_params(a = 1, b = 'строка', c = True)
    print(a, b, c)

print("------------ ПРИМЕРЫ ------------")                 # Разделитель в консоли

print_params()                                             # Вызываем функцию с параметрами по умолчанию
print_params(a = 15, b = "кодинг", c = False)              #
values_list = [15, "кодинг", False]                        #
values_dict = {"a" : 1, "b" : "строка", "c" : True}        #
print_params(b = 25)                                       # Меняем параметры
print_params(c = [1,2,3])                                  #
print_params(*values_list)                                 # Вызываем функцию с параметрами списка values_list
print_params(**values_dict)                                # Вызываем функцию с параметрами словаря values_dict

print("------- ЗАДАНИЕ module_3_3 ------")                 # Разделитель в консоли

values_list_2 = [54.32, 'Строка']                          # Создаем список
print_params(*values_list_2, 42)                        # Вызываем функцию в консоль



