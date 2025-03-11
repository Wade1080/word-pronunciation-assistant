from flask import Flask, send_file, request, jsonify, render_template
import requests
import hashlib
from datetime import datetime
import os
import io
import json

app = Flask(__name__)

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

@app.route('/api/pronounce', methods=['GET'])
def get_pronounce():
    try:
        # 从请求参数中获取单词
        word = request.args.get('word', '')
        if not word:
            return jsonify({
                "success": False,
                "error": "请提供要发音的单词"
            }), 400

        # 基础参数
        params = {
            "le": "",
            "phonetic": "",
            "rate": 4,
            "word": word,
            "type": "2",
            "id": ""
        }

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
        params = {k: v for k, v in result.items() if k != "key"}

        # 发送请求
        response = requests.get(url, params=params, headers=headers)
        
        # 检查响应状态
        if response.status_code == 200:
            # 创建内存文件对象
            audio_io = io.BytesIO(response.content)
            return send_file(
                audio_io,
                mimetype='audio/mpeg',
                as_attachment=True,
                download_name=f'pronounce_{word}.mp3'
            )
        else:
            return jsonify({
                "success": False,
                "error": f"获取发音失败，状态码：{response.status_code}"
            }), response.status_code
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/word_info', methods=['GET'])
def get_word_info():
    try:
        word = request.args.get('word', '')
        if not word:
            return jsonify({
                "success": False,
                "error": "请提供要查询的单词"
            }), 400

        # 请求有道词典API获取翻译和例句
        url = "https://dict.youdao.com/jsonapi"
        params = {
            "q": word,
            "dicts": json.dumps({
                "count": 10,
                "dicts": [["ec"], ["web_trans"], ["fanyi"], ["blng_sents_part"]]
            })
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            "Referer": "https://www.youdao.com/"
        }

        response = requests.get(url, params=params, headers=headers)
        if response.status_code != 200:
            return jsonify({
                "success": False,
                "error": f"获取单词信息失败，状态码：{response.status_code}"
            }), response.status_code

        data = response.json()
        
        # 解析返回数据
        result = {
            "word": word,
            "translations": [],
            "examples": []
        }

        # 获取翻译
        if "ec" in data and "word" in data["ec"]:
            for trs in data["ec"]["word"][0]["trs"]:
                if "tr" in trs and "l" in trs["tr"][0]:
                    result["translations"].append(trs["tr"][0]["l"]["i"])

        # 获取例句
        if "blng_sents_part" in data:
            sentences = data["blng_sents_part"].get("sentence-pair", [])
            for sent in sentences[:3]:  # 只取前3个例句
                result["examples"].append({
                    "en": sent.get("sentence", ""),
                    "cn": sent.get("sentence-translation", "")
                })

        return jsonify({
            "success": True,
            "data": result
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    # 启动Flask服务
    app.run(host='0.0.0.0', port=5000, debug=True) 