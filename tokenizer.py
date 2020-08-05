import requests
import json


class Tokenizer(object):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty'
        }
    
    headers2 = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'content-type': 'application/json',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty'
    }

    client= requests.Session()

    def captchaSend(self):
        r = self.client.get('https://ecomm.ynap.biz/api/captcha/new/NAP/en/', headers=self.headers)
        return r.json()

    def solution(self, payload):
        r = self.client.post('https://ecomm.ynap.biz/api/captcha/verify', headers = self.headers2, data=json.dumps(payload))
        return r.status_code

    def register(self, header, cookie, payload):
        r =self.client.post('https://www.net-a-porter.com/gb/en/emailUpdatesRegistration.nap', headers=header, cookies=cookie, data= payload)
        return r.status_code
