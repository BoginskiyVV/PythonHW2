# 16. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример: Для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}

def sumnumbers(n):
    sum = 0
    b = 1
    count = 0
    for i in range(1, n + 1):
        a = (1+1/b)**b
        sum += a
        count += 1
        b += 1
        array.append(round(a, 2))
    print(array)
    print(f'Сумма чисел для {n} по формуле равна {round(sum, 2)}')

array = []
n = int(input('Введите число: '))
sumnumbers(n)