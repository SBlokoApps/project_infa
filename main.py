# -*- coding: utf-8 -*-
# Version 1.31
from file import *
from PyQt5.QtWidgets import QMainWindow, QDialog, QLineEdit, QAbstractItemView
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QInputDialog
from PyQt5.QtCore import QSize, Qt
import sys
from file_system import * # Импорт окна программы из QtDesigner
from Error47 import * # Импорт окна ошибки из QtDesigner


class MyDialog(QDialog, Ui_Dialog): # Класс окна ошибки
    def __init__(self):
        super().__init__()
        super().setupUi(self)


class Main(QMainWindow, Ui_MainWindow): # Класс окна программы
    def __init__(self):
        super().__init__()
        super().setupUi(self) # Наследуем элементы интерфейса
        self.active = True # Переключатель активного окна левое/правое
        self.name = '' # Имя выделенного файла
        self.all_names_l = [] # Имена всех файлов/папок в левом окне
        self.all_names_r = [] # Аналогично в правом
        self.error47 = MyDialog() # Инициализируем и настраиваем окно ошибки
        self.error47.label_2.setText('Так получилось')
        self.dialog_ok = MyDialog() # Инициализируем и настраиваем окно готово
        self.dialog_ok.label_2.setText('Завершена')
        self.dialog_ok.label.setText('Задача')
        self.left = FileSystem('C:\\') # Инициализация левого окна файловой
        # системы
        self.right = FileSystem('D:\\') # Аналогично для правого
        # Если таких дисков нет, программа вылетит в список дисков
        # Следующие строки - настройка Таблиц для показа файловой системы
        self.left_table.setColumnCount(2) # Число столбцов для левой таблицы
        self.right_table.setColumnCount(2) # Аналогично для правого
        self.left_table.setHorizontalHeaderLabels(['Имя', 'Тип']) # Названия
        # Столбцовв
        self.right_table.setHorizontalHeaderLabels(['Имя', 'Тип'])
        self.left_table.setSortingEnabled(False) # Выключаем
        # сортировку столбцов по алфавиту
        self.right_table.setSortingEnabled(False) # Аналогично для правого
        # Настройки выделения таблиц
        self.left_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.right_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.left_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.right_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.update()
        self.left_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.right_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Подключение кнопок и таблиц к методам нажатий
        self.n_left.clicked.connect(self.nazad_l)
        self.n_right.clicked.connect(self.nazad_r)
        self.copy.clicked.connect(self.copied)
        self.dele.clicked.connect(self.deleted)
        self.open.clicked.connect(self.new_name)
        self.new_dir.clicked.connect(self.dir)
        self.new_file.clicked.connect(self.txt)
        self.left_table.itemPressed.connect(self.get_item_l)
        self.right_table.itemPressed.connect(self.get_item_r)
        self.move.clicked.connect(self.moved)
        self.left_table.itemDoubleClicked.connect(self.opened)
        self.right_table.itemDoubleClicked.connect(self.opened)
        self.cmd.clicked.connect(self.open_cmd)

    def update(self): # Обновление таблиц файловой системы
        self.name = '' # Обнуляем выделение
        l_fs = self.left.vse() # Получаем список файлов в директории слева
        r_fs = self.right.vse() # Аналогичто справа
        if l_fs == 'Vse Ploxo': # Если ошибка при показе слева
            self.nazad_l() # Выходим назад из директории
            self.error47.show() # Показыаем ошибку
            return
        if r_fs == 'Vse Ploxo': # Аналогично справа
            self.nazad_r()
            self.error47.show()
            return
        self.all_names_l = [i[2] for i in l_fs] # Заполняем список всех имён
        self.all_names_r = [i[2] for i in r_fs]
        len_left = len(l_fs)
        len_right = len(r_fs)
        self.left_table.setRowCount(len_left) # Ставим количество строк
        self.right_table.setRowCount(len_right)
        # Заполняем таблицу
        for i in range(len_left):
            self.left_table.setItem(i, 0, QTableWidgetItem(l_fs[i][0]))
            self.left_table.setItem(i, 1, QTableWidgetItem(l_fs[i][1]))
        for i in range(len_right):
            self.right_table.setItem(i, 0, QTableWidgetItem(r_fs[i][0]))
            self.right_table.setItem(i, 1, QTableWidgetItem(r_fs[i][1]))
        self.left_table.resizeColumnsToContents()
        self.right_table.resizeColumnsToContents()

    def nazad_l(self): # Перемещение назад слева
        self.left.nazad() # Вызываем метод из FileSystem для  левой системы
        self.update() # После каждого метода надо обновлять таблицу

    def nazad_r(self): # Справа переходим назад, аналогично слева
        self.right.nazad()
        self.update()

    def copied(self): # Копирование файла/директории
        if self.name != '': # Если выделен файл или директория
            if self.active: # Если активно левое окно
                if not self.left.copy(self.name, self.right.path): # Вызываем
                    # метод из FileSystem, если копирование неудачно
                    self.error47.show() # Показываем окно ошибки
                else:
                    self.dialog_ok.show() # Инаде вызываем окно ОК
            else: # Аналогично, если левое окно неактивно
                if not self.right.copy(self.name, self.left.path):
                    self.error47.show()
                else:
                    self.dialog_ok.show()
        self.update()

    def moved(self): # Перемещение файлов/директории
        # Написано аналогично копированию
        if self.name != '':
            if self.active:
                if not self.left.move(self.name, self.right.path):
                    self.error47.show()
                else:
                    self.dialog_ok.show()
            else:
                if not self.right.move(self.name, self.left.path):
                    self.error47.show()
                else:
                    self.dialog_ok.show()
        self.update()

    def open_cmd(self): # Открытие командной строки
        if self.active: # Если активно слева
            self.left.open_cmd() # Левая система открывает командную строку
        else:
            self.right.open_cmd() # Иначе открывает правая

    def dir(self): #
        text, ok = QInputDialog.getText(
            self, 'Введите название', '', QLineEdit.Normal, '')
        # Создаем окно с вводом, если нажато ок
        if ok:
            if self.active: # Если слева активно
                if not self.left.new_papka(text): # Левая система создает папку
                    self.error47.show() # Вылезает окно ошибки
            else: # Если слева неактивно
                if not self.right.new_papka(text):
                    self.error47.show()
        self.update()

    def txt(self): # Создание файла
        # Аналогично созданию директории
        text, ok = QInputDialog.getText(
            self, 'Введите название', '', QLineEdit.Normal, '')
        if ok:
            if self.active:
                if not self.left.new_txt(text):
                    self.error47.show()
            else:
                if not self.right.new_txt(text):
                    self.error47.show()
        self.update()

    def new_name(self): # Переименование
        if self.name != '': # Если есть выделенный файл
            # Создаем окно с вводом
            text, ok = QInputDialog.getText(self, 'Введите новое название',
                                            '', QLineEdit.Normal, '')
            if ok: # Если нажато ок, аналогичный вызов метода 
                if self.active:
                    if not self.left.rename(self.name, text):
                        self.error47.show()
                else:
                    if not self.right.rename(self.name, text):
                        self.error47.show()
        self.update()

    def deleted(self): # Удаление файлов/директорий
        if self.name != '': # Аналогично тому, что было выше
            if self.active:
                if not self.left.remove(self.name):
                    self.error47.show()
            else:
                if not self.right.remove(self.name):
                    self.error47.show()
        self.update()

    def opened(self): # Открытие директорий/файлов
        if self.name != '': #  Аналогично удалению
            if self.active:
                if not self.left.open(self.name):
                    self.error47.show()
            else:
                if not self.right.open(self.name):
                    self.error47.show()
        self.update()

    def get_item_l(self): # Получаем имя выделенного файла слева
        index = self.sender().selectedItems()[0].row() # Индекс выделенного
        # элемента таблицы
        self.name = self.all_names_l[index] # Имя по индексу
        self.active = True # Левое окно активно

    def get_item_r(self): # Получаем имя выделенного файла справа, аналогично
        # получению имени слева
        index = self.sender().selectedItems()[0].row()
        self.name = self.all_names_r[index]
        self.active = False


app = QApplication(sys.argv)
wwindoww = Main()
wwindoww.show()
sys.exit(app.exec_())
