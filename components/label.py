import static
from config.config import config, siganl
from PyQt5 import QtWidgets, QtCore, QtGui

class ElidedLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._elide_mode = QtCore.Qt.ElideRight
        self._full_text = ""
        self.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)

    def setText(self, text: str):
        # 永远保存完整内容
        self._full_text = text
        self.update_elided_text()

    def text(self) -> str:
        # 返回完整文本，而不是省略的
        return self._full_text

    def setElideMode(self, mode):
        self._elide_mode = mode
        self.update_elided_text()

    def update_elided_text(self):
        fm = QtGui.QFontMetrics(self.font())
        available_width = max(0, self.width() - self.contentsMargins().left() - self.contentsMargins().right())
        elided = fm.elidedText(self._full_text, self._elide_mode, available_width)
        super().setText(elided)

        # 🚀 判断是否被省略，设置 tooltip
        if elided != self._full_text:
            self.setToolTip(self._full_text)
        else:
            self.setToolTip("")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_elided_text()


class ScaleLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFixedSize(60, 30)
        self.moveCenter()
        self.setStyleSheet('''
            background-color: rgba(0, 0, 0, 0.3);
            border-radius: 15px;
            color: white;
        ''')

    def moveCenter(self):
        self.move((self.parent().width() - self.width()) // 2, (self.parent().height() - self.height()) // 2)
