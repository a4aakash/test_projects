import requests
import json


URL="http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    r=requests.get(url=URL, headers=headers, data=json_data)
    data=r.json()
    print(data)
get_data()

def post_data():
    data = {
        'name': 'Raj',
        'roll': 110,
        'city': 'delhi'
    }
    headers = {'content-type': 'application/json'}
    json_data = json.dumps(data)
    r=requests.post(url=URL, headers=headers, data=json_data)
    data=r.json()
    print(data)

# post_data()

def update_data():
    data = {
        'id': 6,
        'name': 'Swiki',
        'city': 'Hajipur'
    }
    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    r=requests.put(url=URL, headers=headers, data=json_data)
    data=r.json()
    print(data)

# update_data()

def delete_data():
    data = {'id': 6}
    json_data = json.dumps(data)
    r=requests.delete(url=URL, data=json_data)
    data=r.json()
    print(data)

# delete_data()