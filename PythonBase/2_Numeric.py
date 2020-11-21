import math

s1 = bin(10)   # получаем из числа 10 строки для представления числа в бинарной,
# восьмеричной и шестнадцатеричной системах счисления
print(s1)
print(int(s1, 2))  # обратно из бинарной строки в целое число

s2 = oct(10)  # Восьмеричное представление числа
print(s2)  # Заметьте, что префикс **0o**, а не просто 0, как в языке С.
print(int(s2, 8))  # обратно из бинарной строки в целое число

s3 = hex(10)  # Шестадцатиричное
print(s3)
print(int(s3, 16))

x1 = int('10')      # из строки - десятичного представления числа - получаем целое число типа int
print(x1)
print(type(x1))

x1 = int('  10  ')  # **допускает пробельные символы до и после числа**
print(x1)
print(type(x1))

print("Комплексные числа")
# преобразовываем стандартные типы
kmpl = complex(int(s3, 16), int(s2, 8))
print(kmpl)
print(type(kmpl))

x = float(x1)
x = str(x1)
x = bool(x1)
x = int(x1)
y = int(s3, 16)

print(x + y)
print(x)
x += 1
print(x)
x -= 2
print(x)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(-x)
print(abs(-x))  # Возвращает абсолютное значение x
print(divmod(x, y))  # Возвращает частное и остаток деления x на y в виде кортежа двух значений типа int
print(pow(x, y, 5))  # Более быстрая альтернатива выражению (x ** y) % z
print(round(3.1416, 10))  # Округление


# Числа с плавающей точкой
print("Округления")
x = 1.854
print("round(", x, ") =", round(x))
print("round(", x, ",2) =", round(x, 2))
print("math.floor(", x, ") =", math.floor(x))  # Округляет число вниз («пол»), при этом floor(1.5) = 1, floor(-1.5)=-2
print("math.ceil(", x, ") =", math.ceil(x))  # Округляет число вверх («потолок»), при этом ceil(1.5) = 2,ceil(-1.5)=-1
print("math.trunc(", x, ") =", math.trunc(x))  # Отбрасывает дробную часть
print("float.is_integer(", x, ") =", float.is_integer(x))  # True, если дробная часть 0.
print("float.as_integer_ratio(", x, ") =", float.as_integer_ratio(x))  # Возвращает числитель и знаменатель дроби

print("Math")
x = 0.567
print("math.acos(", x, ") =", math.acos(x))
print("math.acosh(", 1.3, ") =", math.acosh(1.3))
print("math.asin(", x, ") =", math.asin(x))
print("math.asinh(", x, ") =", math.asinh(x))
print("math.atan(", x, ") =", math.atan(x))
print("math.atan2(", x, y, ") =", math.atan2(y, x))  # Возвращает арктангенс y/x в радианах
print("math.atanh(", x, ") =", math.atanh(x))
print("math.copysign(", x, -3, ") =", math.copysign(x, y))
x = 1.867
print("math.cos(", x, ") =", math.cos(x))
print("math.cosh(", 0.876, ") =", math.cosh(0.876))
print("math.sin(", x, ") =", math.sin(x))
print("math.sinh(", 0.876, ") =", math.sinh(0.876))
print("math.tan(", x, ") =", math.tan(x))
print("math.tanh(", 0.876, ") =", math.tanh(0.876))


print("math.degrees(math.acos(", 0.876, ")) =", math.degrees(math.acos(0.876)))
print("math.radians(", 135, ") =", math.radians(135))

print("math.e", math.e)
print("math.pi", math.pi)
print("math.exp(", x, ") =", math.exp(x))  # Возвращает e в степени x, то есть math.e ** x
print("math.pow(", x, y, ") =", math.pow(y, x))  # Возвращает $$x^y$$ в виде числа типа float
print("math.sqrt(", 425, ") =", math.sqrt(425))  # Возвращает e в степени x, то есть math.e ** x

print("math.fabs(", -x, ") =", math.fabs(x))  # Возвращает абсолютное значение x в виде числа типа float
print("math.factorial(", 5, ") =", math.factorial(5))  # Возвращает Возвращает x!
print("math.floor(", x, ") =", math.floor(x))  #
print("math.fmod(", x, y, ") =", math.fmod(y, x))  # Выполняет деление по модулю (возвращает остаток) числа x на
# число y дает более точный результат, чем оператор %, применительно к числам типа float
print("math.frexp(", x, ") =", math.frexp(x))  # Возвращает кортеж из двух элементов с мантиссой (в виде числа
# типа float) и экспонентой (в виде числа типа int)
print("math.ldexp( 0.9333, 1 ) =", math.ldexp(0.9333, 1))  # Возвращает $$m \cdot 2^x$$ – операция, обратная math.frexp
print("math.fsum(", (2, 3, 6), ") =", math.fsum((2, 3, 6)))  # Возвращает сумму значений в итерируемом объекте i в
# виде числа типа float

print("math.hypot(", x, y, ") =", math.hypot(y, x))  # Возвращает расстояние от точки (0,0) до точки
# (x,y) $$\sqrt{x^2 + y^2}$$

# Работа с бесконечностями и бесконечномалыми
f = float('inf')
print(f + 45)
print("math.isinf(f = float('inf')) =", math.isinf(f))  # Возвращает True, если значение x типа
# float является бесконечностью $$±\infty$$
print("10 / (f = float('inf')) =", 10 / f)
print("f / f =", f / f)
print("math.isnan(f / f) =", math.isnan(f / f))  # Возвращает True, если значение x типа float не является числом
f2 = float('-inf')
print("f2 = float('-inf'); f + f2", f + f2)

print("math.isnan(f + f2) =", math.isnan(f + f2))
print("math.log(", x, y, ") =", math.log(y, x))  # Возвращает $$\log_{b} {x}$$, аргумент b является необязательным и
# по умолчанию имеет значение math.e
print("math.log10(", x, ") =", math.log10(x))
print("math.log1p(", x, ") =", math.log1p(x))  # Возвращает $$\log_{e} (1+x)$$; дает точные значения, даже когда
# значение x близко к 0
print("math.modf(", x, ") =", math.modf(x))  # Возвращает дробную и целую часть числа x в виде двух значений типа float






