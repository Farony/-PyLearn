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
number_lessons = input("Введите количество уроков: ")

les_length = 45
break_length = 5



