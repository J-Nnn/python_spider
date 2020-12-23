import requests
import time,random,hashlib

def translate(key):
    base_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Referer': 'http://fanyi.youdao.com/',
        'Origin': 'http://fanyi.youdao.com',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-605181805@10.108.160.100; JSESSIONID=aaafpo27YDn9ehIoz_dAx; OUTFOX_SEARCH_USER_ID_NCOO=1120963885.6050303; ___rl__test__cookies=1608531965479'
    }

    ts = str(int(time.time()*1000))
    salt = ts + str(random.randint(0,9))
    text = "fanyideskweb" + key + salt + "Tbh5E8=q6U3EXe+&L[4c@"
    sing = hashlib.md5(text.encode('utf-8')).hexdigest()
    data = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sing,
        'lts': ts,
        'bv': '0785986963146aebf8c240a24088d066',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    response = requests.post(base_url,headers=headers,data=data)
    print(response.json())

if __name__ == '__main__':
    key = input('请输入翻译内容:')
    translate(key)