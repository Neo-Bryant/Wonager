#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Neo-Bryant

from time import sleep
import pandas
import os
from tkinter import *


# 定义一个类，定义完整的功能，再根据逻辑进行修改
class Wonager():
    def __init__(self, window) -> None:
        '''基本属性定义'''
        self.window = window

        # 全局变量定义
        self.title = 'Wonger'
        self.sub_title = 'focus on what you doing today'
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.normal = (1068, 681)
        self.zoomed = (self.screen_width, self.screen_height)
        self.signature = 'zengcaijue'
    
    # 窗口初始化配置
    def init(self, size='normal', color='white'):
        '''配置窗口'''
        # 窗口标题
        self.window.title = self.title

        # 设置窗口大小
        if size == 'icon':      # 最小化（隐藏）
            self.window.state('icon')
        elif size == 'zoomed':    # 最大化（全屏）
            # self.window.state('zoomed')
            self.window.geometry('%dx%d+0+0' % self.zoomed)
        else:                       # 默认大小
            self.window.geometry('%dx%d+10+10' % self.normal)
        
        # 获取当前窗口的实际大小
        self.win_width = self.window.winfo_width()
        self.win_height = self.window.winfo_height()

        # 窗口背景颜色
        self.window.config(bg=color)

    def header(self):
        '''顶部配置'''
        self.header_frame = Frame(self.window)

    def sidebar(self):
        '''侧边栏配置'''
        pass

    def mainbody(self):
        '''主体配置'''
        pass

# 正负逻辑实现按钮可复用
def zoom(obj):
    global i
    if i == 1:
        size = 'zoomed'
        obj.init(size=size, color='red')
    else:
        size = 'normal'
        obj.init(size=size, color='green')
    i = -i




def main():
    global i
    root = Tk()
    a = Wonager(root)
    a.init(color='gray')
    i = 1
    Button(root, text='−', command=lambda:a.init(size='icon')).pack()
    Button(root, text='⧉', command=lambda:zoom(a)).pack()
    Button(root, text='×', command=lambda:root.quit()).pack()
    root.mainloop()

main()