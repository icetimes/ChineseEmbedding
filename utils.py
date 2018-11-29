# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 13:52
# @Author  : huyulan
# @Email   : huyulan@boe.com.cn
# @File    : test.py
# @Software: PyCharm
list = []
import os
with open("D:/boe-data/项目申请/糖尿病/糖尿病数据 - 副本.txt", "r", encoding="utf-8") as f:
    for line in f:
        split = line.split("\t", 8)
        filename = os.path.basename(split[0])
        ss= split[0].replace(filename,"")
        list.append(ss)
# v = frozenset(set)
for i in set(list):
    print(i)
