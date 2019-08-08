#-*- coding: utf-8 -*-

# 1.什么是单元测试unittest
# 单元测试：指对软件中最小可测试单元进行检查和验证。对于单元测试中单元的含义，一般来说，要根据实际情况去判定其具体含义，如C语言中单元指一个函数，function
# add（inta，intb）{
# }
#
# Java里单元指一个类，图形化的软件中可以指一个窗口或一个菜单等。
# 总的来说，单元就是人为规定的最小的被测功能模块，单元测试是在软件开发过程中要进行的最低级别的测试活动，软件的独立单元将与程序的其他部分相隔离的情况下进行测试。
#
# 1.1.unittest框架是python的单元测试框架（java的单元测试框架是junit）
#
# 1.2.unittest = TestCase + TestResult  执行加结果

# 2.单元测试框架unittest入门
#
# 2.1 unittest的使用
# 2.1.1 用import语句引入unittest模块
# 2.1.2 测试的类都继承于TestCase类
# 2.1.3 setUp（）测试前的初始化工作；tearDown（）测试后的清除工作（在每个测试方法运行时被调用）
#
# 2.2注意点：
# 2.2.1 所有类中方法的入参为self，定义方法的变量也要“self.变量”
# 2.2.2 定义测试用例，以“test”开头命名的方法，方法的入参为self
# 2.2.3 unittest.main（）方法会搜索该模块下所有以test开头的测试用例方法，并自动执行他们
# 2.2.4 自己写的py文件不能用unittest.py命名，不然会找不到TestCase
#       成功是输出，失败是F
#
# 2.3 代码框架示例：
#
# import unittest
#
# class UserTestCase(unittest.TestCase):
#     def setUp(self):
#         print("###setUp###")
#
#     def tearDown(self):
#         print("###tearDown###")
#         self.name =“小D课堂”
#         self.age = 18
#
#     def test_name(self):
#         print("调用test_name")
#         self.assertEqual（self.name, "小D课堂"，msg = "名字不对"）  # 断言是否相同
#
#         def test_isupper(self):
#             print("调用test_isupper")
#             # 断言是否为True，msg是断言判断错误的提示信息
#             self.assertFalse（"xdclass", isupper（）, msg = "不是大写"）
#
#             def test_age(self):
#                 print("调用test_age")
#                 self.assertEqual(self.age, 18)
#
#         if __name__ == '__main__':  # 脚本文件的主要入口
#             unittest.main()
#
# 3.TestSuite的基本介绍和使用场景
#
# 利用unittest执行流程测试而非单元测试
# 控制unittest的执行顺序
#  3.1 unittest.TestSuite()
#         类来表示一个测试用例集
#         用来确定测试用例的顺序，哪个先执行哪个后执行
#         如果一个class中有四个test开头的方法，则加载到suite中时则有四个测试用例
#         由TestLoder加载TestCase到TestSuite
#         verbosity参数可以控制执行结果的输出，0是简单报告、1  是一般报告、2是详细报告  默认1
#         会在每个成功的用例前面有个“.”, 每个失败的用例前面有个“F”
#
# 3.2 TextTestRunner（）文本测试用例运行器
#
# 3.3 run（）方法是运行测试套件的测试用例，入参为suite测试套件
#
# 3.4 代码示例
#         import unittest
#
#         class XdclassTestCase(unittest.TestCase):
#             def setUp(self):
#                 self.name =“小D课堂”
#                 self.age = 18
#                 print("setUp method**")
#
#             def tearDown(self):
#                 print("tearDown method**")
#                 self.assertEqual（'foo', upper(), 'FOO'）
#
#                 def test_one(self):
#                     print("test_one 小D来了")
#                     self.assertEqual（self.name, "小D课堂"，msg = "名字不对"）  # 断言是否相同
#
#                     def test_two(self):
#                         print("test_two 前端来啦")
#                         # 断言是否为True，msg是断言判断错误的提示信息
#                         self.assertFalse（'XD', isupper（）, msg = "不是大写"）
#
#                         def test_three(self):
#                             print("test_three 后端来啦")
#                             self.assertEqual(self.age, 18)
#
#                         def test_four(self):
#                             print("test_four 小D官网上线啦")
#                             self.assertEqual(self.age, 18)
#
#                     if __name__ == '__main__':  # 脚本文件的主要入口
#                         suite = unittest.TestSuite()
#                         suite.addTest(XdclassTestCase("test_one"))
#                         suite.addTest(XdclassTestCase("test_two"))  # 想先执行第2个测试用例，将第2个放在第1个前面即可
#                         suite.addTest(XdclassTestCase("test_three"))
#                         suite.addTest(XdclassTestCase("test_four"))
#
#                         # verbosity 参数可以控制执行结果的输出
#                         runner = unittest.TextTestRunner(verbosity=1)
#                         runner.run(suite)

