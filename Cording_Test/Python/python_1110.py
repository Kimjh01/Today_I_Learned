# https://www.acmicpc.net/problem/1110

num = input()
if len(num) == 1:
    num = '0' + num  

origin = num
count = 0

while True:
    total = str(int(num[0]) + int(num[1]))
    num = num[-1] + total[-1]
    count += 1
    if num == origin:
        break

print(count)
