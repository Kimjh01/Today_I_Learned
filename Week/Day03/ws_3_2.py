number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    increase_user()
    print(f'{name}님 환영합니다!')
    return {'name': name, 'age': age, 'address': address}

print('현재 가입 된 유저 수 :', number_of_people)

user_info = create_user('홍길동', 30, '서울')

print(user_info)
print('현재 가입 된 유저 수 :', number_of_people)
