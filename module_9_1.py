# Домашнее задание по теме "Введение в функциональное программирование"


def apply_all_func(int_list, *functions):
    """
    Функция apply_all_func(int_list, *functions) принимает параметры: int_list и *functions
    Функция вызвает из списка functions каждую функцию к переданному списку int_list
    и возвращает словарь где ключом будет название вызванной функции
    а значением - её результат работы со списком int_list.
    :param int_list: список из чисел (int, float)
    :param functions: неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
    :return: results
    """
    results = {}
    for function in functions:
        results[function.__name__] = function(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min), end=' ')
print(apply_all_func([6, 20, 15, 9], len, sum, sorted), end=' ')
