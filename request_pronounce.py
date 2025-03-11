import requests
import hashlib
from datetime import datetime

def generateSign(params, secretKey, keyId, product, keyFrom):
    # 基础参数
    baseParams = {
        "product": product,
        "appVersion": 1,
        "client": "web",
        "mid": 1,
        "vendor": "web",
        "screen": 1,
        "model": 1,
        "imei": 1,
        "network": "wifi",
        "yduuid": "abcdefg",
        "keyfrom": keyFrom,
        "keyid": keyId,
        "mysticTime": int(datetime.now().timestamp() * 1000)
    }

    # 合并参数
    mergedParams = {**baseParams, **params}

    # 移除空值
    mergedParams = {k: v for k, v in mergedParams.items() if v != ""}

    # 排序参数键名
    keys = sorted([k for k in mergedParams.keys() if mergedParams[k] is not None])

    # 添加key参数
    keys.append("key")
    mergedParams["key"] = secretKey

    # 拼接参数字符串
    signStr = "&".join([f"{k}={mergedParams[k]}" for k in keys])
    print("签名字符串：", signStr)

    # 计算MD5签名
    md5 = hashlib.md5()
    md5.update(signStr.encode('utf-8'))
    sign = md5.hexdigest()

    # 生成pointParam
    pointParam = ",".join(keys)

    # 返回完整参数
    return {
        **mergedParams,
        "sign": sign,
        "pointParam": pointParam
    }

def get_pronounce(word):
    # 基础参数
    params = {
        "le": "",
        "phonetic": "",
        "rate": 4,
        "word": word,
        "type": "2",
        "id": ""
    }

    # 获取要下载的单词
    word = params["word"]
    # 构建文件名
    filename = f"pronounce_{word}.mp3"

    # 生成签名
    result = generateSign(
        params,
        "U3uACNRWSDWdcsKm",  # SECRET_KEY
        "voiceDictWeb",      # KEY_ID
        "webdict",           # PRODUCT
        "dick"               # KEY_FROM
    )

    # 请求URL
    url = "https://dict.youdao.com/pronounce/base"

    # 请求头
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=345466825.0203428; OUTFOX_SEARCH_USER_ID=806719546@183.237.194.91",
        "Pragma": "no-cache",
        "Range": "bytes=0-",
        "Referer": "https://www.youdao.com/",
        "Sec-Fetch-Dest": "audio",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }

    # 从result中获取所有参数
    params = {k: v for k, v in result.items() if k != "key"}  # 移除key参数，它不需要在URL中

    try:
        # 发送请求
        response = requests.get(url, params=params, headers=headers)
        
        # 检查响应状态
        if response.status_code == 200:
            # 保存音频文件
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"发音文件已保存为 {filename}")
        else:
            print(f"请求失败，状态码：{response.status_code}")
            print("响应内容：", response.text)
            
    except Exception as e:
        print(f"发生错误：{str(e)}")

if __name__ == "__main__":
    word = input('请输入待查读音的单词：')
    get_pronounce(word)