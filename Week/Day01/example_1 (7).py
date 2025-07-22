number = 3

double = number * 2
print("정수와 연산자 사용 3의 2배_1:", 3*2)
print("변수 사용 3의 2배_2:", double)

square = number ** 2
print("정수와 연산자 사용 3의 제곱:", 3**2)
print("변수 사용 3의 제곱:", square)

quotient = square // double
remainder = square % double
print("정수와 연산자 사용 몫:", 3**2//(3*2))
print("정수와 연산자 사용 나머지:", 3**2%(3*2))

print("변수 사용 몫:", quotient)
print("변수 사용 나머지:", remainder)

negative_square = (-number) ** 2  
result = square + (-negative_square)
print("정수와 연산자 사용 3^2 + (-3)^2 =", 3**2 + -3**2)
print("변수 사용 3^2 + (-3)^2 =", result)
