#-*- coding: utf-8 -*-

from selenium import webdriver    #从Selenium包导入WebDriver才能使用Selenium WebDriver的方法；

driver=webdriver.Firefox()    #选用一个浏览器驱动实例，会提供一个接口去调用Selenium命令来跟浏览器交互；
driver.maximize_window()      #窗口最大化显示
driver.get("http://www.baidu.com/")
#调用driver.get()方法访问该应用程序，方法调用后，WebDriver会等待，一直到页面加载完成才继续执行脚本；

driver.quit()