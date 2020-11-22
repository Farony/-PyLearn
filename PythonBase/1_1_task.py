"""
x = input("Введите х:")        # 3
y = input("Введите у:")        # 5

print(x, type(x))  # 3 string
print(y, type(y))  # 5 string

z = x+y
print(z, type(z))  # 35 string (две строки написали рядом - конкатенация, concatenation)

x = int(x)
y = int(y)
print(x, type(x))  # 3 string
print(y, type(y))  # 5 string
z = x+y
print(z, type(z))  # 35 string (две строки написали рядом - конкатенация, concatenation)

x, y = map(int, input("Введите х и у через пробел").split())
print(x+y)


"""
import math
# К-й отезок
def les_time(start_min=(8 * 60), number_lessons=1):

    les_length = 45
    break_length = 5
    stady_min = start_min + number_lessons * (les_length + break_length) - break_length
    return (stady_min // 60, stady_min % 60)


r = les_time(60*8, 14)  # input("Введите количество уроков: ")
print('{:02}:{:02}'.format(r[0], r[1]))

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


print(triangle_area(-25, -80, 3, 120, 45, 42))


def time2min(h, m):  # Реализуйте функцию time2min(h, m), которая переводит часы и минуты в минуты с
    # начала суток (00:00).
    return (h * 60) + m


def min2time(mm):  # Реализуйте функцию min2time(mm), которая минуты с начала суток переводит в часы и минуты
    # (для показа на электронных часах).
    return '{:02}:{:02}'.format(mm // 60, mm % 60)


print(time2min(22, 5))
print(min2time(1325))

time_start_h, time_start_mm = map(int, input("Введите врем отправления в формате 00:00: ").split(':'))
time_go_h, time_go_mm = map(int, input("Введите врем движения в формате 00:00: ").split(':'))
print('Время прибытия: ', min2time(time2min(time_start_h, time_start_mm)+time2min(time_go_h, time_go_mm)))

time_stop_h, time_stop_mm = map(int, input("Введите время прибытия 00:00: ").split(':'))
print('Время в пути составляет: ', min2time(time2min(time_stop_h, time_stop_mm)-time2min(time_start_h, time_start_mm)))
