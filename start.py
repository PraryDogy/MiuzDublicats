import tkinter

import cfg
from bar_menu import BarMenu
from widgets import StartBtn, WhatSearch, WhereSearch

cfg.ROOT.title(cfg.APP_NAME)
cfg.ROOT.configure(padx=15, pady=15, bg=cfg.BGCOLOR)

cfg.ROOT.createcommand(
    'tk::mac::ReopenApplication', cfg.ROOT.deiconify)

WhereSearch(cfg.ROOT).pack(pady=(0, 15), fill=tkinter.X)
WhatSearch(cfg.ROOT).pack(fill=tkinter.X)
StartBtn(cfg.ROOT).pack(pady=(15, 15))
cfg.SCROLLABLE.pack(fill=tkinter.BOTH, expand=1)
BarMenu()

cfg.ROOT.update_idletasks()

w, h = cfg.ROOT.winfo_screenwidth()//2, cfg.ROOT.winfo_screenheight()//2
ww, hh = 600//2, 600//2
x, y =  w-ww, h-hh
cfg.ROOT.geometry(f'600x600+{x}+{y}')

cfg.ROOT.deiconify()
cfg.ROOT.mainloop()
