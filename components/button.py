import sys
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel


class BaseTogolButton(QWidget):
    toggled = pyqtSignal(bool)          # 对外暴露的信号

    def __init__(self, parent=None, width=35, height=20):
        super().__init__(parent)
        self._w, self._h = width, height
        self.setFixedSize(QSize(width, height))
        self.setCursor(Qt.PointingHandCursor)

        self._on = False                # 内部状态
        self._margin = 3                # 滑块与边框间距
        self._slider_radius = (height - 2 * self._margin) // 2

    def isChecked(self):
        return self._on

    def setChecked(self, on: bool):
        if self._on != on:
            self._on = on
            self.update()
            self.toggled.emit(self._on)

    def mousePressEvent(self, _):
        self.setChecked(not self._on)

    # 画背景 + 滑块
    def paintEvent(self, _):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 背景圆角矩形
        brush = QBrush(QColor("#27ae60") if self._on else QColor("#EDEEEF"))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(0, 0, self._w, self._h, self._h//2, self._h//2)

        # 滑块
        brush.setColor(Qt.white)
        painter.setBrush(brush)
        x = self._w - self._h + self._margin if self._on else self._margin
        painter.drawEllipse(x, self._margin,
                            self._h - 2 * self._margin,
                            self._h - 2 * self._margin)


class TogolButton(QWidget):
    togolSignal = pyqtSignal(bool)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(75)
        self.setWindowTitle("PyQt5 SwitchButton 示例")
        self.switch = BaseTogolButton()
        self.label = QLabel("浅色")
        self.switch.toggled.connect(self.on_toggle)

        lay = QHBoxLayout(self)
        lay.addWidget(self.label)
        lay.addWidget(self.switch)
        lay.addStretch()

    def on_toggle(self, on):
        self.label.setText("深色" if on else "浅色")
        self.togolSignal.emit(True if on else False)