n = int(input())
d = 0
for i in range(0, n + 1):
    for j in range(0, n+1):
        if i == j:
            d += 2*i
        if i != j:
            d += 0.5*(i+j)
print(int(d))
