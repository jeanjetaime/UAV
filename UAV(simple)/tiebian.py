import sys,random
from PyQt5.QtGui import QPalette,QColor
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,\
 QDesktopWidget,QApplication
from PyQt5.QtCore import Qt,QRect,QEvent,QPoint
from PyQt5.Qt import QCursor,QPropertyAnimation

SCREEN_WEIGHT = 1920
SCREEN_HEIGHT = 1080
WINDOW_WEIGHT = 300
WINDOW_HEIGHT = 600
class Ui_Form(QWidget):
    def __init__(self):
        self.moved = False
        super(Ui_Form,self).__init__()
        self.setupUi()
        self.resize(WINDOW_WEIGHT, WINDOW_HEIGHT)
        self.show()
    def setupUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint
                            | Qt.WindowStaysOnTopHint
                            | Qt.Tool) # 去掉标题栏
        self.widget = QWidget()
        self.Layout = QVBoxLayout(self.widget)
        self.Layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.Layout)
        self.setWindowFlag(Qt.Tool)
        self.main_widget = QWidget()
        self.Layout.addWidget(self.main_widget)
        self.paint = QPushButton(self.main_widget)
        self.paint.setText("切换")
        self.paint.move(QPoint(120,200))
        self.paint.clicked.connect(self.Painting)
        self.exit = QPushButton(self.main_widget)
        self.exit.setText(" 退出 ")
        self.exit.move(QPoint(120,400))
        self.exit.clicked.connect(lambda:exit(0))
        self.setStyleSheet('''
              QPushButton {
              color: rgb(137, 221, 255);
              background-color: rgb(37, 121, 255);
              border-style:none;
              border:1px solid #3f3f3f;
              padding:5px;
              min-height:20px;
              border-radius:15px;
              }
              ''')
    def Painting(self):
        color = random.choice(["CCFFFF","CC6699","CC99FF","99CCFF"])
        palette1 = QPalette()
        palette1.setColor(self.backgroundRole(),QColor("#{}".format(color))) # 改变窗体颜色
        self.setPalette(palette1)
    def enterEvent(self, event):
        self.hide_or_show('show', event)
    def leaveEvent(self, event):
        self.hide_or_show('hide', event)
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
        QApplication.postEvent(self, QEvent(174))
        event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            try:
                self.move(event.globalPos() - self.dragPosition)
                event.accept()
            except:pass
    def mouseReleaseEvent(self, event):
        self.moved = True
        self.hide_or_show('show', event)
    def hide_or_show(self, mode, event):
        pos = self.frameGeometry().topLeft()
        if mode == 'show' and self.moved:
            if pos.x() + WINDOW_WEIGHT >= SCREEN_WEIGHT: # 右侧显示
                self.startAnimation(SCREEN_WEIGHT - WINDOW_WEIGHT + 2, pos.y())
                event.accept()
                self.moved = False
            elif pos.x() <= 0: # 左侧显示
                self.startAnimation(0,pos.y())
                event.accept()
                self.moved = False
            elif pos.y() <= 0: # 顶层显示
                self.startAnimation(pos.x(),0)
                event.accept()
                self.moved = False
        elif mode == 'hide':
            if pos.x() + WINDOW_WEIGHT >= SCREEN_WEIGHT: # 右侧隐藏
                self.startAnimation(SCREEN_WEIGHT - 2,pos.y())
                event.accept()
                self.moved = True
            elif pos.x() <= 2: # 左侧隐藏
                self.startAnimation(2 - WINDOW_WEIGHT,pos.y())
                event.accept()
                self.moved = True
            elif pos.y() <= 2: # 顶层隐藏
                self.startAnimation(pos.x(),2 - WINDOW_HEIGHT)
                event.accept()
                self.moved = True
    def startAnimation(self,width,height):
        animation = QPropertyAnimation(self,b"geometry",self)
        startpos = self.geometry()
        animation.setDuration(200)
        newpos = QRect(width,height,startpos.width(),startpos.height())
        animation.setEndValue(newpos)
        animation.start()
if __name__ == "__main__":
 app = QApplication(sys.argv)
 ui = Ui_Form()
 sys.exit(app.exec_())