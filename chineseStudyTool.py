from tkinter import *
from tkinter import ttk
import tkinter as tk
from googletrans import Translator
import sys
from pypinyin import pinyin, lazy_pinyin, Style

class Application(tk.Frame):
    
    # ボタンがクリックされたら呼ばれる関数
    def CtoJbtn1_clicked(self):

        # 文字列を翻訳
        lines = self.trans(self.CtoJtext1.get(1.0,END),src='zh-CN' ,dest='ja')
        print("--翻訳--")
        print("--"+lines+"--")
        t = StringVar()
        t.set(lines + self.getPinYin(self.CtoJtext1.get(1.0,END)))

        # 翻訳結果をtextに表示
        self.CtoJtext2.delete(1.0, END)
        self.CtoJtext2.insert(INSERT,t.get())

    # Widgetの初期化
    def CtoJInit(self):

        if(self.status == 0):
            self.CtoPframe.pack_forget()
            self.status = 2
        elif(self.status == 1):
            self.JtoCframe.pack_forget()
            self.status = 2
        elif(self.status == 2):
            return

        # widgetの宣言
        self.CtoJframe = ttk.Frame(self.master, padding=10)

        self.CtoJtext1 = Text(self.CtoJframe , height = 10)
        self.CtoJtext1.insert(INSERT,"你好")
        self.CtoJtext2 = Text(self.CtoJframe , height = 5,font=("Helvetica", 24))
        self.CtoJbtn1 = ttk.Button(self.CtoJframe,text="中→日",width=50, command = self.CtoJbtn1_clicked )

        # wigetのセット
        self.CtoJframe.pack(expand = True, fill = BOTH)
        self.CtoJtext1.pack(expand = True, fill = BOTH)
        self.CtoJbtn1.pack(expand = True, fill = BOTH)
        self.CtoJtext2.pack(expand = True, fill = BOTH)
    


    # ボタンがクリックされたら呼ばれる関数
    def JtoCbtn1_clicked(self):

        # 文字列を翻訳
        lines = self.trans(self.JtoCtext1.get(1.0,END),src='ja' ,dest='zh-CN')
        print("--翻訳--")
        print("--"+lines+"--")
        t = StringVar()
        t.set(lines + self.getPinYin(lines))

        # textに表示
        self.JtoCtext2.delete(1.0, END)
        self.JtoCtext2.insert(INSERT,t.get())

    # フレームの初期化
    def jtoCInit(self):

        if(self.status == 0):
            self.CtoPframe.pack_forget()
            self.status = 1
        elif(self.status == 2):
            self.CtoJframe.pack_forget()
            self.status = 1
        elif(self.status == 1):
            return
        else:
            self.status = 1

        # widgetの初期化
        self.JtoCframe = ttk.Frame(self.master, padding=10)
        self.JtoCtext1 = Text(self.JtoCframe , height = 10)
        self.JtoCtext1.insert(INSERT,"こんにちは\n")
        self.JtoCtext2 = Text(self.JtoCframe , height = 5,font=("Helvetica", 24))
        self.JtoCbtn1 = ttk.Button(self.JtoCframe,text="日→中",width=50, command = self.JtoCbtn1_clicked )

        # widgetのセット
        self.JtoCframe.pack(expand = True, fill = BOTH)
        self.JtoCtext1.pack(expand = True, fill = BOTH)
        self.JtoCbtn1.pack(expand = True, fill = BOTH)
        self.JtoCtext2.pack(expand = True, fill = BOTH)

    def getPinYin(self,str):
        res = "\n"
        p =  pinyin(str)
        for c in p:
            for i in c:
                res += i+" ";
        return res

    # 翻訳した文字列を返す
    def trans(self ,str , src , dest):
        translator = Translator()

        # googletransの動作が不安定なため結果が帰ってくるまで繰り返す
        while True:
            try:
                translated = translator.translate(str, src = src ,dest = dest);
                break
            except Exception as e:
                translator = Translator()
        return translated.text

    # ボタンをクリックしたら呼ばれる
    def CtoPbtn1_clicked(self):

        # textから文字を所得して翻訳
        lines = self.CtoPtext1.get(1.0,END)
        print("--翻訳--")
        print("--"+lines+"--")
        t = StringVar()
        t.set( self.getPinYin(lines))

        # textに表示
        self.CtoPtext2.delete(1.0, END)
        self.CtoPtext2.insert(INSERT,t.get())
        
    def CtoPInit(self):
        if(self.status == 1):
            self.JtoCframe.pack_forget()
            self.status = 0
        elif(self.status == 2):
            self.CtoJframe.pack_forget()
            self.status = 0
        elif(self.status == 0):
            return

        # widgetの初期化
        self.CtoPframe = ttk.Frame(self.master, padding=10)
        self.CtoPtext1 = Text(self.CtoPframe , height = 10)
        self.CtoPtext1.insert(INSERT,"你好")
        self.CtoPtext2 = Text(self.CtoPframe , height = 5,font=("Helvetica", 24))
        self.CtoPbtn1 = ttk.Button(self.CtoPframe,text="中→Pn",width=50, command = self.CtoPbtn1_clicked )

        # widgetのセット
        self.CtoPframe.pack(expand = True, fill = BOTH)
        self.CtoPtext1.pack(expand = True, fill = BOTH)
        self.CtoPbtn1.pack(expand = True, fill = BOTH)
        self.CtoPtext2.pack(expand = True, fill = BOTH)

    def __init__(self,master):
        super().__init__(master)
#        self.pack()
        self.status = -1

        # ウィンドウの大きさ座標の設定
        master.geometry( "400x400+500+100") # 幅x高さ+ウィンドウのｘ座標+ウィンドウのｙ座標
        master.minsize(400, 400)
        master.columnconfigure(0, weight=1);
        master.rowconfigure(0, weight=1);

        self.jtoCInit()
        #常に最前面表示
        master.attributes("-topmost", True)
        # menubarの大元（コンテナ）の作成と設置
        menubar = Menu(master)
        master.config(menu=menubar)

        # menubarを親として設定メニューを作成と表示
        setting_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='日→中', command=lambda: self.jtoCInit())
        menubar.add_cascade(label="中→Pn", command=lambda: self.CtoPInit())
        menubar.add_cascade(label='中→日', command=lambda: self.CtoJInit())


def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()

if __name__ == "__main__":
    main()