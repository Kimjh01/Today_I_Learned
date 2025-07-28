import requests
from pprint import pprint as print
 
API_URL = 'https://jsonplaceholder.typicode.com/users/'
dummy_data = []

for idx in range(10):
    response = requests.get(f'{API_URL}{idx + 1}')
    parsed_data = response.json()

    company_name = parsed_data['company']['name']
    lng = float(parsed_data['address']['geo']['lng'])  
    lat = float(parsed_data['address']['geo']['lat'])
    name = parsed_data['name']

    user_data = {
        'name': name,
        'company': company_name,
        'lat' : lat,
        'lng' : lng,
    }

    if abs(lat) < 80 and abs(lng) < 80:
        user_data['lat'] = lat
        user_data['lng'] = lng
        dummy_data.append(user_data)

print(dummy_data)
