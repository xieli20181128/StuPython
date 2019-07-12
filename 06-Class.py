#-*- coding: utf-8 -*-

# 1.类和对象
# 1.1 什么是类：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。
# 1.2 什么是对象：对象是类的实例。
# 1.3 面向对象其他相关概念
#     方法：类中定义的函数
#     类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
#     方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
#     局部变量：定义在方法中的变量，只作用于当前实例的类。
#     实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
#     实例化：创建一个类的实例，类的具体对象。
#
#    例子：
#    笔”作为一个抽象的概念，可以被看成是一个类。
#    一支实实在在的笔则是“笔”这种类型的对象。
#    笔可以写字，因此“写字”就是笔这个类的一种方法。
#    每支笔有自己的颜色，“颜色”就是笔的变量。
#    某种类型的笔有“产量”，但是这个“产量并不属于某一支笔，因此“产量”是类变量，而不是实例变量。

# 2.定义类
# 2.1 基本结构：class语句后跟类名，缩进语句块表示类体，在python定义类时，习惯将首字母大写，用于区分类名和函数名，变量命。
# 2.2 属性和方法
#     构造器：__init__ 构造函数，在生成对象时调用。由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
#             通过定义一个特殊的__init__方法，在创建实例的时候，就把 name score 等属性上去。默认的属性可以写在__init__ 下面。
# 例1：
# class ren(object):
#     def __init__(self,name,sex):                #def __init__ 类的默认属性。当实例化类的时候，就会调用默认属性
#    self.name = name
#    self.sex = sex
#    def funC(self):
#    print ('hello[0]'.format(self.name))
# test = ren('lzc','R')          #实例化类.__init__ 是一个构造器（初始化），当你实例化这个类的时候，必须输入name和sex 变量。
# test.funC()
#
# 例2：
# class Cltdy：         #定义类，并起一个名字
#     n = 1000          #类属性，类内的变量
#     def __init__(self,name,age,profession='IT民工'):     #构造函数，类接收外部传入参数全靠构造函数
#         self.name = name
#         self.age = age
#         self.profession = profession
#     def printing_name(self):      #类的方法
#         print('我的名字是: %s'%self.name)
#     def printing_name(self):
#         print("我的年龄：%s"%self.age)
#     def printing_pfsn(self):
#         print("我的职业：%s"%self.profession)
#
# test = Cltdy('sober',25,'DevOps')            #类的实例化，将参数传入类中，传入参数可以多但不可以少于类构造函数的参数（self参数除外，self是将实例化的变量名传入类）
# print("这是类实例化后的内存地址：%s"%test)
# test.printing_name( )                        #调用实例化后类中的方法
# test.name = 'moon'                           #可以修改构造函数中参数的值
# test.printing_name()
# test.printing_pfsn()
# print(test.n)
# test.n = 2000                  #修改类属性，只针对test实例化生效
# print(test.n,'\n====================')
#
# t2 = Cltdy('jack',22,'student')             #实例化类对象，命名t2
# print(t2.n)
# t2.printing_age()
#
# 2.3 析构器：
#     2.3.1 __init__与__new__这两个魔法方法组成了Python类对象的构造器，
#     2.3.2 在Python类实例化时，其实最先调用的不是__init__而是__new__。
#     2.3.3 __new__是负责实例化对象的，而__init__是初始化操作。
#     2.3.4 __del__是析构器，当Python对象的所有引用都不存在了（被del了），就会自动触发__del__执行。
#
# 2.4 __str__方法：
#     2.4.1 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
#     2.4.2 __str__方法需要返回一个字符串，当做这个对象的描写
#     2.4.3 让print的结果看起来更好一些
#
# 总结：在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法

# 3.使用对象（对象=属性+方法）
#   3.1 创建对象
#      第一步是描述对象，python中对象的描述或蓝图称为一个类。
#      第二步是使用类建立一个对象，这个对象称为这个类的一个实例。例子如下：
# class Ball:
#     def bounce(self):
#         if self.direction == "down":
#             self.direction == "up"
# myball = Ball()
# myball.direction = "down"
# myball.color = "red"
# myball.size = "small"
#
#   3.2 给对象发消息？？？

