import tkinter
from tkinter import DISABLED, NORMAL

import read
from PIL import Image, ImageTk

# 主窗口宽
root_width = 600
# 主窗口高
root_height = 400
# 背景图片位置
imagefile = "image/bj.jpg"
# 设置图标Logo要求128*128大小的ico格式 在线转ico：https://www.qtool.net/ico
#iconfile="image/logo.ico"
# 窗口名
root_name = "命运之手"

root= tkinter.Tk()
root.title(root_name)
root.geometry(str(root_width) + 'x' + str(root_height) + '+500+500')
root.resizable(width=False, height=False)
#设置图标logo 取消下行注释即可
#root.iconbitmap(iconfile)
img = ImageTk.PhotoImage(Image.open(imagefile).resize((root_width, root_height)))
backimagelable = tkinter.Label(root, image=img)
backimagelable.grid()

b=tkinter.Button
def extract():

    b.configure(state=DISABLED)
    def changelable(str):
        lable["text"] = str
        lable.update()
    lable.place(x=70, y=110, height=150, width=460)
    root.after(700, changelable(3))
    root.after(800, changelable(2))
    root.after(900, changelable(1))
    root.after(0, changelable(read.nextname()))
    b.configure(state=NORMAL)

lable = tkinter.Label(root, text="3", font=('microsoft yahei', 45, 'bold'))

b = tkinter.Button(root, text="抽取",command=extract, width=30, height=3)

b.place(x=180, y=290)
root.mainloop()

