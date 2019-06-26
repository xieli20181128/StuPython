#-*- coding: utf-8 -*-
import math
# PI = 3.14159265
r = float(input("输入圆的半径r的值: "))
cell = 2 * math.pi * r
area = math.pi * pow(float(r),2)
print("圆周长为 %.2f" %cell)
print("圆面积为 %.2f" %area)
