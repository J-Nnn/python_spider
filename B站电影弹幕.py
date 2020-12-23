# 八佰电影弹幕
import requests,re

def get_content(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'cookie': '登录后的cookie',
    }
    response = requests.get(url,headers=headers)
    return response.content.decode('utf-8')

def parse_content(xml_data):
    # 弹幕
    barrage_list = re.findall(r'<d p=".*?">(.*?)</d>',xml_data)
    for barrage in barrage_list:
        # # 保存
        # with open('八佰弹幕.txt', 'a', encoding='utf-8') as f:
        #     f.write(f'{barrage}\n')
        print(barrage)


def main():
    base_url = 'https://api.bilibili.com/x/v2/dm/history?type=1&oid=250981350&date=2020-12-22'
    xml_data = get_content(base_url)
    parse_content(xml_data)

if __name__ == '__main__':
    main()