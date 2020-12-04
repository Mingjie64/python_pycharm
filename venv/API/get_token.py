import requests
import json
import pprint


def get_token(Environmental_Science):  #输入请求的环境
    token_url = f'http://crm-{Environmental_Science}.dm-cube.com/crm/sys/login'
    token_header = {'Content-Type': 'application/json'}
    token_payload = {
                'captcha': "123456",
                'captchaToken': "5d9d3e41e04148fb92ed9a946075341b",
                'password': "V+3+e6ecRQfqjJ9vhFQDW2kJ7huzPmPa4U9XpYlSthkhLFg5uJgDyBJQwIwd05O6iyK0+UCs9RISPzHiqWFmOwTLml8p193zvUQvtdJp6/4p1mQPg2btqt4stMSOKa4bH8UXZtDqIiyv1LGFzB5sKoUPBcwyFu/So9QH5OK/qI8=",
                'username': "admin"
    }

    res = requests.post(url=token_url,json=token_payload)
    return res.json()['result']['token']

