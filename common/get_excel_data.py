#!/usr/bin/python
# -*- coding: UTF-8 _*_

import xlrd


def get_excel_value(row):
    excel = xlrd.open_workbook('../testdata/testdata.xlsx')
    table = excel.sheets()[0]
    # print(table.nrows)  # 取总行数
    # print(table.ncols)  # 取总列数
    # print(table.row_values(0))  # 读取第一行的数据
    # print(table.col_values(0))  # 读取第一列的数据
    # print(table.cell_value(0, 0))  # 读取第一行的数据
    # for i in range(1,table.nrows):
    #     print(table.row_values(i))

    return table.cell_value(row, 1), table.cell_value(row, 2)
