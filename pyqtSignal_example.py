import sys
from multiprocessing import Process, Pipe
import time

from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class SubClass(QThread):
    end_signal = pyqtSignal(int)

    def __init__(self, last_frame_pipe):
        QThread.__init__(self)
        self.last_frame_pipe = last_frame_pipe

    def run(self):
        print('checking video!')
        while True:
            ret = self.last_frame_pipe.recv()

            if ret % 5 == 0:
                print('ret : ', ret)
                self.end_signal.emit(1)

            else:
                print('none')


class MainClass(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('title')
        self.setGeometry(10, 10, 320, 200)
        self.button = QPushButton('button', self)
        self.button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
        self.button.move(100, 70)
        self.button.setText('Press Me')
        self.show()

        self.send, self.recv = Pipe()
        self.sub = SubClass(self.recv)
        self.sub.end_signal.connect(self.update)
        self.sub.start()


        external_func_process = Process(target=external_func, args=(self.send, ))
        external_func_process.start()

    # @pyqtSlot()
    def update(self, signal):
        print('Main window update, signal : ', signal)


def external_func(send_pipe):
    cnt = 0
    while True:
        send_pipe.send(cnt)
        cnt += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainClass()
    mainWindow.show()
    sys.exit(app.exec_())
