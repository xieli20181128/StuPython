#-*- coding: utf-8 -*-

# 1. 字符串的使用
#
#    1.1 计算长度:通过len()函数返回字符串的长度；如：text='python'  len(text)   计算结果为6
#
#    1.2 下标运算：下标从0开始，到num-1结尾，
#        如：var1 = 'Hello!'   则var1[0]得到 H  ；
#            var2 = "Python Runoob"     则var2[1:5]得到 ytho
#
#    1.3 切片：切片操作（slice）可以从一个字符串中获取子字符串（字符串的一部分）。
#        1.3.1 格式： [start:end:step]
#        1.3.2 [:] 提取从开头（默认位置0）到结尾（默认位置-1）的整个字符串
#              [start:] 从start 提取到结尾
#              [:end] 从开头提取到end - 1
#              [start:end] 从start 提取到end - 1
#              [start:end:step] 从start 提取到end - 1，每step 个字符提取一个
#        1.3.3 几个例子  letter = 'abcdefghijklmnopqrstuvwxyz'
#             1.3.3.1 提取最后N个字符：letter[-3:]    'xyz'
#             1.3.3.2 从开头到结尾，step为5：letter[::5]   'afkpuz'
#             1.3.3.3 将字符串倒转（reverse），通过设置步长为负数：letter[::-1]    'zyxwvutsrqponmlkjihgfedcba'
#
#    1.4 常用方法
#        1.4.1 split（）通过指定分隔符对字符串进行切片，如果num有指定值（默认为-1 即分隔所有），则分隔num+1个子字符串
#             如：str_a="jackson"   result=str_a.split('a')   则result为['j','ckson']  #a被当成分隔符使用了，所以不会输出
#        1.4.2 join（）用于将序列中的元素以指定的字符连接生成一个新的字符串
#             如：str="-"; seq=("a","b","c"); #字符串序列   print str.join(seq);  输出结果：a-b-c

