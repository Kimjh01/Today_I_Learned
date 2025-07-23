def decrease_book():
    global number_of_book
    global number
    number_of_book -= number
    return f'남은 책의 수 : {number_of_book}'

def rental_book():
    global number, name
    return f'{name}님이 {number}권의 책을 대여하였습니다.'

number_of_book = 100
number = 3
name = '홍길동'

print(decrease_book())
print(rental_book())
