# -*- coding: utf-8 -*-
import json

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    # 'Cookie': 'qm_check=A1sdRUIQChtxen8pI0dANi8zcX5zHBl+YnEhLyZIPxw8WkVRVRliYGBFVVdeSFk2VEdGX0kQc2gwRk9YAElKBQcABQ8AHRghDxUNGw1JcQYDEE9Daw06VkcYCyZPagceEH0DcAlUT0VEWhoSUFRZEgMSBBRVSldESFVKF0o%3D; PHPSESSID=gentt15b8vh86md1aj4i40n1lt; gr_user_id=2a7bbafd-c22e-42bc-a247-4027e1d34bd4; ada35577182650f1_gr_last_sent_cs1=qm24157426445; aso_ucenter=f627Sb47ms1stxgCP7NynrNxGhd1luxGXmy13DVYshCU93KRhIdFLB92aH75rWFjESs; AUTHKEY=lF2jNtEqax2gMQ2j8IXAai8kSC%2B56N%2B%2Fh%2BB%2FuE1TZyIEpcmbhURtCVOd1nxBPQkkNrSQEbUDfoKGdjbp%2BbAGtmJDvxyub0jIyjQLjlJryCyiMhk4p%2BtVuA%3D%3D; USERINFO=Ey6CczElpliXU6lZIOM10FrAN1onrsD3hGZ5wEWlZlzUTqJ2mq390UiA0u%2B2uAMSfiTstec3jdm7mTnP0ih92TOwxjwRrKPm1x3iCBLQm0JO0nbSQX6OhcGR5LSkvYoY6vsUY9iIWx6OAnh9mHz9fA%3D%3D; ada35577182650f1_gr_session_id=bf370755-f2dd-4fc7-a8ff-0f5184351dcd; ada35577182650f1_gr_last_sent_sid_with_cs1=bf370755-f2dd-4fc7-a8ff-0f5184351dcd; ada35577182650f1_gr_session_id_sent_vst=bf370755-f2dd-4fc7-a8ff-0f5184351dcd; ada35577182650f1_gr_cs1=qm24157426445; synct=1741603619.032; syncd=-2848',
}

params = {
    'page': 0
    # 'analysis': 'ex88Dwo/ARBXXFsUBSYAQz83WlU4WlVHUFkISwhXUgAeNwQNClVXQ1YNAD5QUkpWJ0tASUkCCAJQXFUKDiVFVA==',
    # 'brand': 'all',
    # 'device': 'iphone',
    # 'country': 'cn',
    # 'genre': '36',
}
pages_num = 10
for i in range(pages_num):
    pass
# urls = [f'https://api.qimai.cn/rank/indexPlus/brand_id/{i}' for i in range(3)]
# for url in urls:
#     resp = requests.get(url, params=params, headers=headers)
#     resp.encoding = 'utf-8'
#     data = json.loads(resp.text)
#     print(data['list'])




url = 'https://api.qimai.cn/rank/indexPlus/brand_id/0'
# for page in range(pages_num):

def get_data(page, url):
    params['page'] = page
    resp = requests.get(url, params=params, headers=headers)
    resp.encoding = 'utf-8'
    data = json.loads(resp.text)
    print(data['list'])
    page += 1


