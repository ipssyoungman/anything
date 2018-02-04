# -*- coding: utf-8 -*-
def normalize(name):
    s=name
    s=s.lower()
    l1=chr(ord(s[0])-32)#把第一个小写字母对应的大写字母算出来，ASCII码差32
    s=l1+s[1:]#把大写字母放到最前面
    return s



# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
