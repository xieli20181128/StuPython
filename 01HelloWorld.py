# -*- coding: utf-8 -*-

print("Hello World!")
print("Hello Python!")


# Python 简介：
# Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。
# Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色语法结构。
# Python 是一种解释型语言： 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。
# Python 是交互式语言： 这意味着，您可以在一个 Python 提示符 >>> 后直接执行代码。
# Python 是面向对象语言: 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。
# Python 是初学者的语言：Python 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到 WWW 浏览器再到游戏。

# Python 发展历史：
# Python 是由 Guido van Rossum 在八十年代末和九十年代初，在荷兰国家数学和计算机科学研究所设计出来的。
# Python 本身也是由诸多其他语言发展而来的,这包括 ABC、Modula-3、C、C++、Algol-68、SmallTalk、Unix shell 和其他的脚本语言等等。
# 像 Perl 语言一样，Python 源代码同样遵循 GPL(GNU General Public License)协议。
# 现在 Python 是由一个核心开发团队在维护，Guido van Rossum 仍然占据着至关重要的作用，指导其进展。

# python的环境搭建：
# 下载python和pycharm，找到python的安装路径，打开电脑高级的设置进行环境变量的设置，点击path，添加环境变量；

# python的优缺点：
# 优点:
# 1.语言简洁优美
# 例如去除了大括号，写法简单，写法更接近于英语，其他语言几十上百行的代码，十来行就能解决，而且还好看
# 2.跨平台，window、linux、mac通用
# 3.排行高，社区完善
# 4.胶水语言
# python常常被昵称为胶水语言，能够把其他语言制作的各种模块（尤其是C / C + +）很轻松地结合在一起，
# 例如在人工智能领域，因为是计算密集型，核心算法完全依赖C / C + +，他们速度快适合底层写算法，python慢但简单适合上层写逻辑，
# 而且python是这些库的API
# binding，要开发一个其他语言到C / C + +的跨语言接口，python最容易，就这样，最油腻的人和最强最快的马结合在了一起，欢快的跑了起来。
# 可以这么理解，python本身不是一种运算快的语言，但善于利用，整合其他语言且能在各个平台使用得溜，最重要的是开发效率还很高
#
# 缺点:
# 1.运行速度慢
# python是解释型语言，运行时需要一行行转换成CPU能理解的机器码，很费时
# 2.代码不能加密

# 目前Python主要应用领域：
# 云计算: 云计算最火的语言， 典型应用OpenStack
# WEB开发: 众多优秀的WEB框架，众多大型网站均为Python开发，Youtube, Dropbox, 豆瓣。。。， 典型WEB框架有Django
# 科学运算、人工智能: 典型库NumPy, SciPy, Matplotlib, Enthought librarys,pandas
# 系统运维: 运维人员必备语言
# 金融：量化交易，金融分析，在金融工程领域，Python不但在用，且用的最多，而且重要性逐年提高。原因：作为动态语言的Python，语言结构清晰简单，库丰富，成熟稳定，科学计算和统计分析都很牛逼，生产效率远远高于c,c++,java,尤其擅长策略回测
# 图形GUI: PyQT, WxPython,TkInter

# pycharm下载安装：
# 官网下载后安装，比较小白的点击下一步下一步；
# 一些快捷键：
# 1、Ctrl + Enter：在下方新建行但不移动光标；
# 2、Shift + Enter：在下方新建行并移到新行行首；
# 3、Ctrl + /：注释(取消注释)选择的行；
# 4、Ctrl + Alt + L：格式化代码(与QQ锁定热键冲突，关闭QQ的热键)；
# 5、Ctrl + Shift + +：展开所有的代码块；
# 6、Ctrl + Shift + -：收缩所有的代码块；
# 7、Ctrl + Alt + I：自动缩进行；
# 8、Alt + Enter：优化代码，提示信息实现自动导包；
# 9、Ctrl + Shift + F：高级查找；
# 10、Alt + Shift + Q：更新代码到远程服务器
# 注释：
# #单行注释
# ...多行注释...