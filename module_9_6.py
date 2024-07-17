# Домашнее задание по теме "Генераторы"


def all_variants(text):
    count = 0
    while count < len(text):
        i = 0
        for i in range(len(text)):
            if i < len(text) and i <= len(text) - 1 - count:
                yield text[i:i + 1 + count]
            if i == len(text) - 1 - count:
                count += 1


a = all_variants("abc")
for j in a:
    print(j)
