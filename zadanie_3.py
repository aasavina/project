# 3) Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
#
def my_func(*elements):
    spisok = list(elements)
    iterator = 0
    result = 0
    while iterator != 2:
        maximum = max(spisok)
        result = maximum + result
        spisok.remove(maximum)
        iterator = iterator + 1
    print(result)


my_func(3, 6, 7,11)

