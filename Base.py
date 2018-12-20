import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QFileDialog
from PyQt5 import uic
import PyQt5.QtCore as Core
import simpleaudio
import os
from datetime import datetime
import time


def count_speed(letters, time1, time2):
    diff = time2 - time1
    sec_diff = diff.seconds / 60
    return letters // sec_diff


def count_mistakes(mistakes, letters):
    return round(mistakes / letters, 3)


def get_info_from_file(file_name, ex):
    x_es = [0]
    y_es = [ex]
    with open(file_name) as file:
        temp = file.read().strip()
        if not temp:
            number = 0
        else:
            temp = temp.split('\n')
            number = int(temp[-1].split()[0]) + 1
            x_es = list(map(lambda x: int(x.split()[0]), temp)) + [number]
            y_es = list(map(lambda y: float(y.split()[1]), temp)) + [ex]
        file.close()
    file_n = open(file_name, 'a')
    file_n.write('{} {}\n'.format(number, ex))
    file_n.close()
    return x_es, y_es


LOGINS = {x.split()[0]: x.split()[1]
          for x in open('Accounts/Accounts_list.txt').readlines()}

LETTERS = \
    {'а': simpleaudio.WaveObject.from_wave_file('Keys/А.wav'),
     'б': simpleaudio.WaveObject.from_wave_file('Keys/Б.wav'),
     'в': simpleaudio.WaveObject.from_wave_file('Keys/В.wav'),
     'г': simpleaudio.WaveObject.from_wave_file('Keys/Г.wav'),
     'д': simpleaudio.WaveObject.from_wave_file('Keys/Д.wav'),
     'е': simpleaudio.WaveObject.from_wave_file('Keys/Е.wav'),
     'ё': simpleaudio.WaveObject.from_wave_file('Keys/Ё.wav'),
     'ж': simpleaudio.WaveObject.from_wave_file('Keys/Ж.wav'),
     'з': simpleaudio.WaveObject.from_wave_file('Keys/З.wav'),
     'и': simpleaudio.WaveObject.from_wave_file('Keys/И.wav'),
     'й': simpleaudio.WaveObject.from_wave_file('Keys/Й.wav'),
     'к': simpleaudio.WaveObject.from_wave_file('Keys/К.wav'),
     'л': simpleaudio.WaveObject.from_wave_file('Keys/Л.wav'),
     'м': simpleaudio.WaveObject.from_wave_file('Keys/М.wav'),
     'н': simpleaudio.WaveObject.from_wave_file('Keys/Н.wav'),
     'о': simpleaudio.WaveObject.from_wave_file('Keys/О.wav'),
     'п': simpleaudio.WaveObject.from_wave_file('Keys/П.wav'),
     'р': simpleaudio.WaveObject.from_wave_file('Keys/Р.wav'),
     'с': simpleaudio.WaveObject.from_wave_file('Keys/С.wav'),
     'т': simpleaudio.WaveObject.from_wave_file('Keys/Т.wav'),
     'у': simpleaudio.WaveObject.from_wave_file('Keys/У.wav'),
     'ф': simpleaudio.WaveObject.from_wave_file('Keys/Ф.wav'),
     'х': simpleaudio.WaveObject.from_wave_file('Keys/Х.wav'),
     'ц': simpleaudio.WaveObject.from_wave_file('Keys/Ц.wav'),
     'ч': simpleaudio.WaveObject.from_wave_file('Keys/Ч.wav'),
     'ш': simpleaudio.WaveObject.from_wave_file('Keys/Ш.wav'),
     'щ': simpleaudio.WaveObject.from_wave_file('Keys/Щ.wav'),
     'ъ': simpleaudio.WaveObject.from_wave_file('Keys/Ъ.wav'),
     'ы': simpleaudio.WaveObject.from_wave_file('Keys/Ы.wav'),
     'ь': simpleaudio.WaveObject.from_wave_file('Keys/Ь.wav'),
     'э': simpleaudio.WaveObject.from_wave_file('Keys/Э.wav'),
     'ю': simpleaudio.WaveObject.from_wave_file('Keys/Ю.wav'),
     'я': simpleaudio.WaveObject.from_wave_file('Keys/Я.wav'),
     'a': simpleaudio.WaveObject.from_wave_file('Keys/A.wav'),
     'b': simpleaudio.WaveObject.from_wave_file('Keys/B.wav'),
     'c': simpleaudio.WaveObject.from_wave_file('Keys/C.wav'),
     'd': simpleaudio.WaveObject.from_wave_file('Keys/D.wav'),
     'e': simpleaudio.WaveObject.from_wave_file('Keys/E.wav'),
     'f': simpleaudio.WaveObject.from_wave_file('Keys/F.wav'),
     'g': simpleaudio.WaveObject.from_wave_file('Keys/G.wav'),
     'h': simpleaudio.WaveObject.from_wave_file('Keys/H.wav'),
     'i': simpleaudio.WaveObject.from_wave_file('Keys/I.wav'),
     'j': simpleaudio.WaveObject.from_wave_file('Keys/J.wav'),
     'k': simpleaudio.WaveObject.from_wave_file('Keys/K.wav'),
     'l': simpleaudio.WaveObject.from_wave_file('Keys/L.wav'),
     'm': simpleaudio.WaveObject.from_wave_file('Keys/M.wav'),
     'n': simpleaudio.WaveObject.from_wave_file('Keys/N.wav'),
     'o': simpleaudio.WaveObject.from_wave_file('Keys/O.wav'),
     'p': simpleaudio.WaveObject.from_wave_file('Keys/P.wav'),
     'q': simpleaudio.WaveObject.from_wave_file('Keys/Q.wav'),
     'r': simpleaudio.WaveObject.from_wave_file('Keys/R.wav'),
     's': simpleaudio.WaveObject.from_wave_file('Keys/S.wav'),
     't': simpleaudio.WaveObject.from_wave_file('Keys/T.wav'),
     'u': simpleaudio.WaveObject.from_wave_file('Keys/U.wav'),
     'v': simpleaudio.WaveObject.from_wave_file('Keys/V.wav'),
     'w': simpleaudio.WaveObject.from_wave_file('Keys/W.wav'),
     'x': simpleaudio.WaveObject.from_wave_file('Keys/X.wav'),
     'y': simpleaudio.WaveObject.from_wave_file('Keys/Y.wav'),
     'z': simpleaudio.WaveObject.from_wave_file('Keys/Z.wav'),
     '0': simpleaudio.WaveObject.from_wave_file('Keys/0.wav'),
     '1': simpleaudio.WaveObject.from_wave_file('Keys/1.wav'),
     '2': simpleaudio.WaveObject.from_wave_file('Keys/2.wav'),
     '3': simpleaudio.WaveObject.from_wave_file('Keys/3.wav'),
     '4': simpleaudio.WaveObject.from_wave_file('Keys/4.wav'),
     '5': simpleaudio.WaveObject.from_wave_file('Keys/5.wav'),
     '6': simpleaudio.WaveObject.from_wave_file('Keys/6.wav'),
     '7': simpleaudio.WaveObject.from_wave_file('Keys/7.wav'),
     '8': simpleaudio.WaveObject.from_wave_file('Keys/8.wav'),
     '9': simpleaudio.WaveObject.from_wave_file('Keys/9.wav'),}

