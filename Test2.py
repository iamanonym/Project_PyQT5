import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M
import sys

app = C.QCoreApplication(sys.argv)

url = C.QUrl.fromLocalFile("A.wma")
content = M.QMediaContent(url)
player = M.QMediaPlayer()
player.setMedia(content)
player.play()

player.stateChanged.connect(app.quit)
app.exec_()
