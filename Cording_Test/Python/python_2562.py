# https://www.acmicpc.net/problem/2562

arr = []
for _ in range(9):
    N = int(input())
    arr.append(N)

maxi = max(arr)
print(maxi)
print(arr.index(maxi)+1)