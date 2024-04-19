x = int(input('Введите натуральное число x: '))
count = 0
for a in range(1, int(x ** 0.5) + 1):
    b = int((x - a ** 2) ** 0.5)
    if a ** 2 + b ** 2 == x and a <= b:
        print(a, b)
        count += 1

print('Количество способов:', count)