TEXTS = {10: 'Texts/10.txt', 20: 'Texts/20.txt', 30: 'Texts/30.txt',
         40: 'Texts/40.txt', 50: 'Texts/50.txt', 60: 'Texts/60.txt',
         70: 'Texts/70.txt', 80: 'Texts/80.txt', 90: 'Texts/90.txt'}

SOUND_WORDS = \
    {'сортировка': simpleaudio.WaveObject.from_wave_file('Sound/w0.wav'),
     'библиотека': simpleaudio.WaveObject.from_wave_file('Sound/w1.wav'),
     'директория': simpleaudio.WaveObject.from_wave_file('Sound/w2.wav'),
     'трассировка': simpleaudio.WaveObject.from_wave_file('Sound/w3.wav'),
     'архивирование': simpleaudio.WaveObject.from_wave_file('Sound/w4.wav'),
     'репозиторий': simpleaudio.WaveObject.from_wave_file('Sound/w5.wav'),
     'инвертор': simpleaudio.WaveObject.from_wave_file('Sound/w6.wav')}

SOUND_COLLOCATIONS = \
    {'командная строка':
     simpleaudio.WaveObject.from_wave_file('Sound/c0.wav'),
     'программное обеспечение':
     simpleaudio.WaveObject.from_wave_file('Sound/c1.wav'),
     'операционная система':
     simpleaudio.WaveObject.from_wave_file('Sound/c2.wav'),
     'система счисления':
     simpleaudio.WaveObject.from_wave_file('Sound/c3.wav'),
     'закон склеивания':
     simpleaudio.WaveObject.from_wave_file('Sound/c4.wav'),
     'графический интерфейс':
     simpleaudio.WaveObject.from_wave_file('Sound/c5.wav')}


class PasswordWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Password_design.ui', self)
        self.sign_in.clicked.connect(self.signing)
        self.sign_up.clicked.connect(self.signing)
        self.is_new = False

    def check(self, mode='s'):
        self.log = self.login.text()
        self.word = self.password.text()
        if mode == 'e' and self.log not in LOGINS:
            return 'Несуществующий логин'
        elif mode == 'e' and LOGINS[self.log] != self.word:
            return 'Неверный пароль'
        elif mode == 's' and self.log in LOGINS:
            return 'Логин уже существует'
        elif len(self.log) < 8 or len(self.word) < 8:
            return 'Недостаточно символов'
        elif self.word.isdigit() or self.word.isalpha():
            return 'Пароль состоит из символов одного вида'
        elif set(self.log).intersection({',', '.', '!', '?', '/', '\\',
                                         ';', '(', ')', '&', '[', ']',
                                         '<', '>', '*', '|', ':', '"'}):
            return 'Недопустимые символы в логине'
        elif set(self.word).intersection({',', '.', '!', '?', '/', '\\',
                                          ';', '(', ')', '&', '[', ']',
                                          '<', '>', '*', '|', ':', '"'}):
            return 'Недопустимые символы в пароле'

    def signing(self):
        if self.sender().text() == 'Вход':
            self.checking = self.check(mode='e')
        else:
            self.checking = self.check()
            self.is_new = True
        if self.checking:
            self.comment.setText(self.checking)
            self.comment.adjustSize()
        else:
            self.name = 'Accounts/{}'.format(self.log)
            if self.is_new:
                with open('Accounts/Accounts_list.txt', 'a') as file:
                    file.write('{} {}\n'.format(self.log, self.word))
                    file.close()
                self.file1 = open(self.name + '_ach.txt', 'w')
                self.file1.close()
                self.file2 = open(self.name + '_mist.txt', 'w')
                self.file2.close()
                self.is_new = False
            self.result()

    def result(self):
        self.app = QApplication(sys.argv)
        self.bw = BaseWindow(self.name)
        self.bw.show()
        self.app.exec_()
        self.close()


