# Требуется вывести все целые степени двойки, не превосходящие числа N.
import math
N=int(input('Введите число '))
i=0
my_list=[]
n=int(math.log2(N))
for i in range(n+1):
    m=2**i
    my_list.append(m)
    

print(*my_list)
# print(n)