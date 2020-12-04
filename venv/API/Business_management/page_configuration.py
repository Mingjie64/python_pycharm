import requests
from get_token import get_token
import pprint

def floatModels_marqueeModels_popModels():
    url = 'http://crm-dev.dm-cube.com/crm/pageConfig/list'
    header = {
                "Content-Type": "application/json",
                "X-Access-Token": get_token()
    }
    res = requests.post(url=url,json={},headers=header)
    floatModels = res.json()['payload']['floatModels'][0]['id']
    marqueeModels = res.json()['payload']['marqueeModels'][0]['id']
    popModels = res.json()['payload']['popModels'][0]['id']

    return floatModels,marqueeModels,popModels

print(floatModels_marqueeModels_popModels())