number_of_people = -1
user_info = []

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

user_info = list(map(create_user, range(len(name_list))))

print(user_info)
