n = int(input('Введите кол-во упаковок мороженого: '))
dividers = []
d = 0
for i in range(1, n + 1):
    if n % i == 0:
        dividers.append(i)
        d += 1
if n == 2:
    result = n
else:
    result = dividers[1]

print(result)