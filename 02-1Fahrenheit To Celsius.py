#-*- coding: utf-8 -*-

fahrenheit = float(input('输入华氏温度: '))    #接收用户输入

celsius = (fahrenheit - 32)/1.8     #计算摄氏温度
print('%0.1f 华氏温度转换为摄氏温度为 %0.1f '%(fahrenheit,celsius))    #打印出结果
