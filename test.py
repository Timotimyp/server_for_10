import requests

print(requests.get('http://127.0.0.1:5000/api/sorted_keys').json()['q'])
print(requests.get('http://127.0.0.1:5000/api/get_position/Drinks').json()['position'])
print(requests.get('http://127.0.0.1:5000/api/get_info/Drinks/Banana').json()['info'])