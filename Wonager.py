#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Neo-Bryant

import pandas
import os
from tkinter import *


# 定义一个类，定义完整的功能，再根据逻辑进行个性
class Wonager():
    def __init__(self) -> None:
        '''基本属性定义'''
        self.title = 'Wonger'
        self.sub_title = 'focus on what you doing today'
        self.title_bg_color = 'grey'
        self.title_font_color = 'white'
        self.windows = Tk()
        self.windows.title = self.title
        self.windows.config(bg=self.title_bg_color)
    
    def config_screen(self, screen_type):
        '''配置窗口的大小'''
        pass
        self.windows.state('zoomed')
        self.windows.conify()

    def base(self):
        pass

a = Wonager
a.windows.mainloop()