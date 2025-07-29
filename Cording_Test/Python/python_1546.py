# https://www.acmicpc.net/problem/1546

N = int(input())
score = list(map(float, input().split()))
M = max(score)
average = 0
for i in range(N):
    average += (score[i] / M)*100 

print(average/N)