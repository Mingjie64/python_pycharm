import requests
import xlrd,xlwt,xlutils
from get_token import get_token

# def excel_add_single_page():
#     data = xlrd.open_workbook()
#     url = 'http://crm-dev.dm-cube.com/crm/pageConfig/addPage'
#     payload = {
#         "floatModelId": ,
#         "marqueeModelIds": [632],
#         "modelType": 1,
#         "pageName": "1",
#         "popModelId": 611,
#         "remarkExplain": "1",
#         "renderType": 1,
#         "sourceExplain": "1",
#         "sourceType": 0
#     }
#     res = requests

# url = 'http://crm-test.dm-cube.com/crm/dmp/quartzJob/add'
# header = {
#             "Content-Type": "application/json",
#             "X-Access-Token": get_token('test')
#           }
# payload = {"jobCycle":"","jobName":"微信首次关注120分钟后推送","tagCode":["Loan_Not_FenQiLe_Age","no_anyihua_age_22_45"],"jobType":3,"eventCode":"NxR82dB7Sg4sVQ0o699MsmsWvhUxDoSn","execDate":"undefined","execTime":"undefined","configList":[{"configId":None,"wechatAccount":["mingjie"],"distributeType":5,"msgTemplateCode":"Xf2G99mg69Vw8Uab3nfnLe02b8oOa9EV"}]}
# res = requests.post(url=url,json=payload,headers=header)
# 
# print(res.json())