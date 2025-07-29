# https://www.acmicpc.net/problem/4673

def d(n):
    s = n
    for digit in str(n):
        s += int(digit)
    return s

limit = 10000
generated = set()

for i in range(1, limit + 1):
    generated.add(d(i))

for i in range(1, limit + 1):
    if i not in generated:
        print(i)
