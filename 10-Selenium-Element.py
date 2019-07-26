#-*- coding: utf-8 -*-
'''
1.selenium基础实战之定位网页元素技巧
   简介：讲解使用selenium定位网页元素
        find_element_by_id，find_element_by_name，find_element_by_class_name

  1.1 开启浏览器：browser = webdriver.FireFox();

  1.2 打开网页：
      browser.get("http://baidu.com")  #也可以写https
      使用python判断是否正确
      browser.title  或者 browser.current_url

  1.3 定位元素的8种方法
      browser.find_element_by_id()
      browser.find_element_by_class_name()
      browser.find_element_by_css_selector()
      browser.find_element_by_link_text()
      browser.find_element_by_xpath()
      browser.find_element_by_tag_name()
      browser.find_element_by_partial_link_text()
      browser.find_elements_by_name()

  1.4 定位实例
    1.4.1 id定位：
          driver.find_element_by_id("kw").send_keys("小D课堂")
          driver.find_element_by_id("su").click()   #点击事件
    1.4.2 name定位：
          driver.find_element_by_name("wd").send_keys("selenium小D课堂")   选中输入框，输入selenium小D课堂
          driver.find_element_by_id("su").click()  选中按钮，点击事件
    1.4.3 class_name定位：(不能确定唯一性)
          driver.find_element_by_class_name("s_ipt").send_keys("jmeter小D课堂")
          driver.find_element_by_id("su").click()
    1.4.4 tag_name定位：
          browser.find_element_by_tag_name()   通过标签进行定位，不常用 ，因为标签通常不是唯一的
    1.4.5 link_text定位：超链接内容定位，元素内容
          find_element_by_link_text()    通过超链接
          from time import  sleep
          driver.get("https://xdclass.net")
          print(driver.title)
          sleep(3)
          driver.find_element_by_partial_link_text("视频学习").click()
    1.4.6 partial_link_text内容定位：模糊匹配，和上面类似
          driver.find_element_by_partial_link_text("工具").click()
    1.4.7 css定位：根据css属性定位，一般class是用.标记， id是用#标记， 定位方式也会比Xpath快
          driver.find_element_by_css_selector(".//*[@id='app']/div/div[2]/div[2]/div[3]/div/div[1]/div[4]/a/img").click()
          使用firebug拷贝找到css路径
          路径:审查元素—右键复制—CSS选择器
    1.4.8 xpath定位：XPath 使用路径表达式来选取 XML 文档中的节点或者节点集。
                    这些路径表达式和我们在常规的电脑文件系统中看到的表达式非常相似。
          绝对路径：绝对路径起始于正斜杠( /html )
          相对路径：利用元素属性来进行xpath定位
          driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[4]/div[1]/image").click()
          使用firebug拷贝找到css路径

  1.5 定位到元素后的方法：
      clear()  清空
      send_key()  输入
      back（）    后退页面
      maximize_window()  浏览器窗口最大化
      click（）         点击事件
      submit（）         提交表单

  1.6 如果定位元素报错，原因如下：
      1.6.1 根据定位取不到
      1.6.2 多个元素根据下标超出范围，没有0，从1开始
      解决办法：
               换其他方式定位元素
'''