class BaseWindow(QMainWindow):
    def __init__(self, name):
        super().__init__()
        uic.loadUi('Base_design.ui', self)
        self.mode = None
        self.ed.toggled.connect(self.set_mode)
        self.stand.toggled.connect(self.set_mode)
        self.unseen.toggled.connect(self.set_mode)
        self.choose.clicked.connect(self.choosing)
        self.begin.clicked.connect(self.start)
        self.typing.currentIndexChanged.connect(self.change_type)
        self.name = None
        self.data = None
        self.file_name = name
        self.sound_text = SOUND_WORDS

    def change_type(self, index):
        self.sound_text = SOUND_WORDS if not index else SOUND_COLLOCATIONS

    def set_mode(self):
        self.mode = self.sender().text()

    def choosing(self):
        self.filter = 'Texts (*.txt)'
        self.name, _ = QFileDialog.getOpenFileName(self, 'Открыть файл',
                                                   os.getcwd(), self.filter)
        if not self.name:
            return None
        with open(self.name) as file:
            self.data = ' '.join(file.read().split('\n'))
            if not self.data:
                self.greet_4.setText('Файл пуст. Выберите другой')
            else:
                self.greet_4.setText('Файл выбран')
            if len(self.data) > 800:
                self.data = self.data[:800]
            file.close()

    def start(self):
        if not self.mode:
            return None
        elif self.mode == 'Стандартный':
            if not self.data:
                self.words = self.counter.value()
                if not self.words % 10 and self.words > 10:
                    self.words = (self.words // 10) * 10
                elif self.words > 10:
                    self.words = 10
                with open(TEXTS[self.words]) as file:
                    self.data = file.read().strip()
                    file.close()
                self.app_stand = QApplication(sys.argv)
                self.standart = Standart(self.data, self.file_name)
                self.standart.show()
                self.app_stand.exec_()
                self.close()
        elif self.mode == 'Режим слепой печати':
            self.app_sound = QApplication(sys.argv)
            self.sound = Dictation(self.sound_text, self.file_name)
            self.sound.show()
            self.app_sound.exec_()
            self.close()
        elif self.mode == 'Обучение':
            self.app_ed = QApplication(sys.argv)
            self.edu = Education()
            self.edu.show()
            self.app_ed.exec_()
            self.close()


class Education(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Edu_design.ui', self)
        self.user_text = ''
        self.is_write = True

    def keyPressEvent(self, event):
        try:
            b = LETTERS[event.text().lower()].play()
            b.wait_done()
            if self.is_write:
                self.user_text += event.text()
        except KeyError:
            if event.key() == Core.Qt.Key_Space and self.is_write:
                self.user_text += ' '
        self.field.setText(self.user_text)
        if len(self.user_text) == 800:
            self.is_write = False
            self.comment.setText('Превышен лимит длины поля')
            self.comment.adjustSize()


class Standart(QMainWindow):
    def __init__(self, text, name):
        super().__init__()
        uic.loadUi('Standart_design.ui', self)
        self.text = text
        self.field1.setText(self.text)
        self.begin = None
        self.end = None
        self.user_text = ''
        self.counter = 0
        self.mistakes = 0
        self.file_name = name

    def keyPressEvent(self, event):
        if not self.begin:
            self.begin = datetime.now()
        if event.text() == self.text[self.counter]:
            self.user_text += event.text()
            self.counter += 1
        elif (self.text[self.counter] == ' ' and
              event.key() == Core.Qt.Key_Space):
            self.user_text += ' '
            self.counter += 1
        elif event.key() != Core.Qt.Key_Shift:
            self.mistakes += 1
        self.field2.setText(self.user_text)
        if self.counter == len(self.text):
            self.end = datetime.now()
            time.sleep(0.5)
            self.result()

    def result(self):
        self.speed = count_speed(len(self.text), self.begin, self.end)
        self.mis_perc = count_mistakes(self.mistakes,
                                       len(self.text) + self.mistakes)
        self.res_app = QApplication(sys.argv)
        self.res = Result(self.speed, self.mis_perc, self.file_name)
        self.res.show()
        self.res_app.exec_()
        self.close()


class Dictation(QMainWindow):
    def __init__(self, text, name):
        super().__init__()
        uic.loadUi('Sound_design.ui', self)
        self.text = text
        self.word_counter = 0
        self.word = list(self.text.keys())[self.word_counter]
        self.symbol_counter = 0
        self.begin = None
        self.end = None
        self.mistakes = 0
        self.user_text = ''
        self.file_name = name

    def keyPressEvent(self, event):
        if event.key() == Core.Qt.Key_PageUp:
            if not self.begin:
                self.begin = datetime.now()
                self.playing(self.text[self.word])
            elif len(self.word) == self.symbol_counter:
                self.symbol_counter = 0
                self.word_counter += 1
                self.user_text = ''
                try:
                    self.word = list(self.text.keys())[self.word_counter]
                    self.playing(self.text[self.word])
                except IndexError:
                    self.end = datetime.now()
                    self.result()
            else:
                self.mistakes += 1
                self.playing(self.text[self.word])
        elif event.text() == self.word[self.symbol_counter]:
            self.user_text += event.text()
            self.symbol_counter += 1
        elif (self.word[self.symbol_counter] == ' ' and
              event.key() == Core.Qt.Key_Space):
            self.user_text += ' '
            self.symbol_counter += 1
        elif event.key() != Core.Qt.Key_Shift:
            self.mistakes += 1
        self.field.setText(self.user_text)

    def playing(self, music):
        self.player = music.play()
        self.player.wait_done()

    def result(self):
        self.speed = count_speed(len(' '.join(self.text)),
                                 self.begin, self.end)
        self.mis_perc = count_mistakes(self.mistakes,
                                       len(' '.join(self.text)) +
                                       self.mistakes)
        self.res_app = QApplication(sys.argv)
        self.res = Result(self.speed, self.mis_perc, self.file_name)
        self.res.show()
        self.res_app.exec_()
        self.close()


class Result(QMainWindow):
    def __init__(self, speed, mistake, name):
        super().__init__()
        self.speed, self.mistake = speed, mistake
        self.corr = True
        self.x_es1, self.y_es1, self.x_es2, self.y_es2 = \
            None, None, None, None
        uic.loadUi('Res_design.ui', self)
        self.res_greet2.setText('Скорость печати: {} '
                                'символов в минуту'.format(round(speed)))
        self.res_greet2.adjustSize()
        self.res_greet3.setText('Процент ошибок: '
                                '{}%'.format(round(mistake, 3)))
        self.res_greet3.adjustSize()
        self.file_name = name
        try:
            self.x_es1, self.y_es1 = \
                get_info_from_file(self.file_name + '_ach.txt', self.speed)
            self.x_es2, self.y_es2 = \
                get_info_from_file(self.file_name + '_mist.txt', self.mistake)
        except FileNotFoundError:
            self.corr = False
        except IndexError:
            self.corr = False
        if self.corr:
            self.stat_ach.clicked.connect(self.graph_ach)
            self.stat_mist.clicked.connect(self.graph_mist)

    def graph_ach(self):
        self.graph_app = QApplication(sys.argv)
        if self.x_es1 and self.y_es1:
            self.graph = Graph(self.x_es1, self.y_es1)
        else:
            self.graph = Graph()
        self.graph.show()
        self.graph_app.exec_()

    def graph_mist(self):
        self.graph_app2 = QApplication(sys.argv)
        if self.x_es2 and self.y_es2:
            self.graph2 = Graph(self.x_es2, self.y_es2)
        else:
            self.graph2 = Graph()
        self.graph2.show()
        self.graph_app2.exec_()


class Graph(QMainWindow):
    def __init__(self, x_es=None, y_es=None):
        super().__init__()
        uic.loadUi('Graph_maker_design.ui', self)
        if x_es and y_es:
            self.graph.plot(x_es, y_es, pen='g')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pswd = PasswordWindow()
    pswd.show()
    sys.exit(app.exec_())