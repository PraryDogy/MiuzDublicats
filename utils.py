from calendar import c
import json
import os
import subprocess
import tkinter
from tkinter.ttk import Separator, Progressbar, Style

import tkmacosx

import cfg


def on_exit():
    cfg.FLAG = False
    cfg.ROOT.destroy()


def place_center(top_level):
    """
    Place new tkinter window to center relavive main window.
    * param `top_level`: tkinter.TopLevel
    """
    cfg.ROOT.update_idletasks()
    x, y = cfg.ROOT.winfo_x(), cfg.ROOT.winfo_y()
    xx = x + 600//2-top_level.winfo_reqwidth()//2
    yy = y + 600//2-top_level.winfo_reqheight()//2

    top_level.geometry(f'+{xx}+{yy}')


class MyButton(tkinter.Label):
    """
    Tkinter Label with custom style.
    * method `cmd`: bind function to mouse left click
    * method `press`: simulate button press with button's bg color
    """

    def __init__(self, master, **kwargs):
        tkinter.Label.__init__(self, master, **kwargs)
        self.configure(
            bg=cfg.BGBUTTON, fg=cfg.FONTCOLOR,
            width=17, height=2)

    def cmd(self, cmd):
        """
        Binds tkinter label to mouse left click.
        * param `cmd`: lambda e: some_function()
        """
        self.unbind('<Button-1')
        self.bind('<Button-1>', cmd)

    def press(self):
        """
        Simulates button press with button's bg color
        """
        self.configure(bg=cfg.BGPRESSED)
        cfg.ROOT.after(100, lambda: self.configure(bg=cfg.BGBUTTON))


class MyLabel(tkinter.Label):
    """
    Tkinter Label with custom style.
    """
    def __init__(self, master, **kwargs):
        tkinter.Label.__init__(self, master, **kwargs)
        self.configure(bg=cfg.BGCOLOR, fg=cfg.FONTCOLOR)


class MyFrame(tkinter.Frame):
    """
    Tkinter Frame with custom style.
    """
    def __init__(self, master, **kwargs):
        tkinter.Frame.__init__(self, master, **kwargs)
        self.configure(bg=cfg.BGCOLOR)


class SearchDublicats():
    def __init__(self):
        old_scrl = [v for k, v in cfg.ROOT.children.items() if 'canv' in k][0]
        old_scrl.destroy()

        scrollable = tkmacosx.SFrame(
            cfg.ROOT, bg=cfg.BGSEARCH, scrollbarwidth=10)
        scrollable.pack(fill=tkinter.BOTH, expand=1, pady=(15, 0))

        if type(cfg.FILE_PATH) != str or len(cfg.FILE_PATH) == 0:
            self.no_file(scrollable, 'Выберите файл')
            return

        stats = os.stat(cfg.FILE_PATH)
        src_props = (
            int(stats.st_birthtime),
            int(stats.st_mtime),
            int(os.path.getsize(cfg.FILE_PATH))
            )

        with open(os.path.join(cfg.CFG_FOLDER, cfg.CFG_FILE), 'r') as file:
            config = json.load(file)

        for root, _, files in os.walk(config['search_path']):
            cfg.DYNAMIC['text'] = root
            for file in files:

                if not cfg.FLAG:
                    return

                path = os.path.join(root, file)
                get = os.stat(path)
                props = (
                    int(get.st_birthtime),
                    int(get.st_mtime),
                    int(os.path.getsize(path))
                    )

                if props == src_props:
                    self.file_frame(scrollable, path)

        if len(scrollable.children.items()) == 0:
            self.no_file(scrollable, 'Нет совпадений')

    def no_file(self, scrollable, txt):
        for k, v in scrollable.children.items():
            v.destroy()

        lbl = MyLabel(scrollable, text=txt)
        lbl['bg'] = cfg.BGSEARCH
        lbl.pack(pady=15)

    def file_frame(self, scrollable, path):
        frame = tkinter.Frame(scrollable, bg=cfg.BGSEARCH)
        frame.pack(pady=(15, 0), fill=tkinter.X)

        lbl = MyLabel(frame, text=path)
        lbl.configure(anchor=tkinter.W, justify=tkinter.LEFT, bg=cfg.BGSEARCH)
        lbl.pack(fill=tkinter.X, padx=15)

        btn_frame = tkinter.Frame(frame, bg=cfg.BGSEARCH)
        btn_frame.pack()

        btn_folder = MyButton(btn_frame, text='Открыть папку')
        btn_folder.configure(height=1, width=13)
        btn_folder.cmd(lambda e: self.open_folder(btn_folder, path))
        btn_folder.pack(pady=(5, 0), side=tkinter.LEFT)

        btn_rem = MyButton(btn_frame, text='Удалить')
        btn_rem.configure(height=1, width=13)
        btn_rem.cmd(lambda e: self.rem_file(frame, path))
        btn_rem.pack(pady=(5, 0), padx=(15,0), side=tkinter.RIGHT)

        sep = Separator(frame, orient=tkinter.HORIZONTAL)
        sep.pack(fill=tkinter.X, padx=30, pady=(15, 0))

    def open_folder(self, btn, path):
        btn.press()
        path = os.path.join(os.sep, *path.split('/')[:-1])
        subprocess.check_output(["/usr/bin/open", path])

    def rem_file(self, frame, path):
        os.remove(path)
        frame.destroy()
