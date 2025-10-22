from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QPointF
from PyQt5.QtGui import QPainter, QPixmap, QWheelEvent, QMouseEvent, QTransform
from PyQt5.QtWidgets import  QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QWidget

class CanvasQG(QGraphicsView):
    scaleChanged = pyqtSignal(float)
    def __init__(self, parent=None):
        super().__init__()
        self.setParent(parent)
        self.image = None
        self.image_item = None
        self.current_angle = 0
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def get_fit_scale(self):
        if not self.image_item:
            return 1.0
        view_rect = self.viewport().rect()
        scene_rect = self.image_item.boundingRect()
        if scene_rect.width() == 0 or scene_rect.height() == 0:
            return 1.0
        scale_x = view_rect.width() / scene_rect.width()
        scale_y = view_rect.height() / scene_rect.height()
        return min(scale_x, scale_y)

    def loadImage(self):
        if self.image:
            if self.image_item:
                self.scene.clear()
        self.image_item = QGraphicsPixmapItem(self.image)
        self.image_item.setFlag(QGraphicsPixmapItem.ItemIsMovable)
        self.scene.addItem(self.image_item)
        self.fitInView(self.image_item, Qt.KeepAspectRatio)
        self.show()
        self.scaleChanged.emit(self.get_fit_scale())

    def wheelEvent(self, event: QWheelEvent):
        if self.image_item:
            if event.angleDelta().y() > 0:
                self.scale(1.1, 1.1)
            else:
                self.scale(1 / 1.1, 1 / 1.1)

            # 从视图变换矩阵拿真实缩放比例
            transform = self.transform()
            scale_factor = transform.m11()  # x 方向缩放，y 同理 m22()
            self.scaleChanged.emit(scale_factor)

    def update_image(self):
        if self.image:
            if self.image_item:
                self.scene.clear()
        self.scene.clear()
        self.image_item = QGraphicsPixmapItem(self.image)
        self.image_item.setFlag(QGraphicsPixmapItem.ItemIsMovable)
        self.scene.addItem(self.image_item)
        self.image_item.setOffset(self.sceneRect().center() - self.image_item.boundingRect().center())
        self.fitInView(self.image_item, Qt.KeepAspectRatio)
        self.show()
        self.scaleChanged.emit(self.get_fit_scale())

    def rotate_image(self):
        if self.image_item:
            self.current_angle += 90
            self.image_item.setRotation(self.current_angle)
            bounding_rect = self.image_item.boundingRect()
            self.image_item.setTransformOriginPoint(bounding_rect.center())
            self.center_image()
            if self.current_angle >= 360:
                self.current_angle = 0

    def center_image(self):
        if self.image_item:
            view_center = self.viewport().rect().center()
            scene_center = self.mapToScene(view_center)
            self.image_item.setPos(scene_center - self.image_item.boundingRect().center())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.image_item:
            self.fitInView(self.image_item, Qt.KeepAspectRatio)
            self.scaleChanged.emit(self.get_fit_scale())
    
    def mouseDoubleClickEvent(self, event):
        if self.image_item:
            self.fitInView(self.image_item, Qt.KeepAspectRatio)
            self.current_angle = 0
            self.image_item.setRotation(self.current_angle)
            self.center_image()
            self.scaleChanged.emit(self.get_fit_scale())

