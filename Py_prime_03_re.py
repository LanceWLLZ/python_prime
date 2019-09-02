# _*_ coding: utf-8 _*_
# 开发人员：Lance_wllz
# 开发人员 86186
# 开发时间 2019/8/2710:49
# 文件名称 Py_prime_03_re
# 开发工具:PyCharm

''''''
# 正则表达式
'''
正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
re 模块使 Python 语言拥有全部的正则表达式功能。
compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。
re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数
'''
import re
#   python 01 re.match
'''
    re.match(pattern, string, flags=0)
    re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
'''
x = 1
if(x==1):
    print(re.match('www', 'www.runoob.com'))
    print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配成功
    print(re.match('com', 'www.runoob.com'))         # 不是起始位置匹配成功

