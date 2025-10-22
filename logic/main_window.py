import static
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
from view.main_window import UI_MainWindow
from logic.image_show import AppImageView
from logic.setting import AppSetting
from PyQt5.QtWidgets import QTreeWidgetItem

class MainWindow(UI_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_collapsed = False
        self.imageViewerWidget_wd = AppImageView(self)
        self.setting_wd = AppSetting(self)
        self.router = {}
        self.menu_collapse.itemClicked.connect(self.changeMenuWidth)
        self.menu_collapse.doubleClicked.connect(self.changeMenuWidth)
        self.menu_scroll.itemClicked.connect(self.changeStackedWidget)
        self.menu_bottom.itemClicked.connect(self.changeStackedWidget)
        self._initMenu()
        self.addStaticWidget()
    
    def addStaticWidget(self):
        self.router[self.imageViewerWidget_wd.windowTitle()] = self.stackedWidget.addWidget(self.imageViewerWidget_wd)
        self.router[self.setting_wd.windowTitle()] = self.stackedWidget.addWidget(self.setting_wd)
        self.stackedWidget.setCurrentIndex(0)

    def _initMenu(self):
        self.addMenuCollapseWidget()
        self.addMenuScrollWidget("image.png", self.imageViewerWidget_wd.windowTitle())
        self.addMenuBottomWidget()
        self.menu_scroll.setCurrentItem(self.menu_scroll.topLevelItem(0))

    def addMenuScrollWidget(self, micon: str, name: str):
        item = QTreeWidgetItem(self.menu_scroll)
        item.setText(0, '')
        icon = QIcon()
        icon.addPixmap(QPixmap(f":/menu/light/{micon}"), QIcon.Normal, QIcon.Off)
        item.setIcon(1, icon)
        item.setText(2, name)
        item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)
        self.menu_scroll.addTopLevelItem(item)
        self.iconlist.append((item, micon))

    def changeMenuWidth(self):
        if not self.is_collapsed:
            self.menu_bottom.setColumnHidden(2, True)
            self.menu_scroll.setColumnHidden(2, True)
            self.menu_bottom.setMaximumWidth(70)
            self.menu_scroll.setMaximumWidth(70)
            self.menu_collapse.setMaximumWidth(70)
            self.is_collapsed = True
        else:
            self.menu_bottom.setColumnHidden(2, False)
            self.menu_scroll.setColumnHidden(2, False)
            self.menu_bottom.setMaximumWidth(200)
            self.menu_scroll.setMaximumWidth(200)
            self.menu_collapse.setMaximumWidth(200)
            self.is_collapsed = False
    
    def clearMenuSelected(self, option):
        if option == 'scroll':
            self.menu_scroll.clearSelection()
        elif option == 'bottom':
            self.menu_bottom.clearSelection()
    
    def changeStackedWidget(self, item):
        if item.text(2) == "设置":
            self.clearMenuSelected('scroll')
        else: self.clearMenuSelected('bottom')
        self.stackedWidget.setCurrentIndex(self.router[item.text(2)])

    def updateIcon(self, theme: bool):
        if theme:
            for item, icon in self.iconlist:
                item.setIcon(1, QIcon(f":/menu/dark/{icon}"))
        else:
            for item, icon in self.iconlist:
                item.setIcon(1, QIcon(f":/menu/light/{icon}"))