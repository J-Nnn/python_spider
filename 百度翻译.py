import requests

def get_content(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    data = {
        'kw': key
    }
    response = requests.post(url,headers=headers,data=data)
    # print(response.json())
    return response.json()


def main():
    basr_url = 'https://fanyi.baidu.com/sug'
    res = get_content(basr_url)
    item = {}
    for data in res['data']:
        # print(data)
        item['英文'] = data['k']
        item['中文'] = data['v']
        print(item)



if __name__ == '__main__':
    key = input('请输入要翻译的内容：')
    main()