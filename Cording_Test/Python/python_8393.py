# https://www.acmicpc.net/problem/8393

num = int(input())
result = 0
for idx in range(1, num+1):
    result += idx
    
print(result)