import requests,re,os

# 获取贴吧整页内容
def get_content(url):
    response = requests.get(url,headers=headers)
    return response.text

# 提取图片
def get_img(img_url_list):
    # 保存路径
    dir_name = '1.tieba_img/'+key
    #遍历
    for img_url in img_url_list:
        respone = requests.get(img_url,headers=headers)
        res = respone.content
        print(res)
        # 进行分割取图片名称
        img_name = img_url.split('/')[-1]
        # 判断保存路径舒服存在
        if not os.path.exists(dir_name):
            # 如果不存在创建路径
            os.makedirs(dir_name)
        # 保存图片
        with open(dir_name+'/'+img_name,'wb',)as f:
            f.write(res)

def main():
    # 确定目标url
    base_url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
    # 实现分页
    for i in range(start-1,end):
        page = get_content(base_url.format(key,i*50))
        # 使用正则提取图片url
        img_url_list = re.findall(r'<ul class="threadlist_media.*?<img src="" attr=".*?jpg"  bpic="(.*?)" class=',page,re.S)
        # 实现图片提取
        get_img(img_url_list)
        # print(page)


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    # 爬取的贴吧名称
    key = input('请输入贴吧名称：')
    # 爬取的开始页
    start = int(input('请输入开始页：'))
    # 爬取的结束页
    end = int(input('请输入结束页：'))
    main()