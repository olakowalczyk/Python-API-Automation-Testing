import requests
import json

class HttpManager:
    headers = {'Content-Type': 'application/json'}
    

    @staticmethod
    def auth(url, user, password):
        data = json.dumps({
        'username': user,
        'password': password
    })
        response = requests.post(url, headers=HttpManager.headers, data=data)
        response_json = json.loads(response.text)
        HttpManager.headers['Cookie'] = response_json['token']
