import requests,os
from lxml import etree
from excel_utils import write_to_excel,append_to_excel

# 获取内容页面
def get_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    }
    response = requests.get(url,headers=headers)
    # print(response.content.decode('utf-8'))
    # 返回的页面有乱码，所以下面进行了编码
    # 返回xml内容
    return etree.HTML(response.content.decode('utf-8'))

# 获取每个城市天气
def get_weather(city_content):
    # 遍历省份页面内容，提取出每个地区所在的tr标签列表
    tr_list = city_content.xpath('//div[@class="hanml"]/div[1]/div[@class="conMidtab3"]/table/tr')
    # print(tr_list)
    # 遍历提取出来的地区tr标签
    for tr in tr_list:
        # 创建一个空的天气列表 用于存放下面的item 并保存到xls文件里面
        weather_list = []
        # 城市名称
        city_name = tr.xpath('td/a/text()')[0]
        # 天气现象
        weather_name = tr.xpath('td[last()-6]/text()')[0]
        # 风向风力
        wind = tr.xpath('td[last()-5]/span/text()')
        # 最高气温
        max_temp = tr.xpath('td[last()-4]/text()')[0]
        # 最低气温
        min_temp = tr.xpath('td[last()-1]/text()')[0]
        # print(max_temp)
        # 定义一个字典 用于保存提取出来的天气信息等
        item = {}
        item['地区'] = city_name
        item['天气现象'] = weather_name
        item['风向风力'] = wind
        item['温度'] = item['温度'] = f'{min_temp}/{max_temp}℃'
        # print(item)
        weather_list.append(item)
        # 保存
        # 第一次调用写入excel的方法
        if not os.path.exists(filename):
            write_to_excel(weather_list, filename)
        # 第二次调用追加方法
        else:
            append_to_excel(weather_list, filename)

def main():
    # 确定目标url
    base_url = 'http://www.weather.com.cn/textFC/hb.shtml#'
    # 获取目标url首页内容
    content = get_content(base_url)
    # print(content)
    # 获取分类的省份url列表
    city_url_list = content.xpath('//div[@class="lqcontentBoxheader"]/ul/li/a/@href')
    # print(city_url_list)
    # 循环遍历省份url列表,获取每个省的的url
    for url in city_url_list:
        # 进行url拼接
        city_url = 'http://www.weather.com.cn'+url
        # print(city_url)
        # 进入省份页获取内容
        city_content = get_content(city_url)
        # print(city_content)
        # 获取天气信息
        get_weather(city_content)


if __name__ == '__main__':
    # 数据要保存的路径
    filename = '全国天气信息.xls'
    main()