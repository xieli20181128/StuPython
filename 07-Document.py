#-*- coding: utf-8 -*-
# 读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
#
# 1. 读文件：要以读文件的模式打开一个文件对象，使用python内置的open（）函数，传入文件名和标识符
#
# 1.1 读取整个文件
# open(file,mode='r')
# file:必须，文件路径（相对或绝对路径）
# mode：可选，文件打开模式
#
# 例如：
# f=open('C:/Users/tntjoy03/test.txt','r') 这样就表示成功打开了一个文件
# f.read()    'Hello tnt!'   文件打开成功后，就调用read（）方法可以一次读取文件的全部内容，python把内容读到内存，用一个str对象表示
# f.close()                  最后一步是调用close（）方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
#
# 1.2 逐行读取文件：
# 1.2.1 file.readline(size)：读取整行，只读取一行内容，包括“\n”字符
# 例如：
# >>> f=open('C:/Users/tntjoy03/test.txt','r')
# >>> f.readline(2)
# 'He'
# >>> f.readline(10)
# 'llo tnt!\n'
# >>> f.close()
#
# 1.2.2 file.readlines(sizeint)：读取所有行并返回列表，一次读取文件所有内容，若给定sizeint>0,则是设置一次读多少字节，这是为了减轻读取压力
# 例如：
# >>> f=open('C:/Users/tntjoy03/test.txt','r')
# >>> f.readlines()
# ['Hello tnt!\n', 'zhaojing\n', 'hanmemei\n']
# >>> f.close()
#
# 1.3 文件路径：可以以相对路径或者绝对路径

# 2.写文件:写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
# #
# # 2.1 覆盖写入
# # f=open（'C:/Users/tntjoy03/test.txt','w'）    w为覆盖写入
# # f.write('Hello zhaojing!')
# # f.close()
# #
# # 2.2 追加写入
# # f=open('C:/Users/tntjoy03/test.txt','a')     a为追加
# # f.write('zhui jia xie ru')
# # f.close()
# #
# # 2.3 文本文件
# # f=open（'C:/Users/tntjoy03/test.txt','t'） 默认的是文本模式
# #
# # 2.4 二进制文件
# # 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
# # >>> f=open('C:/Users/tntjoy03/test.txt','rb')
# # >>> f.read()
# # 执行结果：
# # b'hello zhaojing!zhui jia xie ru'

# 3. 异常处理
#
# 3.1 异常机制的重要性：
# 3.1.1 在python中使用try-except语句来处理异常，具体做法是将可能引发异常的语句放到try块中执行，当发生异常时，跳过try块中剩余的语句，直接跳转至except中的语句来处理异常；
# 3.1.2 可以自定义异常处理方式
# 3.1.3 可以避免因异常产生导致程序运行终止
#
# 3.2 try-except代码块
# try的工作原理是，当开始一个try语句后，python就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里，try子句先执行，接下来会发生什么依赖于执行时是否出现异常。
# 如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
# 如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印缺省的出错信息）。
# 如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。
#
# 3.2.1 例子
# try：
#      f=open（'test.txt'）
#      f.read()
#      f.close()
# except :
#      print("没有找到文件")
#
# 执行结果：没有找到文件
#
# 3.2.2 如果不同类型的异常，程序的处理方式不相同，还可以使用多个except语句
# try：
#      f=open('test.txt')
#      f.read()
#      f.close()
# except IOError:
#      print('wrong1')
# except TypeError:
#      print('wrong2')
# except ValueError:
#      print('wrong3')
#
# 执行结果：wrong1
#
# 3.2.3 使用except而不带任何异常类型
# try:
#     正常的操作
# except:
#     发生异常，执行这块代码
# else:
#     如果没有异常执行这块代码
#
# 3.3 else代码块
# try:
#     f = open("test", "w")
#     f.write("这是一个测试文件，用于测试异常!!")
# except IOError:
#     print "Error: 没有找到文件或读取文件失败"
# else:
#     print "内容写入文件成功"
#     f.close()
#
# 3.4 finally代码块
# try-finally 语句无论是否发生异常都将执行最后的代码。
# try:
# <语句>
# finally:
# <语句>    #退出try时总会执行
#
# try:
#     print('请输入一个数字：')
#     user=input()
#     print(int(user)+1)
# except (ValueError,IOError):
#    print("必须输入数字！")
# except：
#    print('wrong')
# else：
#    print('OK')
# finally:
#   print('Finally')
#
# 3.5 内置异常类型
# 3.5.1 BaseException：  所有异常的基类
# 3.5.2 Exception:常规错误的基类
# 3.5.3 SystemExit：解释器请求退出
# 3.5.4 KeyboardInterrupt：用户中断执行(通常是输入^C)
# 3.5.5 StandardError：所有的内建标准异常的基类
# 3.5.6 ArithmeticError：所有数值计算错误的基类
# 3.5.7 ValueError：传入无效的参数
# 3.5.8 Warning：警告的基类
# 3.5.9 SyntaxError：Python 语法错误
# 3.5.10 IndentationError：缩进错误
#
# 3.6 异常栈
# import traceback
#
# def f1():
#     result = 123
#     int('asdf')
#     return result
#
# def run():
#     try:
#         ret = f1()
#         print(ret)
#     except Exception as e:
#         msg = traceback.format_exc()
#         print('错误的堆栈信息')
# run()
#
# 3.7 raise语句
# 在python中进行异常处理时，也可以使用raise语句主动引发异常，主动引发异常时可以指明异常类型。
# try：
#     print("a")
#     print("b")
#     raise Exception
#     print("c")
# except：
#    print('wrong')
# else：
#    print('OK')
# finally:
#   print('Finally')

