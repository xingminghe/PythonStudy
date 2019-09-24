# pack布局案例
import tkinter

# grid布局案例
import tkinter

baseFrame = tkinter.Tk()

#下面被注释掉的一行代码跟下面两行代码等效
#lb1 = tkinter.Label(baseFrame, text="账号: ").grid(row=0, sticky= tkinter.W)
lb1 = tkinter.Label(baseFrame, text="账号: ")
lb1.grid(row=0, sticky= tkinter.E)

en = tkinter.Entry(baseFrame)
en.grid(row=0, column=1, sticky=tkinter.E)
print(en.grid_size())


lb2 = tkinter.Label(baseFrame,text="密码：").grid(row=1,sticky=tkinter.E)
tkinter.Entry(baseFrame).grid(row=1, column=1, sticky=tkinter.E)

lb2 = tkinter.Label(baseFrame, text="验证码: ").grid(row=2, sticky= tkinter.E)
tkinter.Entry(baseFrame).grid(row=2, column=1, sticky=tkinter.E)

print(en.grid_size())
btn = tkinter.Button(baseFrame, text="登录").grid(row=8, column=1, sticky=tkinter.W)


baseFrame.mainloop()