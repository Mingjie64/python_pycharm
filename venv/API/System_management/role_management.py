import requests
import pprint
from get_token import get_token
import json

Environmental_Science = 'dev'  #请输入请求的环境 test or dev...
def get_roleid(roleName):
    url = f'http://crm-{Environmental_Science}.dm-cube.com/crm/sys/role/list?_t=1605507756&column=createTime&order=desc&field=id,,,roleName,roleCode,description,createTime,updateTime,action&pageNo=1&pageSize=60'
    header = {
                "Content-Type": "application/json",
                "X-Access-Token": get_token(Environmental_Science)
    }
    res = requests.get(url=url,headers=header)
    total = res.json()['result']['total']
    roleid = []
    for i in range(0,total):
        roleid.append(res.json()['result']['records'][i])
    for y in roleid:
        # print(y)
        if y['roleName'] == roleName:
            roleid = y['id']
            print(roleid)
    return roleid

def get_role_permissions_list(button_name):  #请输入按钮的名称 查询、导出、新增.....
    url = f'http://crm-{Environmental_Science}.dm-cube.com/crm/sys/role/queryTreeList?_t=1605513356'
    header = {
                "Content-Type": "application/json",
                "X-Access-Token": get_token(Environmental_Science)
    }
    res = requests.get(url=url,headers=header)
    pprint.pprint(len(res.json()['result']['treeList']))
    secondary_menu = []
    amount = 0
    skip = []
    c = 0
    b = 0
    button_key = []
    for i in range(0,19):
        if res.json()['result']['treeList'][i]['children'] != None:
            secondary_menu.append(len(res.json()['result']['treeList'][i]['children']))
            amount+=1  #有效条数
        else:
            skip.append(i)  #跳过
    for y in range(c,amount):
        if y in skip:
            print('skip')
        else:
            for xx in range(0,secondary_menu[b]):
                if res.json()['result']['treeList'][y]['children'][xx]['children'] != None:
                    button = len(res.json()['result']['treeList'][y]['children'][xx]['children'])  #全部按钮的数量
                    # print(res.json()['result']['treeList'][y]['children'][xx]['children'])  #可以查看全部按钮
                    for xxx in range(0,button):
                        if res.json()['result']['treeList'][y]['children'][xx]['children'][xxx]['slotTitle'] == button_name:
                            button_key.append(res.json()['result']['treeList'][y]['children'][xx]['children'][xxx]['key'])

    return button_key


# get_role_permissions_list('')
def queryRolePermission(button_name):  #查询出所有选中的按钮
    url = f'http://crm-{Environmental_Science}.dm-cube.com/crm/sys/permission/queryRolePermission?_t=1605578557&roleId={button_name}'
    header = {
                "Content-Type": "application/json",
                "X-Access-Token": get_token(Environmental_Science)
    }
    res = requests.get(url=url,headers=header)
    return res.json()['result']

def saveRolePermission(roleName,button_name):
    b = []
    b = get_role_permissions_list(button_name) + queryRolePermission(button_name)
    b = list(set(b))
    c = (',').join(str(c)for c in b)
    url = 'http://crm-dev.dm-cube.com/crm/sys/permission/saveRolePermission'
    header = {
                "Content-Type": "application/json",
                "X-Access-Token": get_token(Environmental_Science)
    }
    payload = {
                "permissionIds": c,
                "roleId": get_roleid(roleName)
    }
    res = requests.post(url=url,json=payload,headers=header)
    return print(res.json())

# saveRolePermission('测试3','查询')
