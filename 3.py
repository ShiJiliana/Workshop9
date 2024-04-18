n = int(input('Введите кол-во упаковок мороженого: '))
delitel = []
d = 0
for i in range(1, n + 1):
    if n % i == 0:
        delitel.append(i)
        d += 1
if n == 2:
    result = n
else:
    result = delitel[1]

print(result)