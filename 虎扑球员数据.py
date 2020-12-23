import requests,os
from lxml import etree
from excel_utils import write_to_excel,append_to_excel

def get_content(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    return etree.HTML(response.text)

def get_xpath_data(tree):
    # 列名
    lieming = tree.xpath('//table[@class="players_table"]/tbody/tr[1]/td/text()')
    # tr 标签列表
    tr_lists = tree.xpath('//table[@class="players_table"]/tbody/tr[position()>1]')
    for tr in tr_lists:
        nba_list = []
        data = tr.xpath('./td/text()|./td/a/text()')
        # print(data)
        item = {}
        item[lieming[0]] = data[0]
        item[lieming[1]] = data[1]
        item[lieming[2]] = data[2]
        item[lieming[3]] = data[3]
        item[lieming[4]] = data[4]
        item[lieming[5]] = data[5]
        item[lieming[6]] = data[6]
        item[lieming[7]] = data[7]
        item[lieming[8]] = data[8]
        item[lieming[9]] = data[9]
        item[lieming[10]] = data[10]
        item[lieming[11]] = data[11]
        nba_list.append(item)
        print(nba_list)

        # 保存
        # 第一次调用写入excel的方法
        # if not os.path.exists(filename):
        #     write_to_excel(data, filename)
        # # 第二次调用追加方法
        # else:
        #     append_to_excel(data, filename)

def main():
    base_url = 'https://nba.hupu.com/stats/players/pts/%s'
    for i in range(1,4):
        tree = get_content(base_url %i)
        get_xpath_data(tree)

if __name__ == '__main__':
    filename = 'data/17.nba_data.xls'
    main()