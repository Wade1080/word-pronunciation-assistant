# -*- coding: utf-8 -*-
import requests

cookies = {
    'OUTFOX_SEARCH_USER_ID_NCOO': '345466825.0203428',
    'OUTFOX_SEARCH_USER_ID': '806719546@183.237.194.91',
    '_uetsid': 'aa64be80fdae11ef868419672734d4e2',
    '_uetvid': 'aa64dec0fdae11efb217a97daf8ae355',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Range': 'bytes=0-',
    'Referer': 'https://www.youdao.com/',
    'Sec-Fetch-Dest': 'audio',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=345466825.0203428; OUTFOX_SEARCH_USER_ID=806719546@183.237.194.91; _uetsid=aa64be80fdae11ef868419672734d4e2; _uetvid=aa64dec0fdae11efb217a97daf8ae355',
}
params = {
    'product': 'webdict',
    'appVersion': '1',
    'client': 'web',
    'mid': '1',
    'vendor': 'web',
    'screen': '1',
    'model': '1',
    'imei': '1',
    'network': 'wifi',
    'keyfrom': 'dick',
    'keyid': 'voiceDictWeb',
    'mysticTime': '1741669033233',
    'yduuid': 'abcdefg',
    'le': '',
    'phonetic': '',
    'rate': '4',
    'word': 'link',
    'type': '2',
    'id': '',
    'sign': 'c9ed37844284fd7dec5362847b0a4f74',
    'pointParam': 'appVersion,client,imei,keyfrom,keyid,mid,model,mysticTime,network,product,rate,screen,type,vendor,word,yduuid,key',
}
response = requests.get(
    'https://dict.youdao.com/pronounce/base',
    cookies=cookies,
    headers=headers,
    params=params
)
print(response.status_code)
