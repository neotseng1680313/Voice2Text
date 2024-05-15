import sys
from os import environ
from PyQt5 import QtWidgets, QtCore
from New_Ui import Ui_MainWindow  # 確保引用的是 New_Ui.py 中的正確類名

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"  # 不推薦使用，已被廢棄
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"  # 讓 Qt 自動根據系統 DPI 設定縮放
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"  # 可以為不同屏幕設置不同的縮放因子
    environ["QT_SCALE_FACTOR"] = "1"  # 設置全局縮放因子

if __name__ == '__main__':
    suppress_qt_warnings()  # 在應用啟動前調用

    # 確保 Qt 的屬性設置匹配環境變量設置
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 啟用高 DPI 縮放
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)  # 啟用高解析度圖標

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 修改為 QMainWindow
    ui = Ui_MainWindow()  # 使用 New_Ui.py 中的 Ui_MainWindow 類
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
