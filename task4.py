# Задача 4. Напишите программу, которая на вход принимает число (N),
#  а на выходе показывает все чётные числа от 1 до N.

number = int(input('Введите число N: '))
count = 2
ran = range(1, number+1)
for count in ran:
    if count %2 == 0:
        print(count, end = ', ')
        count += 1