# 2. 列表基本用法
#
#    2.1 定义列表：处理一组有序项目的数据结构，即可以在一个列表中存储一个序列的项目，如购物清单、手机通讯录等；
#
#    2.2 列表的表示：
#      2.2.1 在python中定义列表需要使用方括号，列表中的项目都包含在方括号中，项目之间使用逗号分隔，l1=[1,2,3,4,5]
#      2.2.2 列表中的数据可以是任意数据类型，甚至可以是不同类型的混合，如l2=[1,'a',2,'b']
#
#    2.3 用下标访问元素
#        list1 = ['physics', 'chemistry', 1997, 2019]     则list1[0]:  physics
#        list2 = [1, 2, 3, 4, 5, 6, 7 ]                  则list2[1:5]:  [2, 3, 4, 5]
#
#    2.4 下标越界
#        list1 = ['physics', 'chemistry', 1997, 2019]   则list1[4]则下标越界了
#
#    2.5 添加元素
#        2.5.1 append（）在列表末尾添加元素
#              list3 = []   #空列表
#              list3.append('qian')   #使用append（）添加元素
#              list3.append('xi')
#              print(list3)
#              输出结果：['qian','xi']
#        2.5.2 insert（）在列表中插入元素
#              moto=['h','y','s']
#              moto.insert(0,'d')
#              print(moto)
#              输出结果：['d','h','y','s']
#
#    2.6 删除元素
#        2.6.1  del 删除元素
#              list1 = ['physics', 'chemistry', 1997, 2019]
#              del list1[2]
#              print(list1)
#              输出结果为：['physics', 'chemistry', 2019]
#        2.6.2 pop（）删除末尾的元素，也可以根据索引删除，如moto.pop(0)
#              moto=['h','y','s']
#              moto.pop()
#              print(moto)
#              输出结果：['h','y']
#
#    2.7 修改元素
#        moto=['h','y','s']
#        print(moto)            #输出结果：['h','y','s']
#        moto[0]='d'
#        print(moto)            #输出结果['d','y','s']
#
#    2.8 切片
#        2.8.1 格式[start:end:step]
#              start:起始索引，从0开始，-1表示结束
#              end：结束索引
#              step：步长，end-start，步长为正时，从左向右取值。步长为负时，反向取值
#        2.8.2  s=[1,2,3,4,5,6]
#             2.8.2.1 print(s[:])   #代表截取全部内容,输出[1, 2, 3, 4, 5, 6]
#             2.8.2.2 print(s[:3])  #从起始位置到索引位置2处的字符串，输出[1,2,3]
#             2.8.2.3 print(s[3:])  #从第三个索引位置到结尾的字符串，输出[4,5,6]
#             2.8.2.4 print(s[::-1])  #字符串逆序输出，为[6,5,4,3,2,1]
#             2.8.2.5 print(s[::2])   #从开始位置间隔一个字符组成的字符串，输出[1,3,5]
#                     print(range(10)[::2])    #输出偶数：[0,2,4,6,8]
#    2.9 循环遍历
#        2.9.1 for循环遍历
#              l = [1,2,3,4,5,6,7]
#              for i in range(len(l)):
#                  print(i,l[i])
#
#        2.9.2 while循环遍历
#              l = [1,2,3,4,5,6,7,8]
#              index = 0
#              while index < len(l):
#              print(index,l[index])
#              index++
#
#        2.9.3 index结合for循环遍历
#              l = [1,2,3,4,5,6,7]
#              index = 0
#              for i in l:
#              print(index, i)
#              index +=1
#
#        2.9.4 拉链（zip）方法遍历
#              l = [1,2,,4,5,6,6]
#              for i ,v in zip(range(len(l)), l):
#              print(i, v)
#              #zip把它的2个参数组合成了list长度的元组列表，其实每个元组的值是2个列表中的每一个，所以它叫做拉链方法
#
#        2.9.5 enumerate遍历方法
#              l = [1,2,3,4,4,4,4]
#              for i, v in enumerate(l):
#              print(i, v)
#
#    2.10 列表常用操作
#         连接：                       [1, 2, 3] + [4, 5, 6]      结果[1, 2, 3, 4, 5, 6]
#         复制（复制元素和复制数组）： ['Hi!'] * 4                结果['Hi!', 'Hi!', 'Hi!', 'Hi!']
#         长度：                       len([1, 2, 3])             结果3
#         排序： list.sort(cmp=None, key=None, reverse=False)
#                v=['e','a','u','o','i']    v.sort(reverse=True)  结果降序输出['u','o','i','e','a']
#                默认reverse=False 就是升序
#         倒转： list.reverse()
#         查找： in、not in、count（）计算在列表中出现的次数、index指定值在列表中的位置、list_a.find('a')找到返回第一个匹配的位置，若未找到返回-1
#
#    2.11 生成列表
#
#         2.11.1使用range创建数字列表
#               number = list(range(1,6))
#               print(number)
#               输出结果：[1, 2, 3, 4, 5]
#
#         2.11.2生成器
#               定义：生成器表达式，我个人认为还不如叫列表生成器，就是把列表表达式改变了一下，变成了一个生成器。
#               而且这种改变非常简单，就是把外[]换成了（）就创建了一个generator。

# 3. 元组的使用
#
#    3.1 定义元组：元组与列表类似，不同之处在于元组的元素不能修改。
#    3.2 元组的表示：定义元组使用圆括号（小括号），元组中的元素同样也使用逗号分隔，如t1=（1，2，3，4，5）；t2=（1，'a',2,'b'）
#    3.3 使用元组中的值
#         tup1 = ('physics', 'chemistry', 1997, 2000)       tup1[0]:  physics
#         tup2 = (1, 2, 3, 4, 5, 6, 7 )                     tup2[1:5]:  (2, 3, 4, 5)
#    3.4 修改元组变量：元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
#              tup1 = (12, 34.56)      tup2 = ('abc', 'xyz')     修改元组tup1[0]=100 这个操作是非法的。
#              tup3=tup1 + tup2    print tup3    结果是：(12, 34.56, 'abc', 'xyz')
#    3.5 元组和列表转换
#        3.5.1 将字符串转换成列表，需要使用字符串进行分割，使用字符串方法split（），split（）方法会把字符串按照其中的空白字符进行分隔，最终返回一个列表
#              str_a=zhang san    list_a=str_a.split( )   print(list_a)    结果：['zhang','san']
#        3.5.2 将列表转换成字符串：使用join（）
#              str_a=['zhang','san']  str_a=" ".join(list_a)  print(str_a)   结果：zhang  san
#
# 注意： 元组中只包含一个元素时，需要在元素后面添加逗号来消除歧义  tup1=（50，） 这样才会被识别成元组；如果不加逗号，只会输出50就不对了

