#-*- coding: utf-8 -*-

#登录下单测试用例

# import unittest
# import time
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
#
# class LoginOrderTestCase(unittest.TestCase):
#     def setUp(self):
#         print("测试开始")
#         self.driver = webdriver.FireFox()
#         self.driver.implicitly.wait(20)
#         self.base_url = "http://xdclass.net"
#         self.driver.get(self.base_url)
#
#     def tearDown(self):
#         print("单个测试用例结束")
#         pass
#         #单个测试用例结束
#
#     def test_login_order(self):
#         u"登录测试用例"
#         driver = self.driver
#         login_ele = driver.find_element_by_css_selector("#login")  #查找登录框
#         ActionChains（driver）.click(login_ele).perform()
#
#         sleep(2)
#         driver.find_element_by_id("phone").clear     # 清空输入框内容，查找输入框
#         driver.find_element_by_id("phone").send_keys("1382832389")
#
#         driver.find_element_by_id("pwd").clear     #查找密码输入框
#         driver.find_element_by_id("pwd").send_keys("123456")
#
#         login_btn_ele = driver.find_element_by_css_selector("button.login")
#         login_btn_ele.click()
#
#         user_info_ele = driver.find_element_by_css_selector(".user_head_portrait")
#
#         sleep(1)
#         ActionChains（driver）.move_to_element(user_info_ele).perform()
#
#         sleep(1)
#         user_name_ele = driver.find_element_by_css_selector(".img_name")
#         print（"----测试结果----"）
#         print(user_name_ele.text)
#         name = user_name_ele.text
#
#         if name == u"二当家小D"    # 因是中文，所有前面加个u
#             print（"login ok"）
#         else:
#             print("login fail")
#
#         video_ele = driver.find_element_by_css_selector("div.....").click()
#         video_ele.click()
#         sleep(2)
#         buy_btn_ele = driver.find_element_by_css_selector("div.....")
#         buy_btn_ele.click()
#         print("进入下单页面")
#
# if __name__ == '__main__':
#     unittest.main()