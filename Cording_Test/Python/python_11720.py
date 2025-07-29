# https://www.acmicpc.net/problem/11720

total = 0
N = int(input())
num = int(input())

for _ in range(N):
    total += num % 10
    num //= 10

print(total)