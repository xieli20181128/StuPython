#-*- coding: utf-8 -*-

#主入口

# import unittest
# import HTMLTestRunner
# import login_order,category
# import time
#
# #创建测试集合
# def create_suite():
#     print("测试开始")
#     suite = unittest.TestSuite()
#     suite.addTest(unittest.makeSuite(login_order.LoginOrderTestCase))
#     suite.addTest(unittest.makeSuite(category.CategoryTestCase))
#     return suite
#
# if __name__ == '__main__':
#     suite = create_suite()
#
#     #文件名中加了当前时间，为了每次生成不同的测试报告
#     file_prefix = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
#
#     #创建测试报告，此时这个文件还是空文件 wb以二进制格式打开一个文件，只用于写入，如果文件存在则覆盖
#     fp = open("./"+file_prefix+"_result.html","wb")
#
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"小D课堂 测试报告"，description = u"测试用例执行情况")
#     runner.run(suite)
#     fp.close()
#

