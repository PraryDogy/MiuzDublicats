import json
import os
import tkinter

import tkmacosx

APP_NAME = 'MiuzDublicats'
APP_VER = '1.0.2'

FONTCOLOR = "#E2E2E2"
BGCOLOR = "#222222"
BGBUTTON = "#434343"
BGPRESSED = '#395432'
BGSEARCH = '#1C1C1C'

ROOT = tkinter.Tk()
ROOT.withdraw()
SCROLLABLE = tkmacosx.SFrame(ROOT, bg=BGSEARCH, scrollbarwidth=10)

FILE_PATH = str

CFG_FOLDER = os.path.join(
    os.path.expanduser('~'), 'Library', 'Application Support', APP_NAME)
CFG_FILE = 'cfg.json'

if not os.path.exists(CFG_FOLDER):
    os.makedirs(CFG_FOLDER)

if not os.path.exists(os.path.join(CFG_FOLDER, CFG_FILE)):
    data = {'search_path': ''}

    with open(os.path.join(CFG_FOLDER, CFG_FILE), 'w') as file:
        json.dump(data, file, indent=4)
