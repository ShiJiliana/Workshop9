n, d, r = map(int, input().split()) #n = 3
l = (d * 2 + r * 2) + (((r + d) + ((r + d) - d * 2)) * (n - 1))
print(l)