# 4 高级实战系列之测试套件TestSuite生成测试报告
#  4.1 HTMLTestRunner介绍
#     HTMLTestRunner是Python标准库的 unittest模块的一个扩展，它可以生成HTML的测试报告。无法通过pip安装。
#      首先下载HTMLTestRunner.py，然后将HTMLTestRunner.py复制到python安装目录的Lib文件夹下。
# 注意：
#     python2和python3，语法不一样，导致HTMLTestRunner在python3不兼容
#     解决办法：导入修改好的HTMLTestRunner，搜索HTMLTestRunner python3
#
# 4.2 代码示例
#                     import unittest
#                     import time
#
#                     class XdclassTestCase(unittest.TestCase):
#                         def setUp(self):
#                             self.name = "小D课堂"
#                             self.age = 18
#                             print("setUp method**")
#
#                         def tearDown(self):
#                             print("tearDown method**")
#                             self.assertEqual（'foo', upper(), 'FOO'）
#
#                             def test_one(self):
#                                 print("test_one 小D来了")
#                                 self.assertEqual（self.name, "小D课堂"，msg = "名字不对"）  # 断言是否相同
#
#                                 def test_two(self):
#                                     print("test_two 前端来啦")
#                                     # 断言是否为True，msg是断言判断错误的提示信息
#                                     self.assertFalse（'XD', isupper（）, msg = "不是大写"）
#
#                                     def test_three(self):
#                                         print("test_three 后端来啦")
#                                         self.assertEqual(self.age, 18)
#
#                                     def test_four(self):
#                                         print("test_four 小D官网上线啦")
#                                         self.assertEqual(self.age, 18)
#
#                                 if __name__ == '__main__':  # 脚本文件的主要入口
#                                     suite = unittest.TestSuite()
#                                     suite.addTest(XdclassTestCase("test_one"))
#                                     suite.addTest(XdclassTestCase("test_two"))  # 想先执行第2个测试用例，将第2个放在第1个前面即可
#                                     suite.addTest(XdclassTestCase("test_three"))
#                                     suite.addTest(XdclassTestCase("test_four"))
#
#                                     # 文件名中加了当前时间，为了每次生成不同的测试报告
#                                     file_prefix = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
#                                     print(file_prefix)
#
#                                     # 创建测试报告，此时这个文件还是空文件；wb以二进制格式打开一个文件，只用于写入，如果文件存在则覆盖
#                                     fp = open("./" + file_prefix + "_result.html"，"wb")
#
#                                     # stream定义一个测试报告写入的文件，title就是标题，description就是描述
#                                     runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"小D课堂 测试报告"，description = u"测试用例执行情况")
#                                     runner.run(suite)
#                                     fp.close()
#
# 5.unittest中HTML测试报告优化
#   在每一个测试用例加u“说明内容”
#
#             def test_four(self):
#              u"这是首页登录测试用例"
#                 print("test_four 小D官网上线啦")
#                 self.assertEqual(self.age, 18)
