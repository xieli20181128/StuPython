#-*- coding: utf-8 -*-

# Name ：求斐波那契数列
# Description: 形如：1 1 2 3 5 8 13 21 34..... 递推的方法：F(1)=1,F(2)=1,F(n)=F(n-1)+F(n-2)  (n>=3)

a=1
b=1
i=1
while i<=100:            #限制了前100项
    print(a,end=' ')
    m=a
    a=b
    b=m+b
    i=i+1
