# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

from random import randint

n = int(input('Введите число монеток '))

my_list=[]
j=0
k=0
for i in range(n):
    my_list.append(randint(0,1))
    if my_list[i]==1:
        j=j+1
    else:
        k=k+1
        
print(my_list)
# print(j)
# print(k)
if k>j:
    print(f'{j} монеток надо перевернуть')
else:
    print(f'{k} монеток надо перевернуть')

