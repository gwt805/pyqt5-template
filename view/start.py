import sys, math, random
from PyQt5.QtCore import Qt, QTimer, QPointF, QRectF
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsItem, QDesktopWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont, QLinearGradient, QRadialGradient, QPainterPath, QFontMetrics, QWheelEvent, QTransform

class NoScrollGraphicsView(QGraphicsView):
    """自定义视图类，彻底禁用滚动和缩放"""
    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        # 禁用所有可能的交互
        self.setDragMode(QGraphicsView.NoDrag)
        self.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.setResizeAnchor(QGraphicsView.NoAnchor)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setOptimizationFlag(QGraphicsView.DontAdjustForAntialiasing)
        self.setInteractive(False)
        self.setMouseTracking(False)
        
        # 禁用滚动条
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        # 禁用缩放
        self.setRenderHint(QPainter.Antialiasing)
        self.setFrameShape(QGraphicsView.NoFrame)
        
        # 设置固定的变换矩阵，防止任何缩放或平移
        self.setTransform(QTransform())
        
    def wheelEvent(self, event: QWheelEvent):
        # 完全忽略鼠标滚轮事件
        event.ignore()
        
    def mousePressEvent(self, event):
        # 禁用鼠标按下事件
        event.ignore()
        
    def mouseMoveEvent(self, event):
        # 禁用鼠标移动事件
        event.ignore()
        
    def mouseReleaseEvent(self, event):
        # 禁用鼠标释放事件
        event.ignore()
        
    def mouseDoubleClickEvent(self, event):
        # 禁用双击事件
        event.ignore()
        
    def keyPressEvent(self, event):
        # 禁用键盘事件
        event.ignore()
        
    def resizeEvent(self, event):
        # 确保视图大小改变时不会影响变换
        super().resizeEvent(event)
        self.setTransform(QTransform())

class Particle(QGraphicsItem):
    """粒子类"""
    def __init__(self, scene_rect):
        super().__init__()
        # 在场景中间区域随机生成粒子，避免在边界生成
        margin = 50
        self.x = random.uniform(margin, scene_rect.width() - margin)
        self.y = random.uniform(margin, scene_rect.height() - margin)
        
        # 增加粒子速度范围，使运动更自然
        self.vx = random.uniform(-1.5, 1.5)
        self.vy = random.uniform(-1.5, 1.5)
        
        self.size = random.uniform(1, 3)
        self.life = 1.0
        self.decay = random.uniform(0.005, 0.02)
        self.scene_rect = scene_rect
        self.color = QColor(random.randint(100, 255), random.randint(100, 255), random.randint(150, 255))
        
        # 立即设置粒子位置，避免在(0,0)位置出现
        self.setPos(self.x, self.y)
        
    def boundingRect(self):
        return QRectF(-self.size, -self.size, self.size * 2, self.size * 2)
    
    def paint(self, painter, option, widget):
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        self.color.setAlphaF(self.life)
        painter.setBrush(QBrush(self.color))
        painter.drawEllipse(QPointF(0, 0), self.size, self.size)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= self.decay
        
        # 边界反弹 - 改进版，确保粒子不会卡在边界
        margin = 10
        if self.x < margin:
            self.x = margin
            self.vx = abs(self.vx)  # 确保速度向右
        elif self.x > self.scene_rect.width() - margin:
            self.x = self.scene_rect.width() - margin
            self.vx = -abs(self.vx)  # 确保速度向左
            
        if self.y < margin:
            self.y = margin
            self.vy = abs(self.vy)  # 确保速度向下
        elif self.y > self.scene_rect.height() - margin:
            self.y = self.scene_rect.height() - margin
            self.vy = -abs(self.vy)  # 确保速度向上
            
        self.setPos(self.x, self.y)
        return self.life > 0

