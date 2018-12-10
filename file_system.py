import os
import win32api
import shutil


class FileSystem:
    def __init__(self, base_path):
        self.discs = win32api.GetLogicalDriveStrings().split("\x00")[:-1]
        os.chdir(base_path)
        self.path = os.getcwd()
        self.base = False

    def vpered(self, name):
        if self.base:
            self.path = name
            self.base = False
            return
        elif self.path in self.discs:
            self.path = self.path + name
        else:
            self.path = self.path + '\\'[0] + name

    def nazad(self):
        if self.base:
            return
        if self.path in self.discs:
            self.path = ''
            self.base = True
            return
        else:
            self.path = os.path.split(self.path)[0]

    def remove(self, name):
        try:
            os.remove(self.full_name(name))
            return True
        except Exception:
            return False
    
    def vse(self):
        if self.base:
            return self.discs
        spisok = os.listdir(self.path)
        return self.preobr(spisok)

    def preobr(self, sp):
        return sp

    def new_papka(self, name):
        try:
            os.mkdir(self.path + '\\'[0] + name)
            return True
        except Exception:
            return False

    def new_txt(self, name):
        try:
            with open(name + '.txt', 'w') as f:
                pass
            return True
        except Exception:
            return False

    def rename(self, name, new_name):
        try:
            os.rename(self.path + '\\'[0] + name,
                      self.path + '\\'[0] + new_name)
            return True
        except Exception:
            return False
    
    def copy(self, name, new_dir):
        try:
            shutil.copy2(self.path + '\\'[0] + name, new_dir + '\\'[0] + name)
            return True
        except Exception:
            return False

    def open(self, name):
        try:
            if os.path.isfile(self.path + '\\'[0] + name):
                os.startfile(self.path + '\\'[0] + name)
                return True
            self.vpered(name)
            return True
        except Exception:
            return False