# 4.数据持久化
# 4.1 csv文件概述（逗号分隔符Comma - SeparatedValues）
# csv是一个被行分隔符、列分隔符划分成行和列的文本文件
# csv不指定字符编码，行分隔符为\r\n，最后一行可以没有换行符
# 列分隔符常为逗号或制表符
# 每一行称为一条记录record：字段可以使用双引号括起来，也可以不适用，如果字段中出现双引号，逗号，换行符必须用双引号括起来，表头可选，和字段列对齐就行了
#
# 4.2 csv模块的应用
# 4.2.1 数据读取
# csv.reader(csvfile, dialect=’excel’, ** fmtparams)
# 它是读取CSV文件时最常用的方法
# 它的csvfile参数需要一个文件类型的对象，比如：
# fileObj = open('E:/inputFile.csv', 'r')
# csvReader = csv.reader(fileObj)
# 那么这个方法返回的csvReader就是一个可以按行读取文件的对象。
#
# 4.2.2 数据写入
# csv.writer(csvfile, dialect=’excel’, ** fmtparams)
# 它是写入CSV文件时最常用的方法 ，示例：
# import csv
# with open('eggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
# spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
# spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
#
# 4.3 json数据格式
# JSON有两种表示结构，一种是对象结构，一种是数组结构。
# 对象结构以{键: 值}的形式表示，类似于字典的形式
# 数组结构以[元素1，元素2，元素3]的形式表示
#
# 4.4 json模块的应用
# 使用JSON函数需要导入json
# 库：import json
# json.dumps: 将Python对象编码成JSON字符串
# json.loads: 将已编码的JSON字符串解码成Python对象
#
# 4.4.1 json.dumps
# 语法：json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None,
#               separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)
# 实例1：将数组编码为JSON格式数据
# import json
# data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
# json = json.dumps(data)
# print(json)
#
# 执行结果：[{"a": 1, "c": 3, "b": 2, "e": 5, "d": 4}]
#
# 实例2：使用参数让JSON数据格式化输出
# import json
# print（json.dumps
# {'a': 'Runoob', 'b': 7}, sort_keys = True, indent = 4, separators = (',', ': ')）
# 执行结果：
# {
#     "a": "Runoob",
#     "b": 7
# }
#
# 4.4.2 json.loads
# 语法：json.loads(s[, encoding[, cls[, object_hook[, parse_float[, parse_int[, parse_constant[, object_pairs_hook[,
#               **kw]]]]]]]])
#
# 实例1：解码json对象
# import json
# jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
# text = json.loads(jsonData)
# print(text)
#
# 执行结果：{u'a': 1, u'c': 3, u'b': 2, u'e': 5, u'd': 4}
#
# 使用第三方库：Demjson
# Demjson是python的第三方模块库，可用于编码和解码JSON数据，包含了JSONLint的格式化及校验功能。
#
# 4.4.3 encode()函数用于将Python对象编码成JSON字符串。
# 语法：demjson.encode(self, obj, nest_level=0)
#
# 实例：
# import demjson
# data = [{'a': 1, 'b': 2, 'c': 3}]
# json = demjson.encode(data)
# print(json)
#
# 执行结果：[{"a": 1, "b": 2, "c": 3}]
#
# 4.4.4 使用demjson.decode()函数解码JSON数据。该函数返回Python字段的数据类型。
# 语法：demjson.decode(self, txt)
#
# 实例：
# import demjson
# json = '{"a":'1, "b": 2, "c": 3}';
# text = demjson.decode(json)
# print(text)
#
# 执行结果：{u'a': 1, u'b': 2, u'c': 3}