class WireframeCube(QGraphicsItem):
    """3D线框立方体 - 使用正交投影，每个面大小相同"""
    def __init__(self, size=100):
        super().__init__()
        self.size = size
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0
        self.vertices = [
            [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # 后面
            [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]       # 前面
        ]
        self.edges = [
            [0, 1], [1, 2], [2, 3], [3, 0],  # 后面
            [4, 5], [5, 6], [6, 7], [7, 4],  # 前面
            [0, 4], [1, 5], [2, 6], [3, 7]   # 连接线
        ]
        
    def boundingRect(self):
        return QRectF(-self.size * 2, -self.size * 2, self.size * 4, self.size * 4)
    
    def paint(self, painter, option, widget):
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 创建渐变画笔
        gradient = QLinearGradient(-self.size, -self.size, self.size, self.size)
        gradient.setColorAt(0, QColor(0, 255, 255))
        gradient.setColorAt(0.5, QColor(255, 0, 255))
        gradient.setColorAt(1, QColor(255, 255, 0))
        
        pen = QPen(gradient, 2)
        painter.setPen(pen)
        
        # 3D变换 - 使用正交投影
        rotated_vertices = []
        for vertex in self.vertices:
            # 旋转变换
            x, y, z = vertex
            
            # 绕X轴旋转
            y_rot = y * math.cos(self.angle_x) - z * math.sin(self.angle_x)
            z_rot = y * math.sin(self.angle_x) + z * math.cos(self.angle_x)
            y, z = y_rot, z_rot
            
            # 绕Y轴旋转
            x_rot = x * math.cos(self.angle_y) + z * math.sin(self.angle_y)
            z_rot = -x * math.sin(self.angle_y) + z * math.cos(self.angle_y)
            x, z = x_rot, z_rot
            
            # 绕Z轴旋转
            x_rot = x * math.cos(self.angle_z) - y * math.sin(self.angle_z)
            y_rot = x * math.sin(self.angle_z) + y * math.cos(self.angle_z)
            x, y = x_rot, y_rot
            
            # 正交投影 - 直接使用x,y坐标，忽略z坐标
            # 这样每个面的大小都会保持一致
            screen_x = x * self.size
            screen_y = y * self.size
            
            rotated_vertices.append([screen_x, screen_y])
        
        # 绘制边框 - 只绘制原始的立方体边框，不添加额外线条
        for edge in self.edges:
            p1 = rotated_vertices[edge[0]]
            p2 = rotated_vertices[edge[1]]
            painter.drawLine(QPointF(p1[0], p1[1]), QPointF(p2[0], p2[1]))
    
    def update_rotation(self):
        self.angle_x += 0.01
        self.angle_y += 0.015
        self.angle_z += 0.005
        self.update()

class GlowingText(QGraphicsItem):
    """发光文字效果"""
    def __init__(self, text, font_size=48):
        super().__init__()
        self.text = text
        self.font_size = font_size
        
    def boundingRect(self):
        font = QFont("Arial", self.font_size, QFont.Bold)
        fm = QFontMetrics(font)
        text_width = fm.width(self.text)
        text_height = fm.height()
        return QRectF(-text_width/2 - 5, -text_height/2 - 5, text_width + 10, text_height + 10)
    
    def paint(self, painter, option, widget):
        painter.setRenderHint(QPainter.Antialiasing)
        
        font = QFont("Arial", self.font_size, QFont.Bold)
        painter.setFont(font)
        
        # 获取文字尺寸
        fm = QFontMetrics(font)
        text_width = fm.width(self.text)
        text_height = fm.height()
        
        # 创建文字路径，并调整位置使文字中心在(0,0)
        path = QPainterPath()
        # 计算文字基线位置，使文字垂直居中
        baseline_y = fm.ascent() - text_height/2
        path.addText(-text_width/2, baseline_y, font, self.text)
        
        # 绘制主文字渐变（固定颜色，不变化）
        gradient = QLinearGradient(-text_width/2, -text_height/2, text_width/2, text_height/2)
        gradient.setColorAt(0, QColor(255, 255, 255))      # 白色
        gradient.setColorAt(0.5, QColor(0, 255, 255))       # 青色
        gradient.setColorAt(1, QColor(255, 0, 255))         # 品红色
        
        painter.setPen(QPen(Qt.NoPen))
        painter.setBrush(QBrush(gradient))
        painter.drawPath(path)
        
        # 绘制文字边框
        painter.setPen(QPen(QColor(255, 255, 255), 1))
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path)
    
    def update_animation(self):
        # 不需要更新，颜色固定
        pass

class StartWindow(QMainWindow):
    """启动页面"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.center_window()
        
    def initUI(self):
        self.setWindowTitle("MI-Tool-Plus 启动中...")
        self.setFixedSize(800, 550)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # 创建场景
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 800, 550)  # 设置场景大小与窗口一致
        
        # 创建自定义视图（禁用滚动和交互）
        self.view = NoScrollGraphicsView(self.scene, self)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setGeometry(0, 0, 800, 550)
        self.view.setStyleSheet("background: transparent;")
        self.view.setFrameShape(QGraphicsView.NoFrame)  # 移除边框
        
        # 创建背景渐变
        gradient = QRadialGradient(400, 300, 400)
        gradient.setColorAt(0, QColor(20, 20, 40))
        gradient.setColorAt(1, QColor(0, 0, 0))
        self.scene.setBackgroundBrush(QBrush(gradient))
        
        # 创建粒子系统
        self.particles = []
        self.scene_rect = QRectF(0, 0, 800, 550)  # 保存场景矩形引用
        for _ in range(100):
            particle = Particle(self.scene_rect)
            self.particles.append(particle)
            self.scene.addItem(particle)
        
        # 创建3D线框立方体（位置调整到上方）
        self.cube = WireframeCube(80)
        self.cube.setPos(400, 180)  # 调整位置到上方
        self.scene.addItem(self.cube)
        
        # 创建发光文字（居中显示）
        self.text = GlowingText("PyQt5-Template", 48)
        self.text.setPos(400, 450)  # 窗口正中心
        self.scene.addItem(self.text)
        
        # 启动动画定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(16)  # 约60 FPS
        
        # 淡入动画
        self.opacity = 0
        self.fade_timer = QTimer(self)
        self.fade_timer.timeout.connect(self.fade_in)
        self.fade_timer.start(16)
        
    def fade_in(self):
        self.opacity += 0.02
        if self.opacity >= 1:
            self.opacity = 1
            self.fade_timer.stop()
        self.setWindowOpacity(self.opacity)
        
    def update_animation(self):
        # 更新粒子
        for particle in self.particles[:]:
            if not particle.update():
                # 先隐藏粒子，避免闪烁
                particle.hide()
                self.scene.removeItem(particle)
                self.particles.remove(particle)
                # 添加新粒子，使用保存的场景矩形引用
                new_particle = Particle(self.scene_rect)
                self.particles.append(new_particle)
                self.scene.addItem(new_particle)
        
        # 更新立方体旋转
        self.cube.update_rotation()
        
        # 文字不需要更新动画，颜色固定

    def center_window(self):
        """将窗口居中显示在屏幕上"""
        screen_geometry = QDesktopWidget().screenGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
