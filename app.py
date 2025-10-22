import sys
from PyQt5.QtGui import QIcon
from view.start import StartWindow
from config.config import siganl, config
from logic.main_window import MainWindow
from assets.theme.dark.mainwindow import darkTheme
from assets.theme.light.mainwindow import lightTheme
from qframelesswindow import FramelessWindow, StandardTitleBar
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, QCoreApplication
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QDesktopWidget, QSystemTrayIcon, QMenu, QAction

class App(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.screenRect = None
        self.start = StartWindow()
        self.setupUi()
        self.loadTrayMenu()
        self.center_window()
        self.setTheme(config.is_dark)
        siganl.is_dark.connect(self.setTheme)
        
        # 设置启动窗口与主窗口相同的样式和位置
        self.start.setStyleSheet(self.styleSheet())
        self.start.resize(self.size())
        self.start.move(self.pos())
        
        # 隐藏主窗口，显示启动窗口
        self.hide()
        self.start.show()
        
        # 3秒后开始过渡
        QTimer.singleShot(2000, self.start_transition)

    def setupUi(self):
        self.resize(800, 550)
        self.setMinimumSize(800, 550)
        self.title_bar = StandardTitleBar(self)
        self.title_bar.setTitle("PyQt5-Template")
        self.title_bar.setIcon(":/logo.png")
        self.setTitleBar(self.title_bar)
        self.setObjectName("MainApp")

        self.main_ui = MainWindow(self)
        self.main_ui.setAttribute(Qt.WA_StyledBackground, True)
        self.main_ui.stackedWidget.setAttribute(Qt.WA_StyledBackground, True)
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 32, 0, 0)
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.main_ui)
    
    def setTheme(self, is_dark: bool):
        if is_dark:
            self.setStyleSheet(darkTheme)
        else:
            self.setStyleSheet(lightTheme)
        self.main_ui.updateIcon(is_dark)

    def start_transition(self):
        """开始启动窗口到主窗口的过渡"""
        # 创建主窗口淡入动画
        self.fade_in = QPropertyAnimation(self, b"windowOpacity")
        self.fade_in.setDuration(300)  # 300毫秒
        self.fade_in.setStartValue(0.0)
        self.fade_in.setEndValue(1.0)
        self.fade_in.setEasingCurve(QEasingCurve.InOutQuad)
        
        # 创建启动窗口淡出动画
        self.fade_out = QPropertyAnimation(self.start, b"windowOpacity")
        self.fade_out.setDuration(300)
        self.fade_out.setStartValue(1.0)
        self.fade_out.setEndValue(0.0)
        self.fade_out.setEasingCurve(QEasingCurve.InOutQuad)
        
        # 同时启动两个动画
        self.fade_in.start()
        self.fade_out.start()
        
        # 显示主窗口
        self.show()
        self.raise_()
        self.activateWindow()
        
        # 动画结束后关闭启动窗口
        self.fade_out.finished.connect(self.start.close)

    def center_window(self):
        """将窗口居中显示在屏幕上"""
        screen_geometry = QDesktopWidget().screenGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def loadTrayMenu(self):
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon(':/logo.png'))
        showAction = QAction(QIcon(':/open.png'), "打开", self, triggered = self.Show)
        quitAction = QAction(QIcon(':/exit.png'), "退出", self, triggered = lambda: QCoreApplication.instance().quit())
        self.trayMenu = QMenu(self)
        self.trayMenu.addAction(showAction)
        self.trayMenu.addSeparator()
        self.trayMenu.addAction(quitAction)
        self.tray.setContextMenu(self.trayMenu)
        self.tray.show()

    def Show(self):
        self.show()
        self.raise_()
        self.activateWindow()

    def closeEvent(self, event):
        self.hide()
        event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())