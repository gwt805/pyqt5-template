# Qsetting
from PyQt5.QtCore import QObject, pyqtSignal

class Signal(QObject):
    is_dark = pyqtSignal(bool)

siganl = Signal()


class Config(QObject):
    def __init__(self):
        self.scmap = {
            "is_dark": siganl.is_dark,
        }
        self.is_dark = False

config = Config()