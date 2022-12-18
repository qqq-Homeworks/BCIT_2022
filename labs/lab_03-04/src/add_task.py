a = [i for i in range(10)]

b = [(i, i * i) for i in a]
print(b)

b = list(map(lambda i: (i, i * i), a))
print(b)

b = list(zip(a, [i * i for i in a]))
print(b)

b = list(zip(a, list(map(lambda i: i * i, a))))
print(b)