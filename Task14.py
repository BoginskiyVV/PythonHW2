# 14. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def sumnumbers(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    print(sum)

num = input('Введите число: ').replace('.', '').replace(',', '')
sumnumbers(num)

