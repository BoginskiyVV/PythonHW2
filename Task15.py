# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений 
# чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def multiply_numbers(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        array.append(result)
        i += 1
    print(array)

n = int(input('Введите число: '))
array = []
multiply_numbers(n)