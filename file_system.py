import os


class FileSystem:
    def __init__(self, base_path):
        self.path = base_path

    def vpered(self, name):
        self.path += '/'
        self.path += name

    def nazad(self):
        self.path = '/'.join(self.path.split('/')[:-1])

    def copy(self, name, new_dir):
        pass

    def delete(self, name):
        pass

    def move(self, name, new_dir):
        if self.copy(name, new_dir):
            if self.delete(name):
                return True
            return False

    def rename(self, name, new_name):
        poln_name_1 = self.path + '/' + name
        poln_name_2 = self.path + '/' + new_name
        try:
            os.rename(poln_name_1, poln_name_2)
            return True
        except Exception:
            return False

    def vse(self):
        spisok = 0
        self.filter(spisok)

    def rejim(self, rejim):
        pass

    def filter(self, sp):
        return sp

    def new_papka(self, name):
        try:
            os.mkdir(self.path + '/' + name)
            return True
        except Exception:
            return False

    def new_txt(self, name):
        pass

    def zapusk(self, name):
        os.startfile(self.path + '/' + name)
