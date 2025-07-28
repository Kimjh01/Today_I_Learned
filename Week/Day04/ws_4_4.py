import requests
from pprint import pprint as print

API_URL = 'https://jsonplaceholder.typicode.com/users/'
censored_user_list = {}

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def censorship(company, name):
    if company in black_list:
        print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
        return False
    else:
        print("이상 없습니다.")
        return True

def create_user(user):
    company = user['company']['name']
    name = user['name']
    lng = float(user['address']['geo']['lng'])  
    lat = float(user['address']['geo']['lat'])

    user_data = {
        'name': name,
        'company': company,
        'lat' : lat,
        'lng' : lng,
    }
    if abs(lat) < 80 and abs(lng) < 80:
        user_data['lat'] = lat
        user_data['lng'] = lng
        if censorship(company, name): 
            censored_user_list[company] = [name]


for idx in range(10):
    response = requests.get(f'{API_URL}{idx + 1}')
    user_data = response.json()
    create_user(user_data)

print(censored_user_list)

