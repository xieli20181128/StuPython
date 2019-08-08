#-*- coding: utf-8 -*-

#菜单分类测试用例

# import unittest
# import time
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
#
# class CategoryTestCase(unittest.TestCase):
#     def setUp(self):
#         print("测试开始")
#         self.driver = webdriver.FireFox()
#         self.driver.implicitly.wait(20)
#         self.base_url = "http://xdclass.net"
#         self.driver.get(self.base_url)
#
#     def tearDown(self):
#         print("测试结束")
#         self.driver.quit()
#         #单个测试用例结束
#
#     def test_menu(self):
#         u"弹出菜单测试用例"
#         driver = self.driver  #跳转网页
#         sleep(1)
#
#         memu_ele = driver.find_element_by_css_selector("#banner_left_url > a:nth_child()")
#         ActionChains(driver).move_to_element(memu_ele).perform()
#         sleep(2)
#
#         sub_menu_ele = driver.find_element_by_css_selector("#des > li:nth-child(1) >")
#         sub_menu_ele.click()
#         sleep(2)
#
# if __name__ == '__main__':
#     unittest.main()