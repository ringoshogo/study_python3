# 課題6 CSVファイルをHTML画面から指定できるようにする

import tkinter as tk
import tkinter.filedialog as fd
import platform
import os
import pathlib

# exe化後にカレントディレクトリを取得する
from os import chdir
from os.path import dirname
from sys import executable

# tkアプリウィンドウを開かないように制御
root = tk.Tk()
root.withdraw()
root.geometry("0x0") # サイズを0にする
root.overrideredirect(1) # サイズを0にしても残るタイトルバーを削除する
system = platform.system()

def select_save_file():

    if system == "Windows":
        root.deiconify()
    
    root.update()
    root.attributes('-topmost', True)
    root.lift()
    root.focus_force()

    file_path = fd.askopenfilename(
        initialdir = "./",
        title = "保存先を選択してください。",
        filetypes=[("CSV", ".csv")]
    )

    if system == "Windows":
        root.withdraw()

    return file_path


