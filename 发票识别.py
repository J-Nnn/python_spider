# 数字字母汉字识别验证码

from selenium import webdriver
# 定位器
from selenium.webdriver.common.by import By
# 条件
from selenium.webdriver.support import expected_conditions as EC
# 显示等待对象
from selenium.webdriver.support.wait import WebDriverWait
# 抠图模块
from PIL import Image
# 超级鹰打码平台
from chaojiying import Chaojiying_Client

def main():
    # 请求url
    driver.get('https://inv-veri.chinatax.gov.cn/')
    # 发票代码
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="fpdm"]'))).send_keys('发票代码')
    # 发票号码
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="fphm"]'))).send_keys('发票号码')
    # 开票日期
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="kprq"]'))).send_keys('开票日期')
    # 校验码
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="kjje"]'))).send_keys('校验码')
    # 点击加载验证码 使用js方式
    driver.execute_script('document.getElementById("yzm_img").click()')
    input('按回车进行截图:')
    # 截屏
    driver.save_screenshot('15.quan.png')
    # 验证码元素
    yzm_windows = driver.find_element_by_xpath('//*[@id="yzm"]')
    # 验证码输入框坐标
    location = yzm_windows.location
    # 验证码输入框大小
    size = yzm_windows.size
    # print(location,size)
    # 抠图坐标  左(x)，上(y)，右(x+width)，下(y+height)
    crop_prams=(location['x']-10,  # 左
                location['y'], # 上
                location['x']+size['width']+220,
                location['y'] + size['height']+75)
    image = Image.open('quan.png')
    image_part = image.crop(crop_prams)
    image_part.save('part.png')

    # 调用超级鹰
    chaojiying = Chaojiying_Client()
    im = open('part.png', 'rb').read()
    yzm_code = chaojiying.PostPic(im, 5000)
    print(yzm_code)

    # 阻塞一下
    input('请再次输入回车进行验证:')
    # 输入验证码
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="yzm"]'))).send_keys(yzm_code)
    # 点击查验按钮
    driver.execute_script('document.getElementsByClassName("blue_button")[0].click()')

if __name__ == '__main__':
    # 创建浏览器驱动
    driver = webdriver.Ie()
    driver.maximize_window()
    # 显示等待对象
    wait = WebDriverWait(driver,20)
    main()