import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
import py.display as display, time
from threads import QThread4VideoDisplay

class custom_window(QtWidgets.QMainWindow):
    
    sum = 0
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.init_ui()

    def init_ui(self):
        dis = display.Ui_MainWindow()
        dis.setupUi(self)
        self.total_signal()

    def total_signal(self):
        # 实例化线程类
        self.myThread = QThread4VideoDisplay()

        # 单击按钮, 以单击为发送信号
        switch_btn = self.centralWidget().children()[4]
        switch_btn.clicked.connect(self.on_clicked)
        self.switch_btn = switch_btn
        
    def on_clicked(self):
        self.sum+=1
        if self.sum % 2 == 0:
            self.myThread.send_signal.disconnect(self.switch_slot)
            self.switch_btn.setText("Start")
        else:
            self.myThread.send_signal.connect(self.switch_slot)
            self.switch_btn.setText("Stop")
            self.myThread.start()
            
    def switch_slot(self, pics: str):
        pic1, pic2 = pics.split("=")
        s = self.centralWidget()
        if not os.path.exists(pic1) or not os.path.exists(pic2):
            # print(pic1)
            return
        
        for name, child in zip([ch.objectName() for ch in s.children()], s.children()):
            if name == "label" and isinstance(child, QtWidgets.QLabel):
                child.setPixmap(QtGui.QPixmap(pic1))
            if name == "label_2" and isinstance(child, QtWidgets.QLabel):
                child.setPixmap(QtGui.QPixmap(pic2))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = custom_window()
    #调自定义的界面（即刚转换的.py对象）
    # Ui = hello.Ui_MainWindow() #这里也引用了一次helloworld.py文件的名字注意
    # Ui.setupUi(MainWindow)


    MainWindow.resize(800, 480)
    MainWindow.setWindowTitle("Monitor")
    #显示窗口并释放资源
    MainWindow.show()
    sys.exit(app.exec_())