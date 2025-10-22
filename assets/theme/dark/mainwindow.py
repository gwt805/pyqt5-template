darkTheme = '''
#MainApp {
    background-color: #1C202A;
}

#MainApp * {
    color: white;
    font: 13px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
}
MinimizeButton {
    qproperty-normalColor: white;
    qproperty-normalBackgroundColor: transparent;
    qproperty-hoverColor: white;
    qproperty-hoverBackgroundColor: rgba(255, 255, 255, 26);
    qproperty-pressedColor: white;
    qproperty-pressedBackgroundColor: rgba(255, 255, 255, 51)
}


MaximizeButton {
    qproperty-normalColor: white;
    qproperty-normalBackgroundColor: transparent;
    qproperty-hoverColor: white;
    qproperty-hoverBackgroundColor: rgba(255, 255, 255, 26);
    qproperty-pressedColor: white;
    qproperty-pressedBackgroundColor: rgba(255, 255, 255, 51)
}

CloseButton {
    qproperty-normalColor: white;
    qproperty-normalBackgroundColor: transparent;
}

#MainWindow QTreeView {
    background-color: #1C202A;
    border: none;
    border-radius: 5px;
    outline: none;
    selection-background-color: transparent;
    color: rgba(255, 255, 255, 0.7);
}

#MainWindow QTreeWidget::item:selected {
    background-color: #292D37;
    color: rgba(255, 255, 255, 0.7);  /* 统一选中项颜色 */
    border: none;
}

#MainWindow QTreeWidget::item:selected:!active {
    background-color: #292D37;
    color: rgba(255, 255, 255, 0.7);  /* 修正：非活动状态也使用半透明白色 */
    border: none;
}

#MainWindow QTreeWidget::item:selected:active {
    background-color: rgba(255, 255, 255, 0.06);
    color: rgba(255, 255, 255, 0.7);
    border: none;
}

QTreeWidget::item:selected {
    border: none;
    background: transparent;
}

QTreeWidget::item:focus {
    border: none;
}

QTreeWidget::item:hover {
    background-color: rgba(255, 255, 255, 0.08);
    color: rgba(255, 255, 255, 0.7);
    border: none;
}

QTreeWidget::item:selected:hover {
    background-color: rgba(255, 255, 255, 0.08);
    color: rgba(255, 255, 255, 0.7);
    border: none;
}

#MainWindow QStackedWidget {
    border: 1px solid #242730;
    border-top-left-radius: 5px;
    background-color: transparent;
}

QScrollBar:vertical {
    width: 10px; /* 垂直滚动条宽度 */
    background-color: #f1f5f9; /* 滚动条背景 */
}
QScrollBar:horizontal {
    height: 10px; /* 水平滚动条高度 */
    background-color: #f1f5f9; /* 滚动条背景 */
}
QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background-color: #cbd5e1; /* 滑块背景 */
    border-radius: 5px; /* 滑块圆角 */
}
QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
    background-color: #94a3b8; /* 滑块悬停背景 */
}
QScrollBar::add-line, QScrollBar::sub-line {
    background-color: transparent; /* 隐藏增减按钮 */
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0px;
}

'''