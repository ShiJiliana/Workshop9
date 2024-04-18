import math
n = int(input('Введите положительное число больше 2: '))
while math.sqrt(n) > 2:
    n = math.sqrt(n)
    print(f'{n:.3f}')
n = math.sqrt(n)
print(f'{n:.3f}')