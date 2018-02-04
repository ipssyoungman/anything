# -*- coding: utf-8 -*-
from functools import reduce
def str2float(s):
    def intfn(x,y):
        return x*10+y
    def flofn(x,y):
        return x*10**-1 + y
    for i in range(len(s)):
      num=s.find('.')                     #小数点的位置
        while i<num:
            int_part=reduce(intfn,map(int,s[i]))
        if s[i]!='.':
            reduce(flofn,map(int,s[i]))
            else:
                pass

print('str2float(\'123\') =', str2float('123'))
if abs(str2float('123') - 123) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')



'''
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
'''
