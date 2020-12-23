# 文字点选验证码
# 运行代码之前，Windows系统的显示缩放比要调成100%
# 如果缩放比例不为100%时，抠图抠的位置会错误

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
import time
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.action_chains import ActionChains

def login():
    # 请求url
    driver.get('https://passport.bilibili.com/login')
    # 用户名输入
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-username"]'))).send_keys('17739626050')
    # 密码输入
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-passwd"]'))).send_keys('jin12300')
    # 点击登陆
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="geetest-wrap"]/div/div[5]/a[1]'))).click()
    # 阻塞
    # input('按回车进行截图:')
    time.sleep(2)

    # 调用图片处理方法
    photoshop()

def photoshop():
    # 截图
    driver.save_screenshot('quan.png')

    # 获取验证码元素
    yzm_windows = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[6]/div/div')))
    # 获取验证码输入框坐标
    location = yzm_windows.location
    # 获取验证码输入框大小
    size = yzm_windows.size
    # print(location,size)
    # 抠图坐标  左(x)，上(y)，右(x+width)，下(y+height)
    crop_prams = (location['x'],  # 左
                  location['y'],  # 上
                  location['x'] + size['width'],
                  location['y'] + size['height'])
    image = Image.open('quan.png')
    image_part = image.crop(crop_prams)
    image_part.save('part.png')
    # 调用验证码处理方法
    handle_code(yzm_windows)

# 验证码处理
def handle_code(yzm_windows):
    # 调用超级鹰
    chaojiying = Chaojiying_Client()
    im = open('part.png', 'rb').read()
    code_coord  = chaojiying.PostPic(im, 9004)
    print(code_coord)
    # 等待
    time.sleep(20)
    # input('回车')

    # 打码平台返回的多个坐标进行处理
    coord_list = code_coord.split('|')
    for coord in coord_list:
        x = coord.split(',')[0]
        y = coord.split(',')[1]
        ActionChains(driver).move_to_element_with_offset(yzm_windows,xoffset=int(x),yoffset=int(y)).click().perform()

   # 等待
    time.sleep(5)
    # 点击登陆
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/div[6]/div/div/div[3]/a'))).click()

def main():
    login()

if __name__ == '__main__':
    # 创建驱动
    driver = webdriver.Chrome()
    # 最大化
    driver.maximize_window()
    # 创建显示等待对象
    wait = WebDriverWait(driver, 20)
    main()