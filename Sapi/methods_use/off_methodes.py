import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_camera():
    sp.run('start microsoft.Windows.camera:',shell=True)


def open_note():
    os.startfile(paths['notepad'])

def open_cmd():
    os.system('start cmd')

def open_calc():
    os.startfile((paths['calculator']))