# -*- coding: utf-8 -*-
# Version 1.31
import os # Импортирует всё, что надо
import win32api
import shutil


class FileSystem: # Класс файловой системы
    def __init__(self, base_path):
        # Список всех системных дисков
        self.discs = win32api.GetLogicalDriveStrings().split("\x00")[:-1]
        self.path = base_path # Текущий путь в системе
        self.base = False # Метка нахождения в списке дисков(Под дисками)

    def vpered(self, name): # Перемещение вперед по дереву системы
        if self.base: # Если мы под дисками
            self.path = name # Путь - имя диска
            self.base = False # Мы больше не в корне
            return True
        elif self.path in self.discs: # Если мы в корне диска
            self.path = self.path + name # добавляем имя без слеша, тк их
            # уже много в названии диска
        else: # Иначе мы добавляем имя со слешем
            self.path = self.path + '\\'[0] + name

    def nazad(self): # Перемещение назад по дереву каталога
        if self.base: # Если мы в списке дисков, назад не уйти
            return True
        if self.path in self.discs or self.path[:3] not in self.discs:
            # Если мы в корне диска или диск не существует(полезно при запуске,
            # если диска С или Д нет), переходим назад
            self.path = '' 
            self.base = True # Мы под дисками
            return True
        else:
            self.path = os.path.split(self.path)[0] # Уходим на 1 слеш назад

    def open_cmd(self): # Открытие командной строки
        os.chdir(self.path) # Система устанавливает путь
        os.system('cmd') # cmd открывается в установленном выше пути

    def remove(self, name): # Удаление
        try: # Если можем
            if os.path.isfile(self.path + '\\'[0] + name): # Если это файл
                os.remove(self.path + '\\'[0] + name) # Удаляем файл по пути
            else: # Если это директория
                shutil.rmtree(self.path + '\\'[0] + name) # Удаляем дерево
                # Директорий
            return True
        except Exception:
            return False

    def vse(self): # Показать все файлы и папки в директории
        try: 
            if self.base: # Если мы под дисками
                return self.preobr(self.discs) # Преобразуем список дисков
            spisok = os.listdir(self.path) # Берём список всего в директории
            return self.preobr(spisok) # Преобразуем этот список
        except Exception:
            return 'Vse Ploxo'

    def fix_len(self, spisok, real): # Выравнивание имени и типа по длине
        abc = spisok[0]
        ef = spisok[1] 
        if len(abc) > 40: # Если имя больше 40, обрезаем
            abc = abc[:38] + '...'
        else: # иначе дополним пробелами
            abc = abc + '  ' * (40 - len(abc))
        if len(ef) > 13: # Если тип длиннее 13, обрезаем
            ef = ef[:11] + '...'
        else: # иначе дополним
            ef = ef + '  ' * (13 - len(ef))
        return [abc, ef, real] # Возвращаем выравненные имя и тип +
    # Изначальное неподеленное название

    def preobr(self, sp): # Преобразование списка файлов/папок
        spisok2 = []
        for i in sp: # Добавляем в особый список элементы с преобразованием
            # Все имена подгоняем под одну длину
            if i in self.discs: # Если это диск, добавляем его и скобки
                spisok2.append(self.fix_len([i, '<>'], i))
                continue
            # Скрываем некоторые скрытые лишние системные фалы и директории
            if '.bin' in i.lower() or '.sys' in i.lower():
                continue
            if '.dat' in i.lower() or i == '':
                continue
            if self.path == 'C:\\' and i == 'Documents and Settings':
                continue
            # Отделяем тип файла от остального имени
            if os.path.isfile(self.path + '\\'[0] + i):
                if i.count('.') == 1:
                    spisok2.append(self.fix_len(i.split('.'), i))
                elif i.count('.') == 0:
                    spisok2.append(self.fix_len([i, '-'], i))
                else:
                    i2 = i.split('.')
                    spisok2.append(self.fix_len(
                        ['.'.join(i2[:-1]), i2[-1]], i))
            else:
                # Если директория, добавляем <dir>
                spisok2.append(self.fix_len([i, '<dir>'], i))
        return spisok2

    def new_papka(self, name): # Создание директории
        try: # Если можем, создаем по имени в текущем месте
            os.mkdir(self.path + '\\'[0] + name)
            return True
        except Exception:
            return False

    def new_txt(self, name): # Создание файла, не только txt
        try: # Если можем, откроем файл в текущем месте с созданием
            with open(self.path + '\\'[0] + name, 'w') as f:
                pass # Ничего с ним не сделаем, он закроется
            return True
        except Exception:
            return False

    def rename(self, name, new_name): #
        try: #
            os.rename(self.path + '\\'[0] + name,
                      self.path + '\\'[0] + new_name)
            return True
        except Exception:
            return False

    def move(self, name, new_dir): #
        if self.copy(name, new_dir): #
            if self.remove(name): #
                return True
        return False

    def copy(self, name, new_dir): # Копирование
        if os.path.isfile(self.path + '\\'[0] + name): # Если это файл
            try: # Если можем, копируем файл в новое место с тем же названием
                shutil.copy2(
                    self.path + '\\'[0] + name, new_dir + '\\'[0] + name)
                return True
            except Exception:
                return False
        else:
            try: # Копируем дерево директории
                shutil.copytree(
                    self.path + '\\'[0] + name, new_dir + '\\'[0] + name)
                return True
            except Exception:
        # Если папка копирования уже была, мы рекурсивно копируем всё внутри
                self.vpered(name)
                new_dir = new_dir + '\\'[0] + name
                for i in self.vse():
                    self.copy(i[2], new_dir)
                self.nazad()
                return True

    def open(self, name): # Открытие файлов и директорий
        try:
            if os.path.isfile(self.path + '\\'[0] + name): # Если это файл
                # Открываем его как файл программой по умолчанию
                os.startfile(self.path + '\\'[0] + name)
                return True
            else:
            # у нас папка, значит просто идём вперед по дереву в папку
            # Если вдруг в неё идти нельзя, сработает защита в классе Main
            # оно попробует выполнить vse(), получит False и вернется назад
            # по дереву
                self.vpered(name)
                return True
        except Exception:
            return False
