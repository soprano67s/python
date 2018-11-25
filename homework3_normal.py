#NORMAL

# Задание-1:
# Напишите функцию возвращающую ряд Фибоначчи с n-элемента до m-элемент
# Первыми элементами ряда считать цифры 1 1
print('=' * 60)
print('Функция возвращающая ряд Фибоначчи с n-элемента до m-элемент')
print('\n')
def fibonacci(n, m):
    fib = []
    a, b = 0, 1
    for num in range(m):
        fib.append(b)
        a, b = b, a + b
    n -= 1
    res = [fib[i] for i in range(n, m)]
    del fib
    print(res)
    return res

fibonacci(5, 10)
print('\n')
# Задача-2:
# Напишите функцию сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную фукцию и метод sort()
print('=' * 60)
print('Функция сортирующая исходный список по возрастанию')
print('\n')
def sort_to_max(origin_list):
    lst = []
    while len(origin_list) > 0:
        a = origin_list[0]
        for i in origin_list:
            if i <= a:
                a = i
        origin_list.remove(a)
        lst.append(a)
    print(lst)


origin_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print('-' * 10, 'Исходный лист', '-' * 10, '\n', origin_list)
print('-' * 10, 'Финальный лист', '-' * 10), sort_to_max(origin_list)
print('\n')
# Задача-3:
# Напишите собственную реализацию функции filter
# Разумеется, внутри нельзя использовать саму функцию filter
print('=' * 60)
print('Функция выполняющая реализацию функции filter')
print('\n')
def filters(arg, obj):
    lst = []
    for i in obj:
        if i != arg:
            lst.append(i)
    print(lst)

list = [91, 19, 83, 99, 4, 2, 10, -12, 4, 101, 2.5, 20, 7, 3, -11, 4, 4, 4, 0]
print('-' * 10, 'Исходный лист', '-' * 10, '\n', list)
print('-' * 10, 'Финальный лист', '-' * 10), filters(4, list)
print('\n')
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма

print('=' * 60)

import math

A1 = 2, 3
A2 = 0, 2
A3 = 4, 1
A4 = 6, 2

print('Даны четыре точки A1 =', A1,'A2 = ', A2, 'A3 =', A3, 'A4 =', A4, '\n'
      'Определить, будут ли они вершинами параллелограмма')
print('\n')

def parallel(a, b, c, d):
    p1 = False
    p2 = False
    ab = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    cb = math.sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
    cd = math.sqrt((d[0] - c[0])**2 + (d[1] - c[1])**2)
    ad = math.sqrt((d[0] - a[0])**2 + (d[1] - a[1])**2)
    if ab == cd and cb == ad:
        print('Равенство сторон: верно')
        p1 = True
    else:
        print('Противоположные стороны НЕ равны')
    hO1 = ((a[0] + c[0])/2, (a[1] + c[1])/2)
    hO2 = ((b[0] + d[0])/2, (b[1] + d[1])/2)
    if hO1 == hO2:
        print('Равенство половин диагоналей: верно')
        p2 = True
    else:
        print('Половины диагоналей НЕ равны')

    if p1 and p2:
        print('Вершины A1%s, A2%s, A3%s, A4%s образуют параллелограмм' % (a, b, c, d))
    else:
        print('Вершины не образуют параллелограмм')

parallel(A1, A2, A3, A4)