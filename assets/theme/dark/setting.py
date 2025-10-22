darkTheme = '''
AppSetting {
    background: #242730;
    color: #000000;
    border-top-left-radius: 5px;
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
QScrollArea {
    background: #242730;
    border-top-left-radius: 5px;
}

QScrollArea * {
    background: #242730;
}

QPushButton {
    background: rgba(255, 255, 255, 0.0605);
    border: 1px solid rgba(255, 255, 255, 0.053);
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 5px;
    padding: 5px 10px;
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

QLabel#title_label {
    color: rgb(208, 208, 208);
    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
    font-weight: bold;
}

QLabel#content_label {
    font: 11px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
    color: rgb(208, 208, 208);
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
    color: rgb(208, 208, 208);
    font: 20px "Segoe UI SemiBold", "Microsoft YaHei", 'PingFang SC';
}

QGroupBox QWidget#widget {
    background-color: #31323B; /* 内容背景 */
    border-radius: 8px; /* 圆角 */
}
QGroupBox QWidget QLabel {
    background-color: #30323A; /* 内容背景 */
}

QGroupBox::title {
    subcontrol-origin: margin; /* 标题位置 */
    subcontrol-position: top left; /* 左上对齐 */
    left: 0px; /* 左偏移 */
    top:  5px; /* 上偏移（覆盖边框） */
    padding: 0 4px;
    background-color: transparent; /* 标题背景（覆盖边框） */
}
'''