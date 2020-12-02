# -*- coding:utf-8 -*-
# from ipdb import set_trace
# set_trace()
from LazyTools import DM
import win32com
import win32process  #进程模块  需要安装 pywin32 包
import win32con      #系统定义
import win32api      #调用系统模块
import ctypes        #C语言类型
import win32gui      #界面
import win32com.client
import os
import re
import sys
from subprocess import check_output
dm = DM()
# hwnds = dm.EnumWindow(0, u"记事本")
# dm.ActiveWindow(hwnd=hwnds[0])
# Edithwnd = dm.EnumWindow(hwnds[0], "", "Edit", 2+4)
# sEdithwnd = str(Edithwnd)
# a = "你好".decode("utf-8").encode("gb18030")
# dm.MoveClick(1000, 600, 0.3)
# dm.BindWindow(sEdithwnd, "normal", "dx", "dx", 0)
# dm.KeyPress("1", 0.3)
# print(dm.version)
# a = raw_input()
# print(dm.SetKeypaDelay("dx", 10))

# mydm = win32com.client.Dispatch('dm.dmsoft')
# mydm = win32com.client.DispatchEx('dm.dmsoft')
# print(mydm.SetKeypadDelay("dx", 10))
# print(mydm.ver())

def GetProcessModules():
    handle   = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, pid )
    hModule  = win32process.EnumProcessModules(handle)
    temp=[]
    for i in hModule:
        temp.append([hex(i),debugfile(win32process.GetModuleFileNameEx(handle,i))])
    win32api.CloseHandle(handle)
    return temp
mydm = win32com.client.DispatchEx('dm.dmsoft')
print(mydm.ver())
PROCESS_ALL_ACCESS=(0x000F0000|0x00100000|0xFFF)    #一个常量，标识最高权限打开一个程序
myHwnd = win32api.GetCurrentProcessId()
# hid = win32api.GetCurrentThreadId()
# win32process.GetWindowThreadProcessId()      #根据窗体抓取进程编号
phand=win32api.OpenProcess(PROCESS_ALL_ACCESS, False, myHwnd)   #用最高权限打开进程线程
hModule  = win32process.EnumProcessModules(phand)
print(hModule)
a = raw_input(u" please input infomation ")
