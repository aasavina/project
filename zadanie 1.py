# 1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide(sum_1, sum_2):
    try:
        return sum_1 / sum_2
    except ZeroDivisionError:
        return "ошибка"


x = int(input("введите числитель 1 "))
y = int(input("введите знаменатель 2 "))
sum = divide(x, y)
print(sum)