class CanvasQW(QWidget):
    scaleChanged = pyqtSignal(float) # 缩放比例改变时发出的信号
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.image = None # 存储原始图像数据
        self.scaled_image = None # 存储缩放后的图像数据
        self.scale = 1.0  # 当前图像的缩放比例
        self.offset = QPoint(0, 0) # 图像显示的偏移量
        self.dragging = False  # 标记是否正在拖动图像
        self.last_pos = QPoint()  # 记录鼠标拖动的上一个位置
        self.rotate = 0 # 旋转角度
        self.setMouseTracking(True) # 允许鼠标跟踪, 即使鼠标没有按下也能接收鼠标移动事件
        self.setFocusPolicy(Qt.ClickFocus) # 允许画布通过鼠标点击和键盘快捷键获取焦点

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        painter.setRenderHint(QPainter.TextAntialiasing, True)
        painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
        
        if self.image and self.scaled_image:
            painter.drawPixmap(QPointF(self.offset.x(), self.offset.y()), self.scaled_image)
    
    def set_image_center(self):
        '''将图像居中显示'''
        if self.image:
            # 获取考虑旋转后的图像尺寸
            if self.rotate % 180 == 0:  # 0度或180度
                img_width, img_height = self.image.width(), self.image.height()
            else:  # 90度或270度
                img_width, img_height = self.image.height(), self.image.width()
                
            # 计算缩放比例
            scale_width = self.width() / img_width
            scale_height = self.height() / img_height
            new_scale = min(scale_width, scale_height)
            
            # 如果缩放比例发生变化，则发出信号
            if new_scale != self.scale:
                self.scale = new_scale
                self.scaleChanged.emit(self.scale)
            else:
                self.scale = new_scale
            
            # 计算缩放后的尺寸
            scaled_width = int(img_width * self.scale)
            scaled_height = int(img_height * self.scale)
            
            # 计算偏移量使图像居中
            self.offset = QPoint(self.width() // 2 - scaled_width // 2, self.height() // 2 - scaled_height // 2)
            
            # 更新变换后的图像
            self.update_transformed_image()


    def load_image(self, image_path):
        self.image = QPixmap(image_path)
        if self.image:
            self.image_width, self.image_height = self.image.width(), self.image.height()
            self.rotate = 0  # 重置旋转角度
            self.set_image_center()
            self.update()
        else:
            self.scale = 1.0
            self.offset = QPoint(0, 0)
            self.rotate = 0  # 重置旋转角度

    def update_scaled_image(self):
        """根据当前缩放比例更新缩放后的图像"""
        if self.image:
            w, h = self.image.width(), self.image.height()
            scaled_h = int(h * self.scale)
            scaled_w = int(w * self.scale)
            self.scaled_image = self.image.scaled(scaled_w, scaled_h, Qt.KeepAspectRatio,Qt.SmoothTransformation)

    def rotate_image(self):
        '''图片旋转 +=90度'''
        if self.image:
            self.rotate += 90
            self.rotate %= 360
            self.update_transformed_image()  # 使用新的更新方法
            self.set_image_center()
            self.update()

    def reset_rotate_image(self):
        '''图片旋转恢复初始状态'''
        if self.image:
            self.rotate = 0
            self.update_transformed_image()  # 使用新的更新方法
            self.set_image_center()
            self.update()

    def update_transformed_image(self):
        """根据当前旋转角度和缩放比例更新变换后的图像"""
        if self.image:
            # 先旋转
            transform = QTransform().rotate(self.rotate)
            rotated_image = self.image.transformed(transform)
            
            # 再缩放
            w, h = rotated_image.width(), rotated_image.height()
            scaled_h = int(h * self.scale)
            scaled_w = int(w * self.scale)
            self.scaled_image = rotated_image.scaled(scaled_w, scaled_h, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def wheelEvent(self, event: QWheelEvent):
        """处理鼠标滚轮事件, 以鼠标为中心, 实现图像的缩放功能"""
        if self.image:
            scale_factor = 1.1 if event.angleDelta().y() > 0 else 0.9 
            old_scale = self.scale
            self.scale *= scale_factor
            self.scale = max(0.1, min(self.scale, 5.0))
            
            # 计算缩放前的鼠标在图像上的位置
            mouse_pos = event.pos()
            img_x = (mouse_pos.x() - self.offset.x()) / old_scale
            img_y = (mouse_pos.y() - self.offset.y()) / old_scale
            
            # 计算缩放后的偏移量，使鼠标下的图像点保持不变
            self.offset.setX(int(mouse_pos.x() - img_x * self.scale))
            self.offset.setY(int(mouse_pos.y() - img_y * self.scale))
            
            # 更新变换后的图像
            self.update_transformed_image()
            self.update()
            self.scaleChanged.emit(self.scale)
        super().wheelEvent(event)

    def resizeEvent(self, event):
        """处理窗口大小变化事件, 更新画布"""
        self.reset_view()

    def reset_view(self):
        """重置图像视图，恢复到初始缩放比例和位置"""
        self.update_scaled_image()
        self.set_image_center()
        self.update()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.RightButton:
            self.dragging = True
            self.last_pos = event.pos()
            self.setCursor(Qt.ClosedHandCursor)
            event.accept()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging and self.image is not None:
            delta = event.pos() - self.last_pos 
            self.offset += delta  # 更新图像显示的偏移量
            self.last_pos = event.pos()  # 记录当前鼠标位置
            self.update()
            event.accept()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.RightButton and self.dragging:
            self.dragging = False
            self.setCursor(Qt.ArrowCursor)
            event.accept()
        super().mouseReleaseEvent(event)