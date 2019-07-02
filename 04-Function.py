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



# 函数的语法：def 函数名(参数列表):
# return语句
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