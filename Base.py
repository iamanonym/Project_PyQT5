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


LOGINS = {x.split()[0]: x.split()[1]
          for x in open('Accounts/Accounts_list.txt').readlines()}

LETTERS = \
    {'а': simpleaudio.WaveObject.from_wave_file('Letters/А.wav'),
     'б': simpleaudio.WaveObject.from_wave_file('Letters/Б.wav'),
     'в': simpleaudio.WaveObject.from_wave_file('Letters/В.wav'),
     'г': simpleaudio.WaveObject.from_wave_file('Letters/Г.wav'),
     'д': simpleaudio.WaveObject.from_wave_file('Letters/Д.wav'),
     'е': simpleaudio.WaveObject.from_wave_file('Letters/Е.wav'),
     'ё': simpleaudio.WaveObject.from_wave_file('Letters/Ё.wav'),
     'ж': simpleaudio.WaveObject.from_wave_file('Letters/Ж.wav'),
     'з': simpleaudio.WaveObject.from_wave_file('Letters/З.wav'),
     'и': simpleaudio.WaveObject.from_wave_file('Letters/И.wav'),
     'й': simpleaudio.WaveObject.from_wave_file('Letters/Й.wav'),
     'к': simpleaudio.WaveObject.from_wave_file('Letters/К.wav'),
     'л': simpleaudio.WaveObject.from_wave_file('Letters/Л.wav'),
     'м': simpleaudio.WaveObject.from_wave_file('Letters/М.wav'),
     'н': simpleaudio.WaveObject.from_wave_file('Letters/Н.wav'),
     'о': simpleaudio.WaveObject.from_wave_file('Letters/О.wav'),
     'п': simpleaudio.WaveObject.from_wave_file('Letters/П.wav'),
     'р': simpleaudio.WaveObject.from_wave_file('Letters/Р.wav'),
     'с': simpleaudio.WaveObject.from_wave_file('Letters/С.wav'),
     'т': simpleaudio.WaveObject.from_wave_file('Letters/Т.wav'),
     'у': simpleaudio.WaveObject.from_wave_file('Letters/У.wav'),
     'ф': simpleaudio.WaveObject.from_wave_file('Letters/Ф.wav'),
     'х': simpleaudio.WaveObject.from_wave_file('Letters/Х.wav'),
     'ц': simpleaudio.WaveObject.from_wave_file('Letters/Ц.wav'),
     'ч': simpleaudio.WaveObject.from_wave_file('Letters/Ч.wav'),
     'ш': simpleaudio.WaveObject.from_wave_file('Letters/Ш.wav'),
     'щ': simpleaudio.WaveObject.from_wave_file('Letters/Щ.wav'),
     'ъ': simpleaudio.WaveObject.from_wave_file('Letters/Ъ.wav'),
     'ы': simpleaudio.WaveObject.from_wave_file('Letters/Ы.wav'),
     'ь': simpleaudio.WaveObject.from_wave_file('Letters/Ь.wav'),
     'э': simpleaudio.WaveObject.from_wave_file('Letters/Э.wav'),
     'ю': simpleaudio.WaveObject.from_wave_file('Letters/Ю.wav'),
     'я': simpleaudio.WaveObject.from_wave_file('Letters/Я.wav')}

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
        elif len(self.log) < 8 or len(self.word) < 8:
            return 'Недостаточно символов'
        elif self.word.isdigit() or self.word.isalpha():
            return 'Пароль состоит из символов одного вида'
        elif set(self.word).intersection({',', '.', '!', '?', '/', '\\',
                                          ';', '(', ')', '&', '[', ']'}):
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
            if self.is_new:
                with open('Accounts/Accounts_list.txt', 'a') as file:
                    file.write('{} {}\n'.format(self.log, self.word))
                    file.close()
                os.mkdir('{}/Accounts/{}'.format(os.getcwd(), self.log))
                self.is_new = False
            self.result()

    def result(self):
        self.app = QApplication(sys.argv)
        self.bw = BaseWindow()
        self.bw.show()
        self.app.exec_()
        self.close()


class BaseWindow(QMainWindow):
    def __init__(self):
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
                self.standart = Standart(self.data)
                self.standart.show()
                self.app_stand.exec_()
                self.close()
        elif self.mode == 'Режим слепой печати':
            self.app_sound = QApplication(sys.argv)
            self.sound = Dictation(self.sound_text)
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
    def __init__(self, text):
        super().__init__()
        uic.loadUi('Standart_design.ui', self)
        self.text = text
        self.field1.setText(self.text)
        self.begin = None
        self.end = None
        self.user_text = ''
        self.counter = 0
        self.mistakes = 0

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
        self.res = Result(self.speed, self.mis_perc)
        self.res.show()
        self.res_app.exec_()
        self.close()


class Dictation(QMainWindow):
    def __init__(self, text):
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
        self.res = Result(self.speed, self.mis_perc)
        self.res.show()
        self.res_app.exec_()
        self.close()


class Result(QMainWindow):
    def __init__(self, speed, mistake):
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
        try:
            with open('Results/achievements.txt') as file:
                self.temp = file.read().strip()
                if not self.temp:
                    self.number1 = 0
                else:
                    self.temp = self.temp.split('\n')
                    self.number1 = int(self.temp[-1].split()[0]) + 1
                    self.x_es1 = list(map(lambda x: int(x.split()[0]),
                                          self.temp)) + [self.number1]
                    self.y_es1 = list(map(lambda y: float(y.split()[1]),
                                          self.temp)) + [self.speed]
                self.file_n = open('Results/achievements.txt', 'a')
                self.file_n.write('{} {}\n'.format(self.number1,
                                                   self.speed))
                self.file_n.close()
            with open('Results/mistakes.txt') as file2:
                self.temp2 = file2.read()
                if not self.temp2:
                    self.number2 = 0
                else:
                    self.temp2 = self.temp2.strip().split('\n')
                    self.number2 = int(self.temp2[-1].split()[0]) + 1
                    self.x_es2 = list(map(lambda x: int(x.split()[0]),
                                          self.temp2)) + [self.number2]
                    self.y_es2 = list(map(lambda y: float(y.split()[1]),
                                          self.temp2)) + [self.mistake]
                self.file_n2 = open('Results/mistakes.txt', 'a')
                self.file_n2.write('{} {}\n'.format(self.number2,
                                                    self.mistake))
                self.file_n2.close()
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