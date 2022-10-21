# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на введенных пользователем позициях.

def input_array(n):
    a = 0
    b = -n
    while b < n:
        b = -n + a
        array.append(b)
        a += 1
    print(array)

def multiplication():
    print(f'Произведение чисел по указанным индексам равно: {array[first_num_index] * array[second_num_index]}')

array = []
n = int(input('Введите число создания массива: '))
input_array(n)

size = len(array)-1
print(f'Число индексов в списке равно: {size}')

first_num_index = int(input(f'Введите первый индекс от 0 до {size}: '))
second_num_index = int(input(f'Введите второй индекс от 0 до {size}: '))

print(f'Число с индексом {first_num_index}: {array[first_num_index]}')
print(f'Число с индексом {second_num_index}: {array[second_num_index]}')
multiplication()