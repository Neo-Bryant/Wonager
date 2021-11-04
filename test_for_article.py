from tkinter import *
from tkmacosx import Button
root = Tk()
root.geometry('500x400+100+100')
root.config(bg='gray')
frame1 = Frame(root, width=500, height=200, bg='gray')
Label(frame1, text='hello tkinter').pack()
frame1.pack()
frame1.pack_propagate(0)    # 设置为0可使组件大小不变
# root.mainloop()
root.update()
print(root.winfo_width())
aa = Button(text='按钮测试', background='red')
# aa.config(background='blue')
aa.pack()
root.title('dddd')
root.mainloop()