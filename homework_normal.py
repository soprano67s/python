__author__ = 'Несмачный Максим Станиславович'

import random

print('Задача-1:\n'
      'Дан список заполненный произвольными целыми числами, получите новый список элементами которого будут\n'
      'квадратные корни элементов исходного списка, но только\n'
      'если результаты извлечения корня не имеют десятичной части\n'
      'и если такой корень вообще можно извлечь.')
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

d = [12, -15, 23, 9, -18, 25, 4, 16]
final = [int(i) for i in range(max(d)) if int(i) ** 2 in d]
print('Исходный список: ', d)
print('Финальный список: ', final)
print('-----------------------------------------\n')


print('\nЗадача-2:\n'
      'Дана дата в формате dd.mm.yyyy, например: 02.11.2013.\n'
      'Ваша задача вывести дату в текстовом виде, например: \n'
      'второе ноября 2013 года.\n')

date = input('Введите дату в формате dd.mm.yyyy: ')
newDate = (date.split('.'))
day = {
    '01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое',
    '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
    '11': 'одинадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое',
    '15': 'пятьнадцатое', '16': 'шестьнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое',
    '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе',
    '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое', '26': 'двадцать шестое',
    '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'дридцатое',
    '31': 'тридцать первое'
}
month = {
    '01': 'января', '02': 'февраля', '03': 'марта',
    '04': 'апреля', '05': 'мая', '06': 'июня',
    '07': 'июля', '08': 'августа', '09': 'сентября',
    '10': 'октября', '11': 'ноября', '12': 'декабря'
}
print('Дата в текстовом виде: {} {} {} года.'.format(day[newDate[0]], (month[newDate[1]]), newDate[2]))
print('-----------------------------------------\n')

print('\nЗадача-3:\n'
      'Напишите алгоритм заполняющий список произвольными целыми числами в диапазоне от -100 до 100\n'
      'В списке должно быть n - элементов\n'
      'Подсказка: для получения случайного числа изпользуйте функцию randint() модуля random\n')

count = int(input('Введите количество элементов: '))
numList = []
n = 0
while n < count:
    numList.append(random.randint(-100, 100))
    n += 1

print(numList)
print('-----------------------------------------\n')
print('\nЗадача-4:\n'
      'Дан список заполненный произвольными целыми числами\n'
      'Получите новый список, элементами которого будут только уникальные элементы исходного\n')

a = [1, 2, 3, 1, 4, 5, 3, 6, 7, 5, 2, 6, 8, 7, 9, 4, 10]
b = set(a)
print('Исходный список: ', a)
print('Финальный список: ', b)
