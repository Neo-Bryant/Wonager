#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Neo-Bryant

from time import sleep
from tkinter.font import BOLD
import pandas
import os
from tkinter import *
from tkmacosx import Button

 # 定义一个类，定义完整的功能，再根据逻辑进行修改
class Wonager():
    def __init__(self, window) -> None:
        '''基本属性定义'''
        self.window = window
        self.window.overrideredirect(True)    #去掉标题和边框的功能

        # 全局变量定义，标题及副标题
        self.title = 'Wonger'
        self.sub_title = 'Focus on what you doing today'

        # 获取电脑屏幕的分辨率大小
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        # 窗口的初始值大小，以及全屏时的大小定义
        self.normal = (1068, 681)
        self.zoomed = (self.screen_width, self.screen_height)

        # 个人署名
        self.signature = 'zengcaijue'
    
    # 窗口初始化配置
    def init(self, size='normal', color='white'):
        '''配置窗口'''
        # 窗口标题
        self.window.title(self.title)

        # 设置窗口大小
        if size == 'icon':      # 最小化（隐藏）
            self.window.state('icon')
        elif size == 'zoomed':    # 最大化（全屏）
            # self.window.state('zoomed')    # 实践证明，下面的方法在切换的过程中，更加自然一些
            self.window.geometry('%dx%d+0+0' % self.zoomed)
        else:                       # 默认大小
            self.window.geometry('%dx%d+10+10' % self.normal)
        
        # 获取当前窗口的实际大小
        self.window.update()
        self.win_width = self.window.winfo_width()
        self.win_height = self.window.winfo_height()

        print(self.win_width)
        print(self.win_height)

        # 窗口背景颜色
        self.window.config(bg=color)

    # 获取点击的坐标位置
    def get_pos(self, event):
        global xwin
        global ywin

        xwin = event.x
        ywin = event.y

    # 获取移动的位置，计算移动后的窗口位置，重新设置窗口的位置
    def move_window(self, event):
        self.window.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')
        # print(event.x_root, event.y_root)

    # 鼠标进入关闭按钮时会变红色
    def change_on_hovering(self, event):
        self.quit_botton['bg'] = 'red'

    # 鼠标离开按钮时会变会原来的颜色
    def return_to_normal_state(self, event):
        self.quit_botton['bg'] = self.header_border_bg
    
    # 最大化和正常大小切换，正负逻辑实现按钮复用
    def zoom(self):
        global i
        if i == 1:
            size = 'zoomed'
            self.init(size=size, color='red')
            # self.header_frame_background.config(width=self.win_width)
            # self.header_frame.config(width=self.win_width)
            self.zoom_button.config(text='⧉')           
        else:
            size = 'normal'
            self.init(size=size, color='green')
            # self.header_frame_background.config(width=self.win_width)
            self.header_frame.config(width=self.win_width)
            self.zoom_button.config(text='◻︎')
        i = -i

    def header(self, subtitle='个人工作管理工具', color_bg='gray'):
        '''顶部配置'''

        # 定义：背景色，边框色=按钮色
        self.header_bg = color_bg
        self.header_border_bg = '#666666'
        self.header_fg = 'black'

        # 背景框——背景框+背景=有边框线的背景
        # self.header_frame_background = Frame(self.window, width=self.win_width, height=61, bg=self.header_bg)
        # self.header_frame_background.pack(expand=True, fill='both')
        # self.header_frame_background.pack_propagate(0)

        self.header_frame = Frame(self.window, width=self.win_width, height=60, relief=FLAT)
        self.header_frame.pack(side='top', anchor=N, expand=True, fill='x')
        self.header_frame.pack_propagate(0)

        # 右上角按钮定义
        self.quit_botton = Button(self.header_frame, text='×', width=30, fg='white', bg=self.header_border_bg, command=lambda:self.window.quit())
        self.quit_botton.pack(side='right', anchor=NE, pady=5)

        self.zoom_button = Button(self.header_frame, text='◻︎', width=30, fg='white', bg=self.header_border_bg, command=self.zoom)
        self.zoom_button.pack(side='right', anchor=NE, pady=5)

        self.icon_button = Button(self.header_frame, text='−', width=30, fg='white', bg=self.header_border_bg, command=lambda:self.init(size='icon'))
        self.icon_button.pack(side='right', anchor=NE, pady=5)

        # 标题及副标题设置
        Label(self.header_frame, text=self.title, font=('微软雅黑', 16, BOLD), fg=self.header_fg).pack(anchor=NW, padx=10, pady=5)
        Label(self.header_frame, text=self.sub_title, font=('微软雅黑', 12), fg=self.header_fg).pack(anchor=NW, padx=10, pady=0)
        
        # 布局
        

        # 事件绑定，触发函数
        self.header_frame.bind("<B1-Motion>", self.move_window)
        self.header_frame.bind("<Button-1>", self.get_pos)
        self.quit_botton.bind('<Enter>', self.change_on_hovering)
        self.quit_botton.bind('<Leave>', self.return_to_normal_state)

    def sidebar(self, name='Devoper', color_bg='#F5F5F5'):
        '''侧边栏配置'''
        # 定义：背景色，边框色，按钮色，字体色
        self.sidebar_bg = color_bg
        self.sidebar_border_bg = 'gray'
        self.sidebar_fg = 'black'
        self.sidebar_button_bg = ''

        self.sidebar_frame = Frame(self.window, width=200, height=self.win_height-61, bg=self.sidebar_bg)

        self.sidebar_frame.pack(anchor=SW, side='left', expand=True, fill='both')
        self.sidebar_frame.pack_propagate(0)




    def mainbody(self):
        '''主体配置'''
        # 定义：背景色，边框色
        self.mainbody_bg = 'white'
        self.mainbody_border_bg = 'white'    # #666666
        self.mainbody_fg = 'black'

        # 背景
        self.mainbody_frame = Frame(self.window, width=self.win_width-201, height=self.win_height-61, bg=self.mainbody_bg)

        self.mainbody_frame.pack(anchor=NW, side='right',expand=True, fill='both')
        self.mainbody_frame.pack_propagate(0)


    




def main():
    global i
    root = Tk()
    a = Wonager(root)
    a.init(color='gray')
    a.header()
    a.sidebar()
    a.mainbody()
    i = 1

    root.mainloop()

main()