# -*- coding: UTF-8 -*-
"""
*@ description:
*@ name:	mainWindow.py
*@ author:  17_ayyy and DengBoFan
*@ time:	2024/11/29 10:42
"""

"""
    -TODO: 获取用户FPS,capture_index,algorithm算法并设置
    -TODO: 获取用户算法选择内容
    -TODO: 获取用户算法使用设置
    -TODO: 完成核心功能的开发

    TODO: 完成项目的打包和发布

    TODO: 添加年龄情绪识别
    TODO: 添加保存和点名报告功能
    TODO: 添加基于CNN特征提取算法
    TODO: 添加基于TransForm特征提取算法

"""

from PySide6.QtWidgets import QApplication,QMainWindow,QMessageBox
from PySide6.QtGui import QIcon,QImage,QPixmap
from PySide6.QtCore import QTimer
from mainWindow_V2_Ui import Ui_MainWindow
import cv2
import sys
sys.path.append('.') # todo .. 上级目录  

import os
import numpy as np
import joblib

from Algorithm.BOFF.boff import Boff
from Algorithm.BOFF_PCA.boff_pca import Boff_pca


class MainWindow(QMainWindow):
    def __init__(self):
        # 初始化界面
        super().__init__()
        self.setup_ui()
        self.connect_slot()
        # 属性
        self.capture = None
        self.fps = 100  # 每秒的显示帧数,fps = 1000/ time
        self.time = int(1000/self.fps) # 计时x ms,显示1帧,1s=1000ms
        self.capture_index = 0
        self.algorithm = "Based on Facial feature" # 初始值设置
        # 载入模型
        # todo
        self.load_model(model_path_npz= 'model\\tags_faces.npz', model_path_pca= 'model\\pca.joblib')
    
    def setup_ui(self):
        """
        初始化UI
        """
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Face Recognition")
        self.setWindowIcon(QIcon('GUI\\assets\\transparentLogo\\hebmu.ico'))
        self.ui.frame_label.setPixmap(QPixmap('GUI\\assets\\background\\initframe.png'))

    def connect_slot(self):
        """
        连接信号和槽
        """
        self.ui.start_Button.clicked.connect(self.start_capture)
        self.ui.stop_Button.clicked.connect(self.stop_capture)
        self.ui.start_Button_ico.clicked.connect(self.start_capture)
        self.ui.stop_Button_ico.clicked.connect(self.stop_capture)
        self.ui.fps_lineEdit.returnPressed.connect(self.set_fps)
        self.ui.captureIndex_lineEdit.returnPressed.connect(self.set_capture_index)
        self.ui.comboBox.currentIndexChanged.connect(self.set_algorithm)
        

    def start_capture(self):
        """
        开始捕获摄像头内容
        """
        self.ui.frame_label.clear()
        self.capture = cv2.VideoCapture(self.capture_index)
        width = 640
        height = 480
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
        if not self.capture.isOpened():
            QMessageBox.critical(self, "错误", "无法打开摄像头")
            return
        else:
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.display_frame)
            self.timer.start(self.time)
            QMessageBox.information(
                self,
                'Message',
                '摄像头已经成功开启'
            )

    def load_model(self,model_path_npz,model_path_pca):

        with np.load(model_path_npz) as sa:
            self.faces = sa["faces"]
            self.faces_r = sa["faces_r"]
            self.tags = sa["tags"]
            self.tags_labelEncoded = sa["tags_labelEncoded"]

        self.pca = joblib.load(model_path_pca)

    def display_frame(self):
        """
        展示摄像头捕获内容
        """
        ret, frame = self.capture.read()

        algorithm = self.algorithm
        
        # 3.10以上才使用
        # match algorithm:
        #     case "Based on Facial feature":
        #         frame = Boff(frame,self.faces,self.tags)
        #     case "Based on Facial feature and PCA":
        #         frame = Boff_pca(frame,self.faces,self.tags,self.pca)
        
        if algorithm == "Based on Facial feature":
            frame = Boff(frame,self.faces,self.tags)
        elif algorithm == "Based on Facial feature and PCA":
            frame = Boff_pca(frame,self.faces,self.tags,self.pca)
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            img = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)
            self.ui.frame_label.setPixmap(QPixmap.fromImage(img))
    
    def stop_capture(self):
        """
        停止捕获摄像头内容
        """
        if self.capture is not None:
            self.timer.stop()
            self.capture.release()
            self.capture = None
            self.ui.frame_label.clear()
            self.ui.frame_label.setPixmap(QPixmap("GUI\\assets\\background\\initframe.png"))
            QMessageBox.information(
                self,
                'Message',
                '摄像头已经成功关闭'
            )


    def set_fps(self):
        """
        获取用户FPS并设置
        """
        try:
            self.fps = int(self.ui.fps_lineEdit.text())
            QMessageBox.information(
                self,
                'Message',
                'FPS设置成功'
            )
        except Exception as e:
            QMessageBox.information(
                self,
                'Message',
                'FPS设置失败,请保证输入数字'
            )


    def set_capture_index(self):
        """
        获取用户摄像头索引并设置
        """
        try:
            self.capture_index = int(self.ui.captureIndex_lineEdit.text())
            QMessageBox.information(
                self,
                'Message',
                '摄像头索引设置成功'
            )
        except Exception as e:
            QMessageBox.information(
                self,
                'Message',
                '摄像头索引设置失败,请输入合理的相机索引'
            )


    def set_algorithm(self):
        """
        获取用户选择算法并设置
        """
        try:
            self.algorithm = self.ui.comboBox.currentText()
            QMessageBox.information(
                self,
                'Message',
                '算法设置成功'
            )
        except Exception as e:
            QMessageBox.information(
                self,
                'Message',
                '算法设置失败'
            )


    def set_information(self):
        """
        设置结果信息name,age,emotion
        """
        pass


    def closeEvent(self, event):
        """
        主界面关闭事件
            Args:event
            Returns:None
        """
        reply = QMessageBox.question(self,
                                     '退出',
                                     "是否确定退出嘛？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


