# https://www.acmicpc.net/problem/10815

sang_num = int(input())
num_1 = set(map(int, input().split()))

ck_num = int(input())
num_2 = list(map(int, input().split()))

arr= []

for n in num_2:
    if n in num_1:
        arr.append(1)
    else: 
        arr.append(0)

print(*arr)