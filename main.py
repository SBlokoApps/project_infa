# Version 1.0
from file import *
from PyQt5.QtWidgets import QMainWindow, QDialog, QLineEdit, QApplication, QTableWidgetItem, QInputDialog, QAbstractItemView
from PyQt5.QtCore import QSize, Qt
import sys
from file_system import *
from Error47 import *


class Dialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.active = True
        self.name = ''
        self.all_names_l = []
        self.all_names_r = []
        self.b = Dialog()
        self.left = FileSystem('C:\\')
        self.right = FileSystem('D:\\')
        self.left_table.setColumnCount(2)
        self.right_table.setColumnCount(2)
        self.update()
        self.left_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.right_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.n_left.clicked.connect(self.nazad_l)
        self.n_right.clicked.connect(self.nazad_r)
        self.copy.clicked.connect(self.copied)
        self.dele.clicked.connect(self.delete)
        self.open.clicked.connect(self.new_name)
        self.new_dir.clicked.connect(self.dir)
        self.new_file.clicked.connect(self.txt)
        self.left_table.itemPressed.connect(self.get_item_l)
        self.right_table.itemPressed.connect(self.get_item_r)
        self.move.clicked.connect(self.moved)
        self.left_table.itemDoubleClicked.connect(self.opened)
        self.right_table.itemDoubleClicked.connect(self.opened)

    def update(self):
        self.name = ''
        l_fs = self.left.vse()
        r_fs = self.right.vse()
        if l_fs == 'Vse Ploxo':
            self.nazad_l()
            self.b.show()
            return
        if r_fs == 'Vse Ploxo':
            self.nazad_r()
            self.b.show()
            return
        self.all_names_l = [i[2] for i in l_fs]
        self.all_names_r = [i[2] for i in r_fs]
        len_left = len(l_fs)
        len_right = len(r_fs)
        self.left_table.setRowCount(len_left)
        self.right_table.setRowCount(len_right)
        for i in range(len_left):
            self.left_table.setItem(i, 0, QTableWidgetItem(l_fs[i][0]))
            self.left_table.setItem(i, 1, QTableWidgetItem(l_fs[i][1]))
        for i in range(len_right):
            self.right_table.setItem(i, 0, QTableWidgetItem(r_fs[i][0]))
            self.right_table.setItem(i, 1, QTableWidgetItem(r_fs[i][1]))
        self.left_table.resizeColumnsToContents()
        self.right_table.resizeColumnsToContents()
        
    def nazad_l(self):
        self.left.nazad()
        self.update()
    def copied(self):
        if self.name != '':
            if self.active:
                if not self.left.copy(self.name, self.right.path):
                    self.b.show()
            else:
                if not self.right.copy(self.name, self.left.path):
                    self.b.show()
        self.update()
    def moved(self):
        if self.name != '':
            if self.active:
                if not self.left.move(self.name, self.right.path):
                    self.b.show()
            else:
                if not self.right.move(self.name, self.left.path):
                    self.b.show()
        self.update()
    def dir(self):
        text, ok = QInputDialog.getText(self, 'Введите название',
                                            '', QLineEdit.Normal, '')
        if ok:
            if self.active:
                if not self.left.new_papka(text):
                    self.b.show()
            else:
                if not self.right.new_papka(text):
                    self.b.show()
        self.update()

    def txt(self):
        text, ok = QInputDialog.getText(self, 'Введите название',
                                            '', QLineEdit.Normal, '')
        if ok:
            if self.active:
                if not self.left.new_txt(text):
                    self.b.show()
            else:
                if not self.right.new_txt(text):
                    self.b.show()
        self.update()

    def new_name(self):
        if self.name != '':
            text, ok = QInputDialog.getText(self, 'Введите новое название',
                                            '', QLineEdit.Normal, '')
            if ok:
                if self.active:
                    if not self.left.rename(self.name, text):
                        self.b.show()
                else:
                    if not self.right.rename(self.name, text):
                        self.b.show()
        self.update()
    
    def delete(self):
        if self.name != '':
            if self.active:
                if not self.left.remove(self.name):
                    self.b.show()
            else:
                if not self.right.remove(self.name):
                    self.b.show()
        self.update()
    def opened(self):
        if self.name != '':
            if self.active:
                if not self.left.open(self.name):
                    self.b.show()
            else:
                if not self.right.open(self.name):
                    self.b.show()
        self.update()
    
    def get_item_l(self):
        index = self.sender().selectedItems()[0].row()
        self.name = self.all_names_l[index]
        self.active = True
    
    def get_item_r(self):
        index = self.sender().selectedItems()[0].row()
        self.name = self.all_names_r[index]
        self.active = False
    
    def nazad_r(self):
        self.right.nazad()
        self.update()
        

app = QApplication(sys.argv)
a = Main()
a.show()
sys.exit(app.exec_())
