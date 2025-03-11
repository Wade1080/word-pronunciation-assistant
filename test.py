# -*- coding: utf-8 -*-
import requests

word = input('请输入要下载的单词发音')

url = 'http://localhost:5000/api/pronounce'
params = {
    'word': word
}
requests.get(url,params=params)
