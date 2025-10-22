lightTheme = '''
ImageViewerWidget {
    background: #FFFFFF;
    color: #000000;
    border-top-left-radius: 5px;
}

QPushButton, QToolButton {
    background: transparent;
    border: 1px solid #e7e9ec;
    border-radius: 5px;
    color: #FFFFFF;
}
QPushButton:hover, QToolButton:hover {
    background: #e7e9ec;
    color: #000000;
}

QPushButton:pressed, QToolButton:pressed {
    background: #d4d6d8;
    color: #000000;
}

QToolButton::menu-indicator {
    width: 0px;  /* 隐藏箭头 */
}

QLabel {
    color: #000000;
    padding: 0 5px;
}

QSpinBox {
    border: 1px solid #e7e9ec;
    border-radius: 5px;
    color: #000000;
    padding: 0 5px;
}

QGraphicsView {
    border: none;
    border-top: 1px solid #e7e9ec;
}

QFileDialog{
    background: #FFFFFF;
    color: #000000;
}
QFileDialog *{
    background: #FFFFFF;
    color: #000000;
}
/* 选中项样式 */
QFileDialog QListView::item:selected,
QFileDialog QTreeView::item:selected {
    background: #0078d7;
    color: white;
}
/* 鼠标滑过样式 */
QFileDialog QListView::item:hover,
QFileDialog QTreeView::item:hover {
    background: rgb(231,233,236);
    color: #000000;
}
/* 鼠标选中时滑过 */
QFileDialog QListView::item:selected:hover,
QFileDialog QTreeView::item:selected:hover {
    background: #0078d7;
    color: white;
}
'''