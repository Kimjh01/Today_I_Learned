import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'
dummy_data=[]

# API 요청
for idx in range(10):
    response = requests.get(f'{API_URL}{idx+1}')
    # JSON -> dict 데이터 변환
    parsed_data = response.json()
    name = parsed_data['name']
    dummy_data.append(name)
        
# 특정 데이터 출력
print(dummy_data)
