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
print("Сумма х+у: ", x+y)

print("Деление ", x/y); print("Деление без остатка", x//y)   # можно поставить ; в конце каждой строки, как вы привыкли
# в С++, ругается PEP8
print("Остаток от деления ", x % y)

x += 1  # Увеличиваем на 1
b = bool(7)  # преобразуем 7 в bool возвращает True
print(b)

