# -*- coding:utf-8 -*-
import openpyxl
wb = openpyxl.Workbook()
ws = wb.active
ws.append([1,2,3])
wb.save("demo.xlsx")
