# -*- coding: utf-8 -*-
from functools import reduce
def str2float(s):
    def intfn(x,y):
        return x*10+y
    num=s.find('.')
    for i in range(num):
        int_part=reduce(intfn,map(int,s[i]))
    for j in range(num+1,len(s)):
        flo_part=reduce(intfn,map(int,s[i])
    return int_part+flo_part*10**(-(len(s)-num-1))
            





print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
