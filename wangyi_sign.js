const crypto = require('crypto');

// 测试参数
const testParams = {
    "le": "",
    "phonetic": "",
    "rate": 4,
    "word": "link",
    "type": "2",
    "id": ""
};

const SECRET_KEY = 'U3uACNRWSDWdcsKm';
const KEY_ID = 'voiceDictWeb';
const PRODUCT = 'webdict';
const KEY_FROM = 'dick';

/**
 * 生成网易词典API签名
 * @param {Object} params - 请求参数
 * @param {string} secretKey - 密钥
 * @param {string} keyId - keyId
 * @param {string} product - 产品标识
 * @param {string} keyFrom - 来源标识
 * @returns {Object} - 返回带签名的完整参数
 */
function generateSign(params, secretKey, keyId, product, keyFrom) {
    // 基础参数
    const baseParams = {
        product: product,
        appVersion: 1,
        client: 'web',
        mid: 1,
        vendor: 'web',
        screen: 1,
        model: 1,
        imei: 1,
        network: 'wifi',
        yduuid: 'abcdefg',
        keyfrom: keyFrom,
        keyid: keyId,
        mysticTime: Date.now()
    };

    // 合并参数
    let mergedParams = { ...baseParams, ...params };

    // 移除空值
    Object.keys(mergedParams).forEach(key => {
        if (mergedParams[key] === '') {
            delete mergedParams[key];
        }
    });

    // 排序参数键名
    let keys = Object.keys(mergedParams).sort().filter(key => 
        mergedParams[key] !== undefined
    );

    // 添加key参数
    keys.push('key');
    mergedParams.key = secretKey;

    // 拼接参数字符串
    let signStr = keys.map(key => `${key}=${mergedParams[key]}`).join('&');
    
    console.log('签名字符串：', signStr); // 调试用

    // 计算MD5签名
    let sign = crypto.createHash('md5')
        .update(signStr)
        .digest('hex');

    // 生成pointParam
    let pointParam = keys.join(',');

    // 返回完整参数
    return {
        ...mergedParams,
        sign: sign,
        pointParam: pointParam
    };
}

// 测试代码
function test() {
    const result = generateSign(
        testParams,
        SECRET_KEY,
        KEY_ID,
        PRODUCT,
        KEY_FROM
    );
    
    console.log('\n生成的签名结果：');
    console.log(JSON.stringify(result, null, 2));
    
    console.log('\n签名值：', result.sign);
    console.log('参数列表：', result.pointParam);
}

// 运行测试
test();

// 导出函数供其他模块使用
module.exports = {
    generateSign
}; 