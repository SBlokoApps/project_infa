# Version 1.0
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
        try:
            if self.base:
                return self.preobr(self.discs)
            spisok = os.listdir(self.path)
            return self.preobr(spisok)
        except Exception:
            return 'Vse Ploxo'

    def fix_len(self, spisok, real):
        abc = spisok[0]
        ef = spisok[1]
        if len(abc) > 40:
            abc = abc[:38] + '...'
        else:
            abc = abc + '  ' * (40 - len(abc))
        if len(ef) > 13:
            ef = ef[:11] + '...'
        else:
            ef = ef + '  ' * (13 - len(ef))
        return [abc, ef, real]
    
    def preobr(self, sp):
        spisok2 = []
        for i in sp:
            if i in self.discs:
                spisok2.append(self.fix_len([i, '<>'], i))
                continue
            if '.bin' in i.lower() or '.sys' in i.lower():
                continue
            if '.dat' in i.lower():
                continue
            if self.path == 'C:\\' and i == 'Documents and Settings':
                continue
            if os.path.isfile(self.path + '\\'[0] + i):
                if i.count('.') == 1:
                    spisok2.append(self.fix_len(i.split('.'), i))
                elif i.count('.') == 0:
                    spisok2.append(self.fix_len([i, '-'], i))
                else:
                    i2 = i.split('.')
                    spisok2.append(self.fix_len(['.'.join(i2[:-1]), i2[-1]], i))
            else:
                spisok2.append(self.fix_len([i, '<dir>'], i))
        return spisok2

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
