# Домашнее задание по теме "Создание функций на лету"

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

example = list(map(lambda x, y: x == y, first, second))
print(example)


# Замыкание:


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, mode='w', encoding='utf-8')
        for i in data_set:
            if not isinstance(i, str):
                i = str(i) + '\n'
                file.write(i)
            else:
                i += '\n'
                file.write(i)
        file.close()

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:

from random import choice


class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Может быть', 'Да неужели')
print(first_ball())
print(first_ball())
print(first_ball())
