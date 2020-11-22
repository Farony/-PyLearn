"""
Задачи по основным функциям

"""
import math
# К-й отезок
def les_time(start_min=(8 * 60), number_lessons=1):
    les_length = 45
    break_length = 5
    stady_min = start_min + number_lessons * (les_length + break_length) - break_length
    return (stady_min // 60, stady_min % 60)

# длина отрезка
def legth_line(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# x1, y1, x2, y2 = map(int, input("Введите x1, y1, x2, y2 через пробел").split())
# print(legth_line(x1, y1, x2, y2))

# площадь треугольника по формуле Герона
def triangle_area(x1, y1, x2, y2, x3, y3):
    A = (x1, y1)  # задаем координаты точек
    B = (x2, y2)
    C = (x3, y3)
    a = legth_line(A[0], A[1], B[0], B[1])
    b = legth_line(B[0], B[1], C[0], C[1])
    c = legth_line(C[0], C[1], A[0], A[1])
    p = (a + b + c) / 2  # Найдем полупериод
    return math.sqrt(p * ((p - a) * (p - b) * (p - c)))


def time2min(h, m):  # Реализуйте функцию time2min(h, m), которая переводит часы и минуты в минуты с
    # начала суток (00:00).
    return (h * 60) + m


def min2time(mm):  # Реализуйте функцию min2time(mm), которая минуты с начала суток переводит в часы и минуты
    # (для показа на электронных часах).
    return '{:02}:{:02}'.format(mm // 60, mm % 60)

# Время поезда
def trail_time():
    print(time2min(22, 5))
    print(min2time(1325))
    time_start_h, time_start_mm = map(int, input("Введите врем отправления в формате 00:00: ").split(':'))
    time_go_h, time_go_mm = map(int, input("Введите врем движения в формате 00:00: ").split(':'))
    print('Время прибытия: ', min2time(time2min(time_start_h, time_start_mm)+time2min(time_go_h, time_go_mm)))
    time_stop_h, time_stop_mm = map(int, input("Введите время прибытия 00:00: ").split(':'))
    print('Время в пути составляет: ', min2time(time2min(time_stop_h, time_stop_mm)-time2min(time_start_h, time_start_mm)))


def leap_year(year):  # Високосный год
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        print('YES')
    else:
        print('NO')


def nod(n1, n2):  # НОД (нибольший общий делитель )алгоритм Евклида
    num_big = 0
    num_small = 0
    if n1 > n2:
        num_big = n1
        num_small = n2
    elif n1 < n2:
        num_big = n2
        num_small = n1
    else:
        print('Числа равны')
    nod = -1
    rem = 0
    while True and (num_big != num_small):
        rem = num_big % num_small
        if rem >= num_small:
            break
        if rem == 0:
            nod = num_small
            break
        else:
            num_big = num_small
            num_small = rem
    if nod == -1:
        print('НОД не найден')
    else:
        print('НОД ', nod)

def min_positiv(a):
    min_pos = -1
    for x in a:
        if (x > 0) and (min_pos < 0):
            min_pos = x
        if (min_pos > x) and (x > 0):
            min_pos = x
    if min_pos > 0:
        return min_pos
    else:
        return 'Nothing'


# for i, x in enumerate('Hello'):
def love_frec(petal_max_number):
    def factorial(n):
        f = 1
        for x in range(1, n+1):
            f *= x
        return f

    def sum_of_num(f):  # Находим сумму всех чисел факториала
        s = str(f)
        col = 0
        for x in s:
            col += int(x)
        return col

    def prime_number(number):
        if number == 1:
            return True
        i = 2
        while number % i != 0:
            i += 1
        return i == number

    def chamomile(n):
        if n < 1:
            return -1
        return prime_number(sum_of_num(factorial(n)))

    love = 0
    for x in range(1, petal_max_number + 1):
        if chamomile(x):
            love += 1
    return 'При максимальном количестве лепестков ' + str(petal_max_number) + ' любит встречается ' + str(love)



r = les_time(60*8, 14)  # input("Введите количество уроков: ")
print('{:02}:{:02}'.format(r[0], r[1]))
#trail_time()
print(triangle_area(-25, -80, 3, 120, 45, 42))
leap_year(2010)
nod(230, 20)
print(min_positiv((-3, -4, 1, -10, -20)))
print(love_frec(5))
