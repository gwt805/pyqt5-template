lightTheme = '''
AppSetting {
    background: #FFFFFF;
    color: #000000;
    border-top-left-radius: 5px;
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

QScrollArea {
    background: #FFFFFF;
    border-top-left-radius: 5px;
}

QScrollArea * {
    background: #FFFFFF;
}

QPushButton {
    background: transparent;
    border: 1px solid #e7e9ec;
    border-radius: 5px;
    padding: 5px 10px;
}
QPushButton:hover {
    background: #e7e9ec;
    color: #000000;
}

QPushButton:pressed {
    background: #d4d6d8;
    color: #000000;
}

QLabel#title_label {
    color: black;
    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
    font-weight: bold;
}

QLabel#content_label {
    color: rgb(118, 118, 118);
    font: 12px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
}

QGraphicsView {
    border: none;
    border-top: 1px solid #e7e9ec;
}

QGroupBox {
    border: none; /*1px solid #e2e8f0;  边框 */
    border-radius: 8px; /* 圆角 */
    margin-top: 14px; /* 标题与内容间距 */
    margin-bottom: 20px; /* 标题与内容间距 */
    padding: 15px 0 5px 0; /* 内边距 */
    color: black;
    font: 20px "Segoe UI SemiBold", "Microsoft YaHei", 'PingFang SC';
}

QGroupBox QWidget#widget {
    background-color: #f5f8fa; /* 内容背景 */
    border-radius: 8px; /* 圆角 */
}
QGroupBox QWidget QLabel {
    background-color: #f5f8fa; /* 内容背景 */
}

QGroupBox::title {
    subcontrol-origin: margin; /* 标题位置 */
    subcontrol-position: top left; /* 左上对齐 */
    left: 0px; /* 左偏移 */
    top:  5px; /* 上偏移（覆盖边框） */
    padding: 0 4px;
    background-color: #FFFFFF; /* 标题背景（覆盖边框） */
}
'''