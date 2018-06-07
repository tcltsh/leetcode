#!/usr/bin/env python
# coding=utf-8
# @Time    : 2018/4/16 20:42
# @Author  : litianshuang
# @Email   : litianshuang@jingdata.com
# @File    : test.py
# @Desc    :

import xlrd

def run():
    print("here")
    workbook = xlrd.open_workbook(r'C:\Users\BJQXDN0543\Desktop\top_company.xlsx')
    print(workbook.sheet_names())

if __name__ == "__main__":
    run()