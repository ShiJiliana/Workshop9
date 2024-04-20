n = 1
count = 0
while n != 0:
    if n > 2 and n % 2 == 0:
        count += 1
    n = int(input('Введите кол-во веревок: '))

print(count)