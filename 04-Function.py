#-*- coding: utf-8 -*-

# 1.1 函数的作用？什么是函数？ 封装了一段代码块，可以被重复使用多次，例如数学中的三角函数
# 1.2 代码坏味道：指在代码之中潜在问题的警示信号。并非所有的坏味道所指示的确实是问题，但是对于大多数坏味道，均很有必要加以查看，并作出相应的修改。
# 1.3 封装函数模块：一个.py文件就是一个模块（把一个函数写入py文件中存起来被其他py文件调用）
#       模块管理函数定义：模块管理函数就是将函数的定义放到一个.py文件中，可以在其他.py文件中通过import关键字导入模块。
#          导入后就可以使用模块名+函数名的方式去使用其他模块中的函数.(也就是说把一个函数独立封装到一个py文件中,
#         在另一个py文件中,要想使用这个函数,首先导入模块名,然后再调用模块中的函数名(模块名就是把函数封装到那个py文件的文件名))
#        注意: 模块中的变量不能在模块之外单独使用,模块中的变量只针对模块中的代码使用(比如:你想在py文件1中调用py文件2中的变量,那是不得行的.)
#
#       使用模块：
#           方法（1）：模块名+函数名
#                      import module   #module就是封装函数的那个文件名
#                      aa = module.sum(1,2)   #模块名.函数名
#                      print(aa)
#
#           方法（2）：from 模块名 import 函数名
#                      from module import  count_letter_number  #导入以下函数，import 功能相当于把被导入的模块中的代码拷贝到import的位置
#
#           方法（3）：如果函数名相同，又不想改变函数名，可通过as关键字更改模块名和函数名，目的是防止命名相同，产生冲突。
#                      from module import count_letter_number as sum #这里的sum是将封装好的函数名count_letter_number在调用时零时改为sumn
#                       注意: 函数若同名:后面的函数会覆盖前面的函数.模块下的函数名与被导入模块中的函数名相同时,则会执行模块下的函数,不会执行模块中的函数.
#
#       不导入执行语句，只导入函数：
#            if__name__=='__main__':   #把它看成一把闭加锁，使用它就相当于一把锁，把执行语句放在它下面可以阻止其他模块去执行这些内容。
#                                       #要想不被模块调用函数中的执行语句，就把函数名放在它下面，保护起来
#                    def count_letter_number(string):
#                       letter_count=0
#                       digit_count=0
#                       for ch in string:
#                           if 'a'<=ch<='z' or 'A'<=ch <='Z':
#                               letter_count+=1
#                           elif '0'<=ch <='9':
#                               digit_count+=1
#                       return letter_count,digit_count
#          #比如我们只想导入以上这部分函数，不需要导入以下的main()函数，那就把main（）函数执行的返回值放在if里面，
# #         #main（）函数只能在文本文件名中执行，不会被其他模块调用
#
#                    def main():
#                        print(count_letter_number('a1b2c3d4'))
#                        print(count_letter_number('a123456b'))
#                        print(count_letter_number('123456!!'))
#
#                     if __name__ == '__main__':
#                         main()

# 2.1 函数的语法：def 函数名(参数列表):
# 2.2 return语句
# return作用：
# 1.返回函数执行的结果
# def test1(a,b):
#     print('......')
#     return a+b
# rs = test1(100,200)
# print(rs)

# 2.结束函数的执行
# def test2(a):
#     print('------')
#     if a == 10:
#         return    #return 下方的代码就不会执行了
#     print('**********')
# test2(10)

# 3.在函数中，返回多个值，返回的多个值，放在一个元组里
# def test3( ):
#     return 1,2,3,4,5,6,7,8,9
# rs = test3( )
# print(rs)
# 2.3 调用自定义函数
#   把基础模块放在固定文件夹（或相对固定文件夹），使用sys.append(r’自定义的模块路径’)
#   例：1.在E:\PyCharm Community Edition 2019.1.3新建test.py实现基础功能函数（定义一个hello（）函数）
#         def hello( ):
#              print("hello function!")
#       2.调用自定义的函数
#          import sys
#          sys.path.append(r"E:\PyCharm Community Edition 2019.1.3")
#          import hello
#          hello.hello( )
#       3.运行结果：hello function！

# 2.4 调用内置函数
#     要调用内置函数，要知道函数的名字，该函数实现的功能，参数等。比如abs（）求绝对值，并且参数只有一个，abs（5），abs（-5）

