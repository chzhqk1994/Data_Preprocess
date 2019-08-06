import sys
from multiprocessing import Process, Pipe, Lock
import time

from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class MainClass(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLock = Lock()
        self.setWindowTitle('title')
        self.setGeometry(10, 10, 320, 200)
        self.button = QPushButton('button', self)
        self.button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
        self.button.move(100, 70)
        self.button.setText('kill process')
        self.button.clicked.connect(self.killall)

        self.button2 = QPushButton('button', self)
        self.button2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
        self.button2.move(200, 70)
        self.button2.setText('restart process')
        self.button2.clicked.connect(self.revive)
        self.show()

        self.external_func_process = Process(target=external_func, args=())
        self.external_func_process.start()

        self.external_func_process2 = Process(target=external_func2, args=())
        self.external_func_process2.start()

    def killall(self):
        with self.mainLock:
            self.external_func_process.terminate()
            time.sleep(0.01)
            if not self.external_func_process.is_alive():
                self.external_func_process.join()

        with self.mainLock:
            self.external_func_process2.terminate()
            time.sleep(0.01)
            if not self.external_func_process2.is_alive():
                self.external_func_process2.join()

        with self.mainLock:
            del self.external_func_process
            time.sleep(0.01)
            del self.external_func_process2

    def revive(self):
        self.external_func_process = Process(target=external_func, args=())
        self.external_func_process.start()

        self.external_func_process2 = Process(target=external_func2, args=())
        self.external_func_process2.start()


def external_func():
    cnt = 0
    while True:
        print(cnt)
        cnt += 1


def external_func2():
    cnt = 10000000000
    while True:
        print(cnt)
        cnt -= 1


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainClass()
    mainWindow.show()
    sys.exit(app.exec_())
