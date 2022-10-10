import json
import os
import threading
import tkinter
from tkinter import filedialog

import cfg
from utils import MyButton, MyFrame, MyLabel, SearchDublicats


class Globals:
    file_widget = tkinter.Label
    search_widget = tkinter.Label

    with open(os.path.join(cfg.CFG_FOLDER, cfg.CFG_FILE), 'r') as file:
        config = json.load(file)


class WhereSearch(MyFrame):
    def __init__(self, master):
        MyFrame.__init__(self, master)
        self.search_btn()
        self.search_label()

    def search_btn(self):
        btn = MyButton(self, text='Где искать', pady=2)
        btn.configure(width=13, height=1)
        btn.cmd(lambda e: self.search_cmd(btn))
        btn.pack(side=tkinter.LEFT)

    def search_cmd(self, btn):
        btn.press()
        Globals.config['search_path'] = filedialog.askdirectory()

        if len(Globals.config['search_path']) == 0:
            return

        with open(os.path.join(cfg.CFG_FOLDER, cfg.CFG_FILE), 'w') as file:
            json.dump(Globals.config, file, indent=4)

        Globals.search_widget['text'] = Globals.config['search_path']

    def search_label(self):
        Globals.search_widget = MyLabel(
            self, text=Globals.config['search_path'])
    
        if len(Globals.config['search_path']) == 0:
            Globals.search_widget['text'] = 'Укажите место поиска'

        Globals.search_widget.pack(padx=(15, 0), side=tkinter.LEFT)


class WhatSearch(MyFrame):
    def __init__(self, master):
        MyFrame.__init__(self, master)
        self.file_btn()
        self.file_label()

    def file_btn(self):
        btn = MyButton(self, text='Что искать', pady=2)
        btn.configure(width=13, height=1)
        btn.cmd(lambda e: self.file_cmd(btn))
        btn.pack(side=tkinter.LEFT)

    def file_cmd(self, btn):
        btn.press()
        file_path = filedialog.askopenfilename()
        
        if len(file_path) == 0:
            return

        cfg.FILE_PATH = file_path
        Globals.file_widget['text'] = cfg.FILE_PATH

    def file_label(self):
        Globals.file_widget = MyLabel(
            self, text='Выберите файл для поиска дубликатов')
        Globals.file_widget.pack(padx=(15, 0), side=tkinter.LEFT)


class Dynamic(MyLabel):
    def __init__(self, master):
        MyLabel.__init__(self, master)
        cfg.DYNAMIC = self
        self.configure(anchor=tkinter.W, justify=tkinter.LEFT, padx=30)


class StartBtn(MyButton):
    def __init__(self, master):
        MyButton.__init__(self, master, text='Старт')
        self.cmd(lambda e: self.btn_cmd())

    def btn_cmd(self):
        self.press()
        cfg.FLAG = True

        self['text'] = 'Стоп'
        self.cmd(lambda e: self.stop_search())

        t1 = threading.Thread(target=SearchDublicats)
        t1.start()

        while t1.is_alive():
            cfg.ROOT.update()

        self['text'] = 'Старт'
        self.cmd(lambda e: self.btn_cmd())

    def stop_search(self):
        cfg.FLAG = False
        cfg.DYNAMIC['text'] = ''