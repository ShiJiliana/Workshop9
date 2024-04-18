n = []
for i in range(10, 100):
    if i // 10 != i % 10:
        n.append(i)

for i in n:
    k = i * i
    if k < 1000 and k % 100 == i:
        print(k)
#Ответ: 625