#-*- coding: utf-8 -*-
'''
1. 输入框按钮Radio，如性别的选择
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("file:///C:/Users/tntjoy3/Desktop/radio.html")   #本地链接
print(driver.title)

print("默认选中male，2秒后选择female")
time.sleep(2)
driver.find_element_by_id("female").click()

2. 自动化测试之页面弹窗的处理，alert（确定和关闭）和confirm（二次确认的弹窗）
   弹窗常用方法 （需要先切换窗口 switch_to_alert）：
   accept（）表示接受,
   dismiss（）表示取消

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("file:///C:/Users/tntjoy3/Desktop/radio.html")   #本地链接
print(driver.title)

time.sleep(3)
driver.find_element_by_id("alert").click()
#切换到弹窗
win = driver.switch_to_alert()
time.sleep(3)
win.accept()

driver.find_element_by_id("confirm").click()
#切换到弹窗
win1 = driver.switch_to_alert()
time.sleep(3)
win1.dismiss()

3.高级知识点自动化测试之验证码常见解决方案：
  3.1 破解验证码：ocr识别（tesseract-ocr）、AI识别
  3.2 绕过验证码：让开发临时关闭验证码（安全性需要保密，一般在开发测试环境使用）；
                 提供一个万能验证码（安全性需要保密，一般在开发测试环境使用）；
                 使用cookie（登录主要是为了拿cookie，获取登录凭证）

4.自动化测试实战进阶之cookie操作

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://xdclass.net/")

print(driver.title)
time.sleep(3)

driver.add_cookie({"name":"name","value":"jack"})
driver.add_cookie({"name":"token","value":""})

video_ele = driver.find_element_by_css_selector("div.....").click()
sleep(2)
buy_btn_ele = driver.find_element_by_css_selector("div.....")
buy_btn_ele.click()
print("进入下单页面")

5.实战系列之自动化测试错误截图
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://xdclass.net/")

time.sleep(3)
# 查找登录按钮
login_ele = driver.find_element_by_css_selector("#login").click()
#触发事件
ActionChains（driver）.click(login_ele).perform()

# 捕捉抓不到元素异常
try:
    driver.find_element_by_id("xdclass").click()
except:
    driver.get_screenshot_as_file("./error.png")
'''