# 4.集合基本用法
#   4.1 集合和列表的区别
#       集合（set）是一个无序的不重复元素序列
#       列表处理一组有序项目的数据结构，即可以在一个列表中存储一个序列的项目
#   4.2 创建集合
#       可以使用大括号 set{ } 或者 set() 函数创建集合；创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
#   4.3 添加元素
#       4.3.1  s.add( x )，将元素x添加到集合s中，如果元素已存在，则不进行任何操作。例如：
#              thisset = set(("Google", "Runoob", "Taobao"))
#              thisset.add("Facebook")
#              print(thisset)
#              结果：{'Taobao', 'Facebook', 'Google', 'Runoob'}
#       4.3.2 s.update( x ) 也可以添加元素，且参数可以是列表，元组，字典等，x可以有多个，用逗号分开。
#             thisset = set(("Google", "Runoob", "Taobao"))
#             thisset.update({1,3})
#             print(thisset)
#             结果：{1, 3, 'Google', 'Taobao', 'Runoob'}
#   4.4 删除元素
#       4.4.1 s.remove( x )        将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
#            thisset = set(("Google", "Runoob", "Taobao"))
#            thisset.remove("Taobao")
#            print(thisset)
#            结果：{'Google', 'Runoob'}
#       4.4.2 s.discard( x )   也是移除集合中的元素，且如果元素不存在，不会发生错误
#            thisset = set(("Google", "Runoob", "Taobao"))
#            thisset.discard("Facebook")            不会出错的
#            print(thisset)
#            结果：{'Taobao', 'Google', 'Runoob'}
#       4.4.3 s.pop( )      可以设置随机删除集合中的一个元素
#            thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
#            x = thisset.pop()
#            print(x)
#            结果：Runoob          多次执行测试结果都不一样。在交互模式，pop 是删除集合的第一个元素（排序后的集合的第一个元素）
#   4.5 清空
#       s.clear()  清空集合 s
#       thisset = set(("Google", "Runoob", "Taobao"))
#       thisset.clear()
#       print(thisset)
#       结果：set( )
#
#   4.6 集合常用操作
#      返回集合的交集：intersection()
#      返回两个集合的并集：union()
#      返回多个集合的差集：difference()
#      对称差：symmetric_difference( )
#      判断指定集合是否为该方法参数集合的子集：issubset()
#      超集：issuperset( )

# 5.字典的基本用法
#   5.1 字典的特点：字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
#   5.2 创建字典
#       d = {key1 : value1, key2 : value2 }    键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组
#       一个实例：testDict={'time':'时间'，'machine':'机器','time machine':'时间机器'}
#
#       访问字典里的值：dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#                       print ("dict['Name']: ", dict['Name'])                输出结果：dict['Name']:  Runoob
#                       print ("dict['Age']: ", dict['Age'])                  输出结果：dict['Age']:  7
#       注意：如果用字典里没有的键访问数据，会输出错误
#
#   5.3 添加元素：向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
#       dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#       dict['Age'] = 8                      更新 Age                 dict['Age']:  8
#       dict['School'] = "菜鸟教程"          添加信息                 dict['School']:  菜鸟教程
#
#   5.4 删除元素：显示删除一个字典用del命令
#       dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#       del dict['Name']         删除键 'Name'
#       del dict                 删除字典
#
#   5.5 取值
#       dict.get(key, default=None)
#
#   5.6 清空
#       dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#       dict.clear( )
#
#   5.7 字典常用操作
#      5.7.1 keys（）方法：以列表返回一个字典所有的键
#      5.7.2 values（）方法：以列表返回字典中的所有值
#      5.7.3 items（）方法：以列表返回可遍历的(键, 值) 元组数组
#      5.7.4 setdefault（）方法：get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值