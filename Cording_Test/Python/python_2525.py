# https://www.acmicpc.net/problem/2525

hour, minute = map(int, input().split())
cook = int(input())

total_minutes = hour * 60 + minute + cook

hour = (total_minutes // 60) % 24
minute = total_minutes % 60

print(hour, minute)