# 4.面向对象的四大支柱
#   4.1 抽象：把一类事物的共有特性提取出来
#   4.2 封装：封装就是把类中的属性和方法定义为私有的，方法就是在属性名或方法名前加双下划线，而一旦这样定义了属性或方法名后，python会自动将其转换为_类名__属性名（方法名）的格式，
#       在类的内部调用还是用双下划线加属性名或方法名，在类的外部调用就要用_类名__属性名（方法名）。
#       父类的私有属性和方法，子类无法对其进行修改。
#   4.3 继承：
#       4.3.1什么是继承：继承的类直接拥有被继承类的属性而不需要在自己的类体中重新再写一遍，其中被继承的类叫做父类、基类，继承的类叫做派生类、子类。
#                         在python3中如果不指定继承哪个类，默认就会继承Object类，而继承了Object类的类就叫做新式类
#       4.3.2 继承的语法：class 类名(父类名):
#       4.3.3 调用父类方法
# class Animal:
#     def eat(self):
#         print("-----吃----")
#     def drink(self):
#         print("-----喝----")
#     def sleep(self):
#         print("-----睡觉----")
#     def run(self):
#         print("-----跑----")
#
# class Dog(Animal):
#     def bark(self):
#         print("----汪汪叫---")
#
# class Xiaotq(Dog):
#     def fly(self):
#         print("----飞----")
#
#     def bark(self):              # 重写父类方法
#         print("----狂叫----")    # 第1种调用被重写的父类的方法
#                                  # Dog.bark(self)#调用父类方法格式：类名.方法名(self)
#         super().bark()           # 第2种
#
#     xiaotq = Xiaotq()
#     xiaotq.fly()
#     xiaotq.bark()
#     xiaotq.eat()
#
#     4.3.4 方法重写
#           子类和父类中拥有方法名相同的方法，说明子类重写了父类的方法
#           重写的作用：父类中已经有了这个方法，但子类想修改里面的内容，直接修改父类是不好的，就需要用到重写
#     4.3.5 类型判定
#           函数isinstance()可以判断一个变量的类型，既可以用在Python内置的数据类型如str、list、dict，也可以用在我们自定义的类，它们本质上都是数据类型
#           s = Student('Bob', 'Male', 88)
#           isinstance(s, Person)         True，s是Person类型
#           isinstance(s, Student)        True，s是Student类型
#           isinstance(s, Teacher)        False，s不是Teacher类型
#     4.3.6 多重继承：即子类有多个父类，并且具有它们的特征
#
#   4.4 多态：多态就是不同的对象可以调用相同的方法然后得到不同的结果

# 5.属性
#   5.1 类属性：直接在类中创建的属性，类属性有且只有一个；
#   5.2 实例属性：每个实例各自拥有，相互独立；绑定在一个实例上的属性不会影响到其他的实例，如果在类上绑定一个属性，那么所有的实例都可以访问类属性，
#           且访问的类属性是同一个，一旦类属性改变就会影响到所有的实例。
#   5.3 属性访问器
#       @property  读
#       @***.setter  写
#   5.4 属性删除器
#       @***.deleter 删除
#   5.5 使用__slots__：
#       定义一个特殊的__slots__变量，来限制该class能添加的属性：
#        class Student(object):
#              __slots__ = ('name', 'age')   # 用tuple定义允许绑定的属性名称
#
#        s = Student()         # 创建新的实例
#        s.name = 'Michael'    # 绑定属性'name'
#        s.age = 25            # 绑定属性'age'
#        s.score = 99          # 绑定属性'score'
#
#       Traceback (most recent call last):
#          File "<stdin>", line 1, in <module>
#       AttributeError: 'Student' object has no attribute 'score'
#
#       由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
#       使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的

# 6.类中的方法
#   6.1 实例方法：第一个参数强制为类实例对象，可以通过这个类实例对象访问类属性，可以通过类实例对象的__class__属性访问类属性。
#      def inst_method(self):
#          print('实例（%s）：%s' % (self.__class__.count, self.inst_name))
#   6.1.1 类实例方法不需要标注，第一个参数必不可少，解析器自动会将类实例对象传给方法的第一个参数。
#         类的初始化方法__init__也是实例方法，在实例创建的时候自动调用。
#         在这里每当初始化一个实例，就通过__class__来访问类属性count，是它加一，用来统计类的实例数。
#         def __init__(self, inst_name):
#            self.inst_name = inst_name
#            self.__class__.count += 1
#
#   6.2 类方法：第一个参数强制为类对象，可以通过这个类对象访问类属性，由于没有传入类实例对象，所以不能访问类实例属性。
#       @classmethod             #类方法需要使用classmethod标注，
#       def class_method(cls):
#           print cls.count       #第一个参数必不可少，解析器自动会将类对象传给方法的第一个参数。
#
#   6.3 静态方法：无法访问类属性、类实例属性、没有默认的第一个参数，其实跟类没什么关系，只是绑定在类命名空间下的函数而已。
#       @staticmethod           #类方法需要使用staticmethod标注
#       def static_method():
#           print 'hello'       #没有默认的第一个参数
#
# 注意：通过类对象可以调用类方法、类静态方法，但不可以调用类实例方法；通过类实例对象可以调用以上三种方法

