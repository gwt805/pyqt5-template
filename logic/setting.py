import os
from PyQt5 import QtWidgets
from config.config import config
from PyQt5.QtGui import  QPixmap
from assets.theme.light.setting import lightTheme
from assets.theme.dark.setting import darkTheme
from view.setting import UI_AppSetting
from PyQt5.QtCore import pyqtSignal, Qt
from __init__ import auth, version, year

class AppSetting(UI_AppSetting):
    themeSignal = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTheme(config.is_dark)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.pushButton.togolSignal.connect(self.setTheme)
        self._init_card()

    def setTheme(self, theme: bool):
        if theme: self.setStyleSheet(darkTheme)
        else: self.setStyleSheet(lightTheme)
        config.is_dark = theme
        config.scmap['is_dark'].emit(theme)
        self.updateIcon()

    def _init_card(self):
        # add other card
        # box,vlayout = self.create_card("图片查看工具")
        # content = self.create_widget_lcr(box, "folder-open.png", "图片目录", "空", "选择目录", self.select_image_path, config.scmap['image_view_path'])
        # vlayout.addWidget(content)
        self.verticalLayout_2.removeItem(self.scrollspacerbottom)
        # self.verticalLayout_2.addWidget(box)

        # info card mast last
        box,vlayout = self.create_card("关于")
        content = self.create_widget_l(box, "info.png", "MI-Tool-Plus", f"© 版权所有 {year}, {auth}, 当前版本 {version}")
        vlayout.addWidget(content)
        self.verticalLayout_2.addWidget(box)

        self.verticalLayout_2.addSpacerItem(self.scrollspacerbottom)

    def updateIcon(self):
        if config.is_dark:
            for icon_label, icon in self.iconlist:
                icon_label.setPixmap(QPixmap(f":/setting/dark/{icon}"))
        else:
            for icon_label, icon in self.iconlist:
                icon_label.setPixmap(QPixmap(f":/setting/light/{icon}"))