import static
from components.canvas import CanvasQG
from PyQt5 import QtCore, QtGui, QtWidgets

class ImageViewerWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    # ---------- 界面构造 ----------
    def setup_ui(self):
        self.setObjectName("ImageViewerWidget")
        self.resize(917, 803)
        self.setWindowTitle("图片查看工具")

        # 整体垂直布局
        self.vlay_main = QtWidgets.QVBoxLayout(self)
        self.vlay_main.setContentsMargins(0, 0, 0, 0)
        self.vlay_main.setSpacing(0)

        # 顶部按钮/标签水平布局
        self.hlay_toolbar = QtWidgets.QHBoxLayout()
        self.hlay_toolbar.setObjectName("hlay_toolbar")

        #  添加菜单按钮 toolbutton
        self.btn_menu = QtWidgets.QToolButton()
        self.btn_menu.setObjectName("btn_menu")
        self.btn_menu.setFixedSize(32, 32)
        self.btn_menu.setIcon(QtGui.QIcon(":/menu/light/menu.png"))
        self.btn_menu.setToolTip("菜单")
        self.hlay_toolbar.addWidget(self.btn_menu)

        # 创建菜单并添加到按钮
        self.menu = QtWidgets.QMenu(self)
        self.btn_menu.setMenu(self.menu)
        self.btn_menu.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        
        # 添加菜单项
        self.action_open = self.menu.addAction("选择图片目录")
        self.action_open.setShortcut("Ctrl+O")
        self.action_open.setIcon(QtGui.QIcon(":/brmenu/light/folder-setting.png"))

        # 1. 左侧伸缩
        self.hlay_toolbar.addItem(QtWidgets.QSpacerItem(40, 20,QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        # 2. 上一张
        self.btn_prev = QtWidgets.QPushButton()
        self.btn_prev.setObjectName("btn_prev")
        self.btn_prev.setFixedSize(32, 32)
        self.btn_prev.setIcon(QtGui.QIcon(":/image/light/left.png"))
        self.btn_prev.setShortcut(QtCore.Qt.Key_Left)
        self.btn_prev.setToolTip("上一张")
        self.hlay_toolbar.addWidget(self.btn_prev)

        # 3. 图片名
        self.hlay_toolbar.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.img_name = QtWidgets.QLabel("未加载图片")
        self.img_name.setAlignment(QtCore.Qt.AlignCenter)
        self.img_name.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.img_name.setObjectName("img_name")
        self.hlay_toolbar.addWidget(self.img_name)

        # 4. 下一张
        self.hlay_toolbar.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.btn_next = QtWidgets.QPushButton()
        self.btn_next.setObjectName("btn_next")
        self.btn_next.setFixedSize(32, 32)
        self.btn_next.setIcon(QtGui.QIcon(":/image/light/right.png"))
        self.btn_next.setShortcut(QtCore.Qt.Key_Right)
        self.btn_next.setToolTip("下一张")
        self.hlay_toolbar.addWidget(self.btn_next)

        # 5. 分隔线 + 索引显示
        self.hlay_toolbar.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        line1 = QtWidgets.QFrame()
        line1.setFrameShape(QtWidgets.QFrame.VLine)
        line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hlay_toolbar.addWidget(line1)

        self.hlay_toolbar.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.img_idx_now = QtWidgets.QLabel("0")
        self.img_idx_now.setObjectName("img_idx_now")
        self.hlay_toolbar.addWidget(self.img_idx_now)

        self.img_idx_seg = QtWidgets.QLabel("/")
        self.img_idx_seg.setObjectName("img_idx_seg")
        self.hlay_toolbar.addWidget(self.img_idx_seg)

        self.img_idx_total = QtWidgets.QLabel("0")
        self.img_idx_total.setObjectName("img_idx_total")
        self.hlay_toolbar.addWidget(self.img_idx_total)

        # 6. 跳转输入框
        self.hlay_toolbar.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.img_idx_input = QtWidgets.QSpinBox()
        self.img_idx_input.setObjectName("img_idx_input")
        self.img_idx_input.setAlignment(QtCore.Qt.AlignCenter)
        self.img_idx_input.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.img_idx_input.setMaximum(999999999)
        self.hlay_toolbar.addWidget(self.img_idx_input)

        # 7. 分隔线 + 旋转/删除
        self.hlay_toolbar.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        line2 = QtWidgets.QFrame()
        line2.setFrameShape(QtWidgets.QFrame.VLine)
        line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hlay_toolbar.addWidget(line2)

        self.hlay_toolbar.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.btn_xuanzhuan = QtWidgets.QPushButton()
        self.btn_xuanzhuan.setObjectName("btn_xuanzhuan")
        self.btn_xuanzhuan.setFixedSize(32, 32)
        self.btn_xuanzhuan.setIcon(QtGui.QIcon(":/image/light/rotate.png"))
        self.btn_xuanzhuan.setShortcut(QtCore.Qt.Key_R)
        self.btn_xuanzhuan.setToolTip("旋转")
        self.hlay_toolbar.addWidget(self.btn_xuanzhuan)

        self.hlay_toolbar.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.btn_del = QtWidgets.QPushButton()
        self.btn_del.setObjectName("btn_del")
        self.btn_del.setFixedSize(32, 32)
        self.btn_del.setIcon(QtGui.QIcon(":/image/light/delete.png"))
        self.btn_del.setShortcut(QtCore.Qt.Key_Delete)
        self.hlay_toolbar.addWidget(self.btn_del)

        # 8. 右侧伸缩
        self.hlay_toolbar.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        # 9. 图片显示区
        self.graphicsView = CanvasQG(self)
        self.graphicsView.setObjectName("graphicsView")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.graphicsView.setSizePolicy(sizePolicy)

        # 把 toolbar 和 graphicsView 放进主布局
        self.vlay_main.addLayout(self.hlay_toolbar)
        self.vlay_main.addWidget(self.graphicsView)
