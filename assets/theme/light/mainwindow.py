lightTheme = '''
#MainApp {
    background-color: #F0F4F9;
}

MinimizeButton {
    qproperty-normalColor: black;
    qproperty-normalBackgroundColor: transparent;
    qproperty-hoverColor: black;
    qproperty-hoverBackgroundColor: rgba(0, 0, 0, 26);
    qproperty-pressedColor: black;
    qproperty-pressedBackgroundColor: rgba(0, 0, 0, 51)
}


MaximizeButton {
    qproperty-normalColor: black;
    qproperty-normalBackgroundColor: transparent;
    qproperty-hoverColor: black;
    qproperty-hoverBackgroundColor: rgba(0, 0, 0, 26);
    qproperty-pressedColor: black;
    qproperty-pressedBackgroundColor: rgba(0, 0, 0, 51)
}

CloseButton {
    qproperty-normalColor: black;
    qproperty-normalBackgroundColor: transparent;
}

#MainWindow QTreeView {
    background-color: #F0F4F9;
    border: none;
    border-radius: 5px;
    outline: none;
    selection-background-color: transparent;
}

#MainWindow QTreeWidget::item:selected {
    background-color: #E4E6E8;
    color: #000000;
    border: none;
}


#MainWindow QTreeWidget::item:selected:!active {
    background-color: #E4E6E8;
    color: #000000;
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
    background-color: #E7EAEF;
    color: #000000;
    border: none;
}


QTreeWidget::item:selected:hover {
    background-color: #E7EAEF;
    color: #000000;
    border: none;
}

#MainWindow QStackedWidget {
    border: 1px solid #F7F9FC;
    border-top-left-radius: 5px;
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