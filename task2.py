#  Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
import math
s=int(input('Сумма чисел  '))
p=int(input('Произведение чисел  '))

# x+y=s
# x*y=p
# x=s-y
# y(s-y)=p
# ys-y^2=p
# y^2-ys+p=0

D=s*s-4*p
y1=(s+(D**0.5))/2
y2=(s-(D**0.5))/2

x1=s-y1
x2=s-y2

c1=p/y1
c2=p/y2

# print(D)
print(f'первое число {int(y1)}, второе число {int(y2)} (или наоборот)')
# print(f'y2 {int(y2)}')

# print(f'x1 {x1}')
# print(f'x2 {x2}')

# print(f'c1 {c1}')
# print(f'c2 {c2}')

# print(a)