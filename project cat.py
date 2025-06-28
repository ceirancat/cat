# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.messagebox as tm
def onclick():
    tm.showinfo(title="已確認", message="姓名已送出!")
window= tk.Tk()
window.title("Project cat")
window.geometry("500x600")
label=tk.Label(window,text="歡迎來到 貓咪計畫",bg="#FFF",fg="#5FC")
label.pack()
label2=tk.Label(window,text="輸入玩家名稱")
label2.pack()
entry=tk.Entry(window,width=30)
entry.pack()
button=tk.Button(window,text="確認", command=onclick)
button.pack()
window.mainloop()

