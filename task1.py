# Задача 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и выводит название этого дня недели.

week_day = int(input('Введите число, обозначающее день недели: '))
if week_day == 1:
    print('Понедельник')
elif week_day == 2:
    print('Вторник')
elif week_day == 3:
    print('Среда')
elif week_day == 4:
    print('Четверг')
elif week_day == 5:
    print('Пятница')
elif week_day == 6:
    print('Ура! Это суббота!')
elif week_day == 7:
    print('Ура! Это воскресенье!')
else:
    print('Такого дня нет')
