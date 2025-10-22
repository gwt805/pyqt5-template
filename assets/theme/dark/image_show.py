darkTheme = '''
ImageViewerWidget {
    background: #242730;
    color: #FFFFFF;
}

ImageViewerWidget * {
    background: #242730;
    color: #FFFFFF;
}

QGraphicsView {
    border: none;
    border-top: 1px solid #31323B;
}

QPushButton {
    background: rgba(255, 255, 255, 0.0605);
    border: 1px solid rgba(255, 255, 255, 0.053);
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 5px;
    padding: 5px 36px 5px 36px;
    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
    color: white;
    outline: none;
}

QPushButton:hover {
    background: rgba(255, 255, 255, 0.0837);
}

QPushButton:pressed {
    color: rgba(255, 255, 255, 0.786);
    background: rgba(255, 255, 255, 0.0326);
    border-top: 1px solid rgba(255, 255, 255, 0.053);
}

QToolButton::menu-indicator {
    width: 0px;  /* 隐藏箭头 */
}

QSpinBox {
    border: 1px solid #292D37;
    border-radius: 5px;
    color: white;
    padding: 0 5px;
}

QLabel {
    padding: 0 5px;
}

QFileDialog{
    background: #242730;
    color: rgb(208, 208, 208);
}
QFileDialog *{
    background: #242730;
    color: rgb(208, 208, 208);
}
/* 选中项样式 */
QFileDialog QListView::item:selected,
QFileDialog QTreeView::item:selected {
    background: #3daee9;
    color: white;
}
/* 鼠标滑过样式 */
QFileDialog QListView::item:hover,
QFileDialog QTreeView::item:hover {
    background: rgb(66,67,75);
    color: white;
}
/* 鼠标选中时滑过 */
QFileDialog QListView::item:selected:hover,
QFileDialog QTreeView::item:selected:hover {
    background: #3daee9;
    color: white;
}
'''