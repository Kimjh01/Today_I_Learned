# 아래 함수를 수정하시오.

class check():
    def __init__(self):
        pass

    def check_number(num):
        try:
            num = int(input('숫자를 입력하세요: '))
            if num > 0:
                ch = '양수'
            elif num < 0:
                ch = '음수'
            else: 
                ch = '0'
            return print(f'{ch}입니다.')
        
        except ValueError:
            print('잘못된 입력입니다.')
 
    
p1 = check()
for _ in range(5):
    p1.check_number()

