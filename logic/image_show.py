import os, static
from natsort import natsorted
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QIcon
from components.label import ScaleLabel
from config.config import siganl, config
from view.imgshow import ImageViewerWidget
from assets.theme.dark.image_show import darkTheme
from assets.theme.light.image_show import lightTheme
from PyQt5.QtWidgets import QFileDialog, QGraphicsPixmapItem, QMessageBox

class AppImageView(ImageViewerWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.image_extensions = ('.png', '.jpg', '.jpeg', '.svg', '.webp', '.ico', '.icon', '.gif', '.bmp')
        self.img_idx = 0
        self.img_list = []
        self.path = ""
        self.setTheme(config.is_dark)
        siganl.is_dark.connect(self.setTheme)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.btn_prev.clicked.connect(lambda: self.image_option("prev"))
        self.btn_next.clicked.connect(lambda: self.image_option("next"))
        self.btn_xuanzhuan.clicked.connect(self.rotate_img)
        self.btn_del.clicked.connect(self.delete_img)
        self.img_idx_input.textChanged.connect(self.input_img_idx)
        self.graphicsView.scaleChanged.connect(self.update_scale_status)        
        self.action_open.triggered.connect(self.get_imgs)

        self.scale_label = ScaleLabel(self)
        self.scale_label.setHidden(True)

    def setTheme(self, theme: bool):
        if theme:
            self.setStyleSheet(darkTheme)
        else:
            self.setStyleSheet(lightTheme)
        self.updateIcon()

    def updateIcon(self):
        if config.is_dark:
            self.btn_prev.setIcon(QIcon(":/image/dark/left.png"))
            self.btn_next.setIcon(QIcon(":/image/dark/right.png"))
            self.btn_xuanzhuan.setIcon(QIcon(":/image/dark/rotate.png"))
            self.btn_del.setIcon(QIcon(":/image/dark/delete.png"))
            self.btn_menu.setIcon(QIcon(":/menu/dark/menu.png"))
            self.action_open.setIcon(QIcon(":/brmenu/dark/folder-setting.png"))
            
        else:
            self.btn_prev.setIcon(QIcon(":/image/light/left.png"))
            self.btn_next.setIcon(QIcon(":/image/light/right.png"))
            self.btn_xuanzhuan.setIcon(QIcon(":/image/light/rotate.png"))
            self.btn_del.setIcon(QIcon(":/image/light/delete.png"))
            self.btn_menu.setIcon(QIcon(":/menu/light/menu.png"))
            self.action_open.setIcon(QIcon(":/brmenu/light/folder-setting.png"))

    def get_imgs(self, path: str):
        self.path = QFileDialog.getExistingDirectory(self, "选择图片所在文件夹")
        if self.path:
            self.img_list = self.find_image_files()
            self.img_list = natsorted(self.img_list)
            if self.img_list:
                self.img_idx_now.setText("1")
                self.img_idx_total.setText(str(len(self.img_list)))
                self.img_idx_input.setMaximum(len(self.img_list))
            self.img_show("first")

    def find_image_files(self):
        image_files = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.lower().endswith(self.image_extensions):
                    image_files.append(os.path.join(root, file))
        return image_files

    def update_scale_status(self, scale_value):
        percent = int(scale_value * 100)
        self.scale_label.setText(f"{percent}%")
        self.scale_label.setHidden(False)
        QTimer.singleShot(2000, self.scale_label.hide)

    def input_img_idx(self):
        if self.path and self.img_list:
            if self.img_idx_input.value() <= 0:
                self.img_idx_input.setValue(1)
                self.img_idx_now.setText("1")
                self.img_idx = 0
            elif self.img_idx_input.value() > len(self.img_list):
                self.img_idx_input.setValue(len(self.img_list))
                self.img_idx_now.setText(str(len(self.img_list)))
                self.img_idx = len(self.img_list) - 1
            else:
                self.img_idx = int(self.img_idx_input.text()) - 1
                self.img_show("update")
        else:
            self.img_idx_input.setMaximum(0)

    def img_show(self, option):
        if self.img_list:
            try:
                self.img_name.setText(f" {self.img_list[self.img_idx]} ")
                self.img_idx_now.setText(str(self.img_idx + 1))
                frame = QPixmap(self.img_list[self.img_idx])
                self.graphicsView.image = frame
                self.graphicsView.image_item = QGraphicsPixmapItem(frame)
                if option == "first":
                    self.graphicsView.loadImage()
                if option == "update":
                    self.graphicsView.update_image()
            except Exception as e:
                self.showMsg("错误提示", f"err: {str(e)}")
        else:
            self.img_name.setText(" 未找到图片 ")
            self.img_idx_now.setText("0")
            self.graphicsView.scene.clear()
            self.graphicsView.image_item = None
            self.scale_label.setText(f"缩放比例: 0%")
            return None

    def rotate_img(self):
        if self.img_list:
            self.graphicsView.rotate_image()
    
    def delete_img(self):
        if self.img_list:
            try:
                os.remove(self.img_list[self.img_idx])
                self.img_list.pop(self.img_idx)
                self.img_idx_total.setText(str(len(self.img_list)))
                if self.img_idx > len(self.img_list) - 1:
                    self.img_idx = len(self.img_list) - 1
                self.img_show("update")
            except Exception as e:
                self.showMsg("错误提示", f"err: {str(e)}")

    def image_option(self, option: str):
        if self.img_list:
            if option == "prev":
                if self.img_idx - 1 >= 0:
                    self.img_idx -= 1

            if option == "next":
                if self.img_idx < len(self.img_list) - 1:
                    self.img_idx += 1
            self.img_show("update")

    def showMsg(self, title: str, msg: str):
        reply = QMessageBox(QMessageBox.Warning, title, msg, QMessageBox.NoButton, self)
        reply.addButton("确定", QMessageBox.YesRole)
        reply.addButton("取消", QMessageBox.NoRole)
        reply.exec_()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.scale_label.moveCenter()