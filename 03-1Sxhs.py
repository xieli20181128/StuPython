#-*- coding: utf-8 -*-

# Name ：求水仙花数
# Description: 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
#              例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

# range() 函数可创建一个整数列表，一般用在 for 循环中。
# 函数语法:range(start, stop[, step])
# 参数说明：
# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

for num in range(100,1000):     # 如果num在[100,1000)范围，就依次循环取出num的值，第一次取100，最后一次取999
    i = num // 100              # //取整符号，对100取整，得到百位上的数字
    j = num // 10 % 10          # %取余符号，得十位上的数字
    k = num % 10                # 得个位上得数字
    if(i**3+j**3+k**3==num):    # 各位数字和等于num
         #print(num)            # 输出符合if条件的数字，换行
         print(num, end = ' ')  # 输出符合条件的数字，end=' '让输出的数不换行，以空格隔开同行输出