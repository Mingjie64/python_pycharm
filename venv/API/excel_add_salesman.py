import requests
from get_token import get_token

import xlrd


def excel_add_salesman():

    data = xlrd.open_workbook('接口测试测试用例模板.xlsx')
    sheet = data.sheet_names()

    url = 'http://crm-dev.dm-cube.com/crm/salesman/saveSalesman'
    header = {
                'Content-Type': 'application/json',
                'X-Access-Token': f"{get_token()}"
    }
    payload = {
                # 'companyId': 30,           #经理必填，id 30 为杰出总公司
                'identityNo': f"{id_card3()}",
                'managerId': 260,          #经理不填,业务员必填
                'name': "明明",
                'phone': f"{phone3()}",
                'position': 2,             #1.经理 2.业务员
                'positionStatus': 1        #1.在职 0.离职
    }

    res = requests.post(url=url,json=payload,headers=header)

    print(res.status_code,res.text)