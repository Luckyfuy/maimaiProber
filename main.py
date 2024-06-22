#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
import sys
import asyncio

import MainWindow
from maimai_best_40 import generate
from maimai_best_50 import generate50
from maimai_best_50_2 import generate50_2

class maimaiProber(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.generate.clicked.connect(self.generate)

    def generate(self):
        if self.ui.qqButton.isChecked():
            payload = {'qq': self.ui.qq.displayText()}
        elif self.ui.usernameButton.isChecked():
            payload = {'username': self.ui.username.displayText()}

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        if self.ui.b40.isChecked():
            img, success = loop.run_until_complete(generate(payload))
        elif self.ui.b50.isChecked():
            payload['b50'] = True
            # img, success = loop.run_until_complete(generate50(payload))
            img, success = loop.run_until_complete(generate50_2(payload))
        loop.close()

        if success == 400:
            QMessageBox.information(self, '错误', '未找到该玩家，请确保该玩家的用户名和查分器中的用户名相同')
        elif success == 403:
            QMessageBox.information(self, '错误', '该玩家禁止了其他人获取数据')
        else:
            fname = QFileDialog.getSaveFileName(self, '保存图片', '.', 'PNG (*.png)')
            img.save(fname[0], 'png')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    maimaiProber = maimaiProber()
    sys.exit(app.exec())