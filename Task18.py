# 18. *Реализуйте алгоритм перемешивания списка.
# В виду отсутствия допонительных требований к списку можно реализовать следующим способом:

def input_array(n):
    a = 0
    while a <= n:
        array.append(a)
        a += 1
    print(array)

def mix_list(size):
    i = size
    while i >= 0:
        z = array[i]
        mix_array.append(z)
        i -= 1
    print(mix_array)
  
array = []
mix_array = []
n = int(input('Введите число для создания массива: '))
input_array(n)

size = len(array)-1
print(f'Число индексов в списке равно: {size}')

mix_list(size)



    


        
        