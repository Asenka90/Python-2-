#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

print("Задача 1")
х = int(input("Введите число:"))
sum = 0
while х > 0:
 number = х % 10
 sum = sum + number
 х = х // 10
print("Сумма цифр введенного числа =", sum)

#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print("Задача 2:")
m = int(input("Введите число N:"))
print("Набор произведений чисел от 1 до N:")
а = 1
for i in range(1, m+1):
 print (а**2)
 а+=1

#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#Пример:
#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

print("Задача 3:")
def f(n):
    sum = 0
    list = {i:((1+1/i)**i) 
    for i in range(1,n+1)}
    for i in list:
        sum += list.get(i)
    print('sum =',round(sum,2))
    return {i:((1+1/i)**i) for i in range(1,n+1)}
n = int(input("Введите кол-во чисел в последовательности: "))
print(f(n))

#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

print("Задача 4:")
import random
n1 = abs(int(input('Введите число N: ')))
s = []
for i in range(-n, n+1):
    s.append(i)
print("Список элементов от ",-n," до ", n," : ", s)
with open('file.txt', 'w') as f:
    for i in range(3):
        f.write(f'{random.randint(0,len(s)-1)}\n')
f= open('file.txt', 'r')
result=1
for line in f:
    result *= s[int(line)]
print("Произведение элементов:", result)
f.close()

#Реализуйте алгоритм перемешивания списка.

print("Задача 5:")
print("Перемешенный список:")
for i in range(len(s)):
 number = s.pop(random.randint(0, len(s)-1))
 s.insert(random.randint(0, len(s)-1), number)
print(s)


