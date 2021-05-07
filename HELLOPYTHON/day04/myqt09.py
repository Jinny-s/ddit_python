import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("myqt09.ui")[0]

global num

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb0.clicked.connect(self.pbClick)
        # btn_list = [self.pb1, self.pb2, self.pb3, self.pb4, self.pb5, self.pb6, self.pb7, self.pb8, self.pb9, self.pb0]
        
        # for i in range(0, 11):
        #     btn_list[i].clicked.connect(self.pbClick)
            
    def pbClick(self):
        
        num = self.pb0.text()
        self.le.setText(num)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()