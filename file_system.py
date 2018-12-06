import os


class FileSystem:
    def __init__(self, base_path):
        self.path = base_path
        self.forms = {}
        with open('set.txt', 'r') as f:
            for line in f:
                i = line.split()
                self.forms[i[0]] = i[1:]

    def vpered(self, name):
        self.path += '/'
        self.path += name

    def nazad(self):
        try:
            self.path = '/'.join(self.path.split('/')[:-1])
            return True
        except Exception:
            return False

    def copy(self, name, new_dir):
        try:
            self.copy(self.path + '/' + name, new_dir)
            return True
        except Exception:
            return False

    def delete(self, name):
        try:
            os.remove(self.path + '/' + name)
            return True
        except Exception:
            return False

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
        spisok = os.listdir(self.path)
        return self.preobr(spisok)

    def rejim(self, rej):
        with open('set.txt', 'r') as f:
            

    def preobr(self, old_sp):
        new_sp = [abc.split('/')[-1] for abc in old_sp]
        new_sp2 = []
        pass

    def new_dir(self, name):
        try:
            os.mkdir(self.path + '/' + name)
            return True
        except Exception:
            return False

    def new_txt(self, name):
        pass

    def open(self, name):
        os.startfile(self.path + '/' + name)
