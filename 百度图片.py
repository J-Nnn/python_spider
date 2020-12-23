import requests, os, time


def get_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'BDqhfp=python%26%260-10-1undefined%26%262333%26%264; BIDUPSID=F4E39A40BC0BE6B951EA4C3BC16F0E98; PSTM=1608616626; BAIDUID=F4E39A40BC0BE6B9B0BE704AE409CCD6:FG=1; H_PS_PSSID=1428_33243_33306_31660_32974_33285_33351_33313_33300_33312_33311_33310_32846_33309_26350_33308_33307_33237; BA_HECTOR=a1agal8504ah00a0vh1fu32li0q; BAIDUID_BFESS=F4E39A40BC0BE6B9B0BE704AE409CCD6:FG=1; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=www.baidu.com; firstShowTip=1; indexPageSugList=%5B%22python%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.0_N2VlMDVkMTgzMzg1YTEzNmY0NjJiY2JlM2Y5YjIzMmVhYjAwNWYzMDQ1ZWY5MDk1NGI1MjQ1NGViYWM4ZmY5MTY1YmYwZjMwNDEwYTk5NzJhNTBiMWI3ZTE5YmQxYzU5',
        'Connection': 'keep-alive',
    }
    i = 0
    while True:
        params = {
            'tn': 'resultjson_com',
            # 'logid': '7531560054304940326',
            'ipn': 'rj',
            'ct': '201326592',
            'fp': 'result',
            'queryWord': key,
            'cl': '2',
            'lm': '-1',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'st': '-1',
            'ic': '0',
            'word': key,
            'face': '0',
            'istype': '2',
            'nc': '1',
            'pn': str(i * 30),
            # 'pn': '30',
            'rn': '30',
        }

        response = requests.get(url, headers=headers, params=params)

        # 获取img的url
        num = 0
        for data in response.json()['data']:
            try:
                num += 1
                img_url = data['thumbURL']
                download_img(img_url,i,num)
            except:
                pass
        i += 1

# 图片下载
def download_img(url, i, num):
    time.sleep(0.2)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Cookie': 'BDqhfp=python%26%260-10-1undefined%26%262333%26%264; BIDUPSID=F4E39A40BC0BE6B951EA4C3BC16F0E98; PSTM=1608616626; BAIDUID=F4E39A40BC0BE6B9B0BE704AE409CCD6:FG=1; H_PS_PSSID=1428_33243_33306_31660_32974_33285_33351_33313_33300_33312_33311_33310_32846_33309_26350_33308_33307_33237; BA_HECTOR=a1agal8504ah00a0vh1fu32li0q; BAIDUID_BFESS=F4E39A40BC0BE6B9B0BE704AE409CCD6:FG=1; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=www.baidu.com; firstShowTip=1; indexPageSugList=%5B%22python%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.0_N2VlMDVkMTgzMzg1YTEzNmY0NjJiY2JlM2Y5YjIzMmVhYjAwNWYzMDQ1ZWY5MDk1NGI1MjQ1NGViYWM4ZmY5MTY1YmYwZjMwNDEwYTk5NzJhNTBiMWI3ZTE5YmQxYzU5',
    }
    response = requests.get(url, headers=headers)
    res = response.content
    # 创建图片名称
    img_name = str(i + 1) + '-' + str(num) + '.jpg'
    # 判断保存路径是否存在
    if not os.path.exists(dir_name):
        # 如果不存在创建路径
        os.makedirs(dir_name)
    # 保存图片
    with open(dir_name + '/' + img_name, 'wb', )as f:
        f.write(res)
    print(f'图片{img_name}下载成功')

def main():
    base_url = 'https://image.baidu.com/search/acjson?'
    get_content(base_url)
    # print(data)


if __name__ == '__main__':
    key = input('请输入要爬取的内容:')
    dir_name = '百度图片/' + key
    main()
