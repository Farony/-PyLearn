x = -234
if x < 0:
    x = -x
    print('Change sign')
print('Absolute value is', x)

if x%2 == 0:
    print('even')
else:
    print('odd')


width = 100 + (10 if x > 0 else 20)
print(width)

offset = 10
if x > 0:
    offset = 20
print(offset)
# можно в одну строку
offset = 10 if x < 0 else 35
print(offset)

# операторы сравнения
a = ["xyz", 3, None]
b = ["xyz", 3, None]
c = ["xyz", 5, None]
d = 3
e = a

if a == b:
    print("a = b")

if a != c:
    print("a != c")
else:
    print("a = c")

if d in b:
    print("d in b")

if e is a:
    print("e is a")

# циклы
n = 10
i = 1
sumi = 0
while i <= n:
    sumi += i
    i += 1
print(sumi)

for x in 'Hello':
    print(x, end=" ")

print()
i = 1
ind = -1
k = "l"
for x in 'Hello':
    i += 1
    if i % 2 != 0:  # пропускаем каждый второй символ
        continue  # пропускаем интерацию цикла
    print(i, x, end=" ")
print()

i = 0
ind = -1
k = "l"
for x in 'Hello':
    if x == k:
        ind = i
        break  # прерывание цикла
    i += 1
print(ind)

k = "h"
for x in 'Hello':
    if x == k:
        print('YES')    # печатаем YES и выходим из цикла
        break
else:
    print('NO')         # если break не было, печатаем NO

r = range(10)
for x in r:
    print(x)

for x in range(3, 10):  # с указаным началом
    print(x)

for x in range(3, 10, 2):
    print(x)

for i, x in enumerate('Hello'):
    print(i, x)
