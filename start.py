import tkinter

import cfg
from bar_menu import BarMenu
from utils import on_exit
from widgets import Dynamic, StartBtn, WhatSearch, WhereSearch

cfg.ROOT.title(cfg.APP_NAME)
cfg.ROOT.configure(padx=15, pady=15, bg=cfg.BGCOLOR)

cfg.ROOT.createcommand(
    'tk::mac::ReopenApplication', cfg.ROOT.deiconify)

cfg.ROOT.protocol("WM_DELETE_WINDOW", on_exit)
cfg.ROOT.bind('<Command-q>', lambda e: on_exit())

WhereSearch(cfg.ROOT).pack(pady=(0, 15), fill=tkinter.X)
WhatSearch(cfg.ROOT).pack(fill=tkinter.X)
Dynamic(cfg.ROOT).pack(pady=(15, 0), fill=tkinter.X)
StartBtn(cfg.ROOT).pack(pady=(15, 0))
cfg.SCROLLABLE.pack(fill=tkinter.BOTH, expand=1, pady=(15, 0))
BarMenu()

cfg.ROOT.update_idletasks()

w, h = cfg.ROOT.winfo_screenwidth()//2, cfg.ROOT.winfo_screenheight()//2
ww, hh = 600//2, 600//2
x, y =  w-ww, h-hh
cfg.ROOT.geometry(f'600x600+{x}+{y}')

cfg.ROOT.deiconify()
cfg.ROOT.mainloop()
