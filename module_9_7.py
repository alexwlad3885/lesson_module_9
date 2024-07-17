# Домашнее задание по теме "Декораторы"


def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        count = 0
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                count += 1
        if count <= 0:
            return (f'Простое\n'
                    f'{number}')
        else:
            return (f'Составное\n'
                    f'{number}')
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
result = sum_three(5, 7, 20)
print(result)
