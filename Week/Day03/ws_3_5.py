many_user = []
number_of_book = 100
number_of_rental = 0
number_of_people = -1
number = 0

name_list = ['김시습', '허균', '남영로', '임제', '박지원']
age_list = [20, 16, 52, 36, 60]
address_list = ['서울', '강릉', '조선', '나주', '한성부']

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(_=None): 
    increase_user()
    print(name_list[number_of_people], '님 환영합니다!')
    return {
        'name': name_list[number_of_people],
        'age': age_list[number_of_people],
        'address': address_list[number_of_people]
    }

def decrease_book(info):
    global number_of_book, number
    number = info['age'] // 10
    number_of_book -= number
    print('남은 책의 수 :', number_of_book)
    return number

def rental_book(info):
    decrease_book(info)
    print(info['name'], '님이', number, '권의 책을 대여하였습니다.')

list(map(create_user, range(len(name_list))))
many_user = list(map(lambda i: {'name': name_list[i], 'age': age_list[i], 'address': address_list[i]}, range(len(name_list))))
list(map(rental_book, many_user))