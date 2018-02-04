# -*- coding: utf-8 -*-
def trim(s):
    a=0
    b=len(s)
    while s[a]==' ':
        a+=1
    while  s[b-1]==' ':
        b=b-1
    return s[a:b]

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')

else:
    print('测试成功!')
