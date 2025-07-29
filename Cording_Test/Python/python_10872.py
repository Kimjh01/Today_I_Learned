# https://www.acmicpc.net/problem/10872

number = 1 
N = int(input())
for i in range(1, N):
    number *= i
print(number)

'''
N = int(input())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(N))
'''