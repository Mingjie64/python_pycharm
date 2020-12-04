# import requests
# from pprint import pprint
import random
from System_management.role_management import saveRolePermission
#
# res = requests.get('http://localhost/rivalCompany/listParentCompany')
#
# if res.status_code == 200 :
#     print("200,通过！")
#
# pprint(res.status_code)
# pprint(res.json(), width=0)


# a = [123,321,3,4,5,6,2,4,7]
#
# list = list(set(a))
# print(list)
# list1=[1,2,3]
# print((',').join(str(x) for x in list1))
import tkinter as tk

window = tk.Tk()
window.title('MJ Script')
window.geometry('500x300')

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=30, height=2)
l.pack()

t1 = tk.Entry(window, show=None, font=('Arial',14))
t2 = tk.Entry(window, show=None, font=('Arial',14))
t1.pack()
t2.pack()

on_hit = False
def ceshi():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('hitting')
    else:
        on_hit = False
        var.set('')

b = tk.Button(window, text='button1', font=('Arial', 12), width=10, height=1, command=ceshi)
b.pack()

window.mainloop()

# from Tkinter import *
# import tkMessageBox
# 
# 
# def getInput(title, message):
#     def return_callback(event):
#         print('quit...')
#         root.quit()
# 
#     def close_callback():
#         tkMessageBox.showinfo('message', 'no click...')
# 
#     root = Tk(className=title)
#     root.wm_attributes('-topmost', 1)
#     screenwidth, screenheight = root.maxsize()
#     width = 300
#     height = 100
#     size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
#     root.geometry(size)
#     root.resizable(0, 0)
#     lable = Label(root, height=2)
#     lable['text'] = message
#     lable.pack()
#     entry = Entry(root)
#     entry.bind('<Return>', return_callback)
#     entry.pack()
#     entry.focus_set()
#     root.protocol("WM_DELETE_WINDOW", close_callback)
#     root.mainloop()
#     str = entry.get()
#     root.destroy()
#     return str
