import requests
import get_token

# url = 'http://crm-dev.dm-cube.com/crm/wechatMessage/li'
# header = {
#             'Content-Type': 'application/json',
#             'X-Access-Token': get_token()
#           }
# res = requests.get(url=url,headers=header)
# print(res.json())

# 消息模板：先拿模板ID
def get_templateId(inTitle):  # 请输入你要使用的模板标题
    url = 'http://crm-dev.dm-cube.com/crm/wechatMessage/listWechatTemplate?_t=1604633301&column=createTime&orderBy=1&pageNum=1&pageSize=10&account=mingjie'
    header = {
        'Content-Type': 'application/json',
        'X-Access-Token': get_token()
    }
    res = requests.get(url=url, headers=header)

    shuliang = len(res.json()['payload'])
    for i in range(0, shuliang):
        title = res.json()['payload'][i]['title']
        if title == inTitle:
            num = i
            break
    return res.json()['payload'][num]['templateId']

# 消息模板：拿到模板ID后执行新增操作
def create_message_template(inTitle):  # 请输入你要使用的模板标题
    header = {
        'Content-Type': 'application/json',
        'X-Access-Token': get_token()
    }
    url = "http://crm-dev.dm-cube.com/crm/dmp/messageTemplate/updateMessageTemplate"

    payload = {
        "account": "mingjie",
        "data": '{"result":{"value":"result","color":"#F50C0C"},"withdrawMoey":{"value":"withdrawMoey","color":"#F9ED05"},"withdrawTime":{"value":"withdrawTime","color":"#DADADA"},"cardIfo":{"value":"cardIfo","color":"#3D3D3D"},"arrivedTime":{"value":"arrivedTime","color":"#A1FB05"},"remark":{"value":"remark","color":"#47C5A8"}}',
        "templateId": get_templateId(inTitle),
        "templateName": 'cs3',
        "templateType": 5,
        "url": "http://www.baidu.com"
    }

    res = requests.post(url=url, json=payload, headers=header)
    print(res.status_code, res.json(), print("响应总时长", res.elapsed.total_seconds()))