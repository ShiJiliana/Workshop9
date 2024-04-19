n = int(input())
d = 0
for x in range(0, n + 1):
    for y in range(0, n+1):
        if x == y:
            d += 2*x
        if x != y:
            d += 0.5*(x+y)
print(int(d))
