import tkinter as tk


class Application(tk.Frame):
    # bindするイベント詳細を取得する関数
    def getEventDetail(self, event):
        print(event.keysym)

    # 追加bind用関数。実行される場合に、hello worldを出力する。
    def getAddFunc(self, event):
        print('hello world')

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        self.master.geometry("300x200")

        # label Widgetを作成する。
        # text : テキスト情報
        # labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(text="test")

        # イベントと関数の実行を紐づける。
        # 第一引数 : イベント内容。label Widgetがクリックされた場合
        # 第二引数 : 第一引数が試行された場合に、実行する関数名。getEventDetailとする。
        # 戻り値 : なし
        label.bind("<ButtonPress>", self.getEventDetail)
        # イベントと関数の実行を紐づける。
        # 第一引数 : イベント内容。label Widgetがクリックされた場合
        # 第二引数 : 第一引数が試行された場合に、実行する関数名。getAddFuncとする。
        # 第三引数 : ''か'+'を指定する。
        # ''の場合、前コードのbindで宣言された関数名を実行しないで今回bindする関数名を実行する。今回の場合、getEventDetailを実行しないで、getAddFuncを実行する。
        # '+'の場合、前コードのbindで宣言された関数名を実行して、今回bindする関数名を実行する。今回の場合、getEventDetailを実行して、getAddFuncを実行する。
        # 戻り値 : なし
        label.bind("<ButtonPress>", self.getAddFunc, '+')

        # Windowを親要素とした場合に、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label.pack()


# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    app.mainloop()