# 3.1 函数的参数
#     3.1.1 必选参数：必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。，比如abs（a） 调用的时候abs（2，5）那就会出现错误
#     3.1.2 命名关键字参数：允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装成一个dict；使用**表示关键字参数
#     3.1.3 默认参数：调用函数时，默认参数的值如果没有传入，则被认为是默认值。
#     3.1.4 可变参数：传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个；在参数前面加上*就是可变参数。
#            在函数内部，参数numbers接收得到的是一个tuple，调用该函数时，可以传入任意个参数，包括0个参数
#     请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
#            def func(a,b,c=0,*args,**kw)
#
#     总结：默认参数一定要用不可变对象，如果是可变对象，运行会有逻辑错误！
#           *args是可变参数，args接收的是一个tuple;
#           **kw是关键字参数，kw接收的是一个dict

# 3.2 函数的返回值：程序中函数完成一件事情后，最后给调用者的结果，需要用到return语句
#     3.2.1 没有返回值：默认返回给none，有三个情况：不写返回值，只print（经济法）；只写一个return；return None（几乎不用）；
#     3.2.2 返回单个值：返回一个值，def func（）：a=123   return a
#     3.2.3 返回多个值：多个值之间用逗号区分，def func1（）：a=123 b='abc'  return a,b
#
# 3.3 作用域问题
#     3.3.1 局部作用域：在函数内部声明的变量不能在函数外部访问，函数内部声明的变量为局部变量，其作用域仅限于函数内部。
#           使用global关键字可以提升函数内部的局部变量为全局变量，当使用global关键字修饰变量时，该变量被提升为全局变量。
#     3.3.2 嵌套作用域：嵌套函数中外层函数体中声明的变量。函数体内嵌套的函数是不能被外部调用的，其作用域仅限于函数体内部。
#     3.3.3 全局作用域：全局变量是指在模块范围内的全局变量，其作用域是整个模块。全局变量可以在模块内的函数内部使用，但需要遵循先声明后使用的原则。
#     3.3.4 内置作用域：python提供的变量(函数)
# 注意：当模块内全局变量的名称和函数体内局部变量的名称相同时，在函数体内声明的局部变量将覆盖与其名称相同的全局变量。

# 3.4 模块管理函数
#     3.4.1 模块的概念：模块就是文件，存放一堆函数，谁用谁拿，就是一系列常用功能的集合体，一个py文件就是一个模块
#          理解过程：一个函数封装成一个功能，现在有一个软件，不可能将所有程序都写入一个文件，所以咱们应该分文件，组织结构要好，代码不冗余，
#                   所以要分文件，分了5个文件，每个文件里都有相同的功能函数，所以将这些相同的功能封装到一个文件中。
#          导入模块：import sys
#                    from。。。import。。。
#          为模块起别名：import module.py as t
#     3.4.2 自定义模块管理函数
#           自定义的源文件，文件名saytest.py,里面有个函数sayFu；如何调用这个函数呢？直接写sayFu（）肯定不行，saytest.sayFu()？
#           也不行，这时候就要想起import sayFu,，还是不行？
#           那如何才能正确引入呢？
#           1.找到Python安装目录下的site-packages文件夹（$Python\Lib\site-packages）。在该目录下创建一个PATH文件（*.pth），例如 MyPath.pth
#           2.打开新创建的文件，将你Python源文件所在的目录写入文件中。
#             比如我的saytest.py文件的目录是E:\PythonSpace，PATH文件名为MyPath.pth。所以我的MyPath.pth的文件内容为：E:\PythonSpace
#           OK，将你的Python容器（IDLE或则command line）重启。因为需要重新载入PATH。
#     3.4.3 命名冲突的时候会怎么样（同一个模块和不同的模块）
#           如果两个包中定义的函数，类，或者子模块互相重名，那么就可能会导致名称冲突，
#           例如:  from analysis.utils import inspect
#                  from frontend.utils import inspect    # 覆盖前一句导入的inspect
#           解决方法1：在import语句中，通过as语句，给引入当前作用域中的属性重新起名
#                     from analysis.utils import inspect as analysis_inspect
#                     from frontend.utils import inspect as frontend_inspect
#           凡是通过import语句引入的内容，都可以通过as子句来改名，及时引入整个模块，也依然能用as为其改名。
#
#           解决方法2：每次使用模块时都从最高层的路径来时，完整地写出各模块的名称。
#                      import analysis.utils
#                      import frontend.utils
#           然后通过analysis.utils.inspect和frontend.utils.inspect这样完整的路径来访问这两个模块中的